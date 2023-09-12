import json
from django.conf import settings
from django.shortcuts import render, redirect
from businessplace_app.api.serializers import BusinessPlaceSerializer
from test_app.forms import BusinessPlaceEditForm, BusinessPlaceForm, EmployeeForm, PaymentForm
from businessplace_app.models import BusinessPlace, BusinessType
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response

import boto3
import base64

from django.db import connection
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from payment_app.models import Payment
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordChangeView
from payment_app.models import Payment
from django.urls import reverse_lazy
import googlemaps

from trip_app.models import Trip


def addTripClone(request, pkMain, pkClone):
    data_list_clone = []
    try:
        with connection.cursor() as cursor:
            sql = f"""
                select 
                    td.id as tripDetailCloneID,
                    place_id,
                    td.trip_id as tripCloneID
                from PLANTRIPDB.TripDetail as td
                inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
                where t.id = {pkClone}
                ;
            """
            cursor.execute(sql)
            data_read = cursor.fetchall()

            for row in data_read:
                data_list_clone.append({
                    "tripDetailCloneID": str(row[0]),
                    "place_id": str(row[1]),
                    "tripCloneID": str(row[-1]),
                })

            for row in data_list_clone:
                sql = f"""
                    insert into PLANTRIPDB.TripDetail (place_id, trip_id, chkIn)
                    value ({row['place_id']}, {pkMain}, 0)
                    ;
                """
                cursor.execute(sql)
    except Exception as e:
        print("Error addTripClone: " + str(e))
    
    print("Success addTripClone.")
    

def getListTripDetailClone(request, pk):
    data_list = []

    with connection.cursor() as cursor:
        sql = f"""
            SELECT 
                td.id as id_trip_detail,
                place_id,
                p.name as place_name,
                lat,
                lng,
                minPrice,
                maxPrice,
                pic1,
                trip_id,
                t.name as trip_name,
                t.budget as trip_budget,
                t.detail as trip_detail,
                t.position_start,
                t.position_end,
                user_id,
                username
            FROM PLANTRIPDB.TripDetail as td
            inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
            inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
            inner join PLANTRIPDB.auth_user as u on u.id = user_id
            where t.id = {pk}
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "id_trip_detail": str(row[0]),
            "place_id": str(row[1]),
            "place_name": str(row[2]),
            "lat": str(row[3]),
            "lng": str(row[4]),
            "minPrice": str(row[5]),
            "maxPrice": str(row[6]),
            "pic1": str("https://plantripbucket.s3.amazonaws.com/"+row[7]),
            "trip_id": str(row[8]),
            "trip_name": str(row[9]),
            "trip_budget": str(row[10]),
            "trip_detail": str(row[11]),
            "position_start": str(row[12]),
            "position_end": str(row[13]),
            "user_id": str(row[14]),
            "username": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def getSorTriptWithtripBudget(request, budget):
    data_list = []
    bg = 0.0
    try:
        bg = float(budget)
    except ValueError as e:
        bg = 0.0
        print("error: ", e)

    with connection.cursor() as cursor:
        sql = f"""
            select 
                t.id,
                t.name,
                t.position_start,
                t.position_end,
                t.budget,
                username,
                pic1
            from PLANTRIPDB.TripDetail as td
            inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
            inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
            inner join PLANTRIPDB.auth_user as u on t.user_id = u.id
            where t.budget <= {bg}
            group by trip_id
            order by t.budget
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "id": str(row[0]),
            "name": str(row[1]),
            "position_start": str(row[2]),
            "position_end": str(row[3]),
            "budget": str(row[4]),
            "username": str(row[5]),
            "pic1": str("https://plantripbucket.s3.amazonaws.com/"+row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def getSorTriptWithUseTrip(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
        select 
            count(*) as count_use, 
            tc.tripClone_id, 
            t.name, 
            t.position_start, 
            t.position_end, 
            t.budget, 
            username,
            pic1
        from PLANTRIPDB.TripClone as tc
        inner join PLANTRIPDB.Trip as t on tc.tripClone_id = t.id
        inner join PLANTRIPDB.TripDetail as td on td.trip_id = tc.tripClone_id
        inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
        inner join PLANTRIPDB.auth_user as u on t.user_id = u.id
        group by tc.tripClone_id 
        order by count_use desc
        ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "count_use": str(row[0]),
            "tripClone_id": str(row[1]),
            "name": str(row[2]),
            "position_start": str(row[3]),
            "position_end": str(row[4]),
            "budget": str(row[5]),
            "username": str(row[6]),
            "pic1": str("https://plantripbucket.s3.amazonaws.com/"+row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def getSorPlacetWithUsePlace(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT 
                count(*) as count_use_place,
                p.id as place_id, 
                p.name as place_name, 
                p.detail, 
                lat, 
                lng, 
                district,
                address, 
                timeOpen, 
                timeClose, 
                website,
                type_id, 
                bt.name as type_name,
                place_user_id, 
                au.username, 
                au.email,
                pic1, 
                pic2, 
                pic3, 
                vr, 
                minPrice, 
                maxPrice
            FROM PLANTRIPDB.TripDetail as td
            inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
            inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
            INNER JOIN PLANTRIPDB.auth_user as au ON p.place_user_id = au.id 
            INNER JOIN PLANTRIPDB.BusinessType as bt ON p.type_id = bt.id  
            group by place_id
            order by count_use_place desc
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()
        print(data_read[-1])

    for row in data_read:
        data_list.append({
            "count_use_place": str(row[0]),
            "place_id": str(row[1]),
            "place_name": str(row[2]),
            "detail": str(row[3]),
            "lat": str(row[4]),
            "lng": str(row[5]),
            "district": str(row[6]),
            "address": str(row[7]),
            "timeOpen": str(row[8]),
            "timeClose": str(row[9]),
            "website": str(row[10]),
            "type_id": str(row[11]),
            "type_name": str(row[12]),
            "place_user_id": str(row[13]),
            "username": str(row[14]),
            "email": str(row[15]),
            "pic1": str(row[16]),
            "pic2": str(row[17]),
            "pic3": str(row[18]),
            "vr": str(row[19]),
            "minPrice": str(row[20]),
            "maxPrice": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def getSortPlaceWithTripBudget(request, pk):
    trip = Trip.objects.get(pk=pk)
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT 
                bp.id as place_id, 
                bp.name as place_name, 
                bp.detail, 
                lat, 
                lng, 
                district,
                address, 
                timeOpen, 
                timeClose, 
                website,
                type_id, 
                bt.name as type_name,
                place_user_id, 
                au.username, 
                au.email,
                pic1, 
                pic2, 
                pic3, 
                vr, 
                minPrice, 
                maxPrice
            FROM PLANTRIPDB.BusinessPlace as bp
            INNER JOIN PLANTRIPDB.auth_user as au
                ON bp.place_user_id = au.id 
            INNER JOIN PLANTRIPDB.BusinessType as bt
                ON bp.type_id = bt.id  
            where maxPrice <= {trip.budget}
            order by maxPrice;
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()
        print(data_read[-1])

    for row in data_read:
        data_list.append({
            "place_id": str(row[0]),
            "place_name": str(row[1]),
            "detail": str(row[2]),
            "lat": str(row[3]),
            "lng": str(row[4]),
            "district": str(row[5]),
            "address": str(row[6]),
            "timeOpen": str(row[7]),
            "timeClose": str(row[8]),
            "website": str(row[9]),
            "type_id": str(row[10]),
            "type_name": str(row[11]),
            "place_user_id": str(row[12]),
            "username": str(row[13]),
            "email": str(row[14]),
            "pic1": str(row[15]),
            "pic2": str(row[16]),
            "pic3": str(row[17]),
            "vr": str(row[18]),
            "minPrice": str(row[19]),
            "maxPrice": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def getScorePlace(request):
    data_list = []
    try:
        with connection.cursor() as cursor:
            sql = f"""
                    SELECT sum(score) as score_place, place_id, name
                    FROM PLANTRIPDB.RatingAndComment as rac
                    inner join PLANTRIPDB.BusinessPlace as p on rac.place_id = p.id
                    where p.place_user_id = {request.user.id}
                    group by place_id
                    ;
            """
            cursor.execute(sql)
            data_read = cursor.fetchall()

            for row in data_read:
                data_list.append({
                    "score_place": row[0],
                    "place_id": row[1],
                    "name": row[-1],
                })

    except Exception as e:
        print("Error: ", e)

    return data_list


def getRacPlace(request, pk):
    data_list = []
    try:
        with connection.cursor() as cursor:
            sql = f"""
                SELECT 
                    rac.id as rac_id,
                    score,
                    comment,
                    created_datetime,
                    place_id,
                    p.name as name_place,
                    user_id,
                    username
                FROM PLANTRIPDB.RatingAndComment as rac
                inner join PLANTRIPDB.BusinessPlace as p on rac.place_id = p.id
                inner join PLANTRIPDB.auth_user as u on rac.user_id = u.id
                where p.place_user_id = {request.user.id} and rac.place_id = {pk}
                ;
            """
            cursor.execute(sql)
            data_read = cursor.fetchall()
            print(data_read[0])

            for row in data_read:
                data_list.append({
                    "rac_id": row[0],
                    "score": row[1],
                    "comment": row[2],
                    "created_datetime": row[3],
                    "place_id": row[4],
                    "name_place": row[5],
                    "user_id": row[6],
                    "username": row[-1],
                })
    except Exception as e:
        print("Error=", e)

    return data_list


@login_required
def open_report(request, pk):
    place_use = getCountUsePlace(request)
    place_score = getScorePlace(request)
    if request.method == 'POST':
        search_query = request.POST['search_query']
        print("search=", search_query)
        places = BusinessPlace.objects.filter(name__contains=search_query)

        if place_score == [] or None:
            return render(request, "report_detail_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "report_detail_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })
    else:
        places = getRacPlace(request, pk)
        p = Paginator(places, 10)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        if place_score == [] or None:
            return render(request, "report_detail_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "report_detail_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })


@login_required
def report(request):
    place_use = getCountUsePlace(request)
    place_score = getScorePlace(request)
    if request.method == 'POST':
        search_query = request.POST['search_query']
        print("search=", search_query)
        places = BusinessPlace.objects.filter(name__contains=search_query)
        if place_score == [] or None:
            return render(request, "report_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "report_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })
    else:
        user_id = request.user.id
        places = BusinessPlace.objects.filter(place_user_id=user_id)
        p = Paginator(places, 10)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        if place_score == [] or None:
            return render(request, "report_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "report_business.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })


def get_list_place_with_distance2(request, pk, lat, lng):
    api_key = 'AIzaSyBOtQTtAbg0Rfl7RQ1WPjEjPw6Pg5pu9TA'
    gmaps = googlemaps.Client(key=api_key)
    lat_start_position = 0.0
    lng_start_position = 0.0

    data_list = []
    list_place_with_distance = []
    with connection.cursor() as cursor:
        sql = f"""
        SELECT  
            td.id as trip_detail_id,
            trip_id,
            t.name as trip_name,
            position_start,
            position_end,
            place_id,
            p.name as place_name,
            p.lat,
            p.lng,
            d.lat as start_lat,
            d.lng as start_lng,
            p.minPrice,
            p.maxPrice,
            chkIn
        FROM PLANTRIPDB.TripDetail as td
        inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
        inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
        inner join PLANTRIPDB.District as d on position_start = d.name
        where trip_id = {pk};
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "trip_detail_id": str(row[0]),
            "trip_id": str(row[1]),
            "trip_name": str(row[2]),
            "position_start": str(row[3]),
            "position_end": str(row[4]),
            "place_id": str(row[5]),
            "place_name": str(row[6]),
            "lat": str(row[7]),
            "lng": str(row[8]),
            "start_lat": str(row[9]),
            "start_lng": str(row[10]),
            "minPrice": str(row[11]),
            "maxPrice": str(row[12]),
            "chkIn": str(row[-1]),
        })

    try:
        lat = float(lat)
        lng = float(lng)
        lat_start_position = lat
        lng_start_position = lng
    except ValueError as e:
        lat_start_position = p['start_lat']
        lng_start_position = p['start_lng']
        print("error: ", e)

    # Find shortest path
    for p in data_list:
        point1 = (lat_start_position, lng_start_position)
        point2 = (p['lat'], p['lng'])

        distance_matrix = gmaps.distance_matrix(point1, point2)

        distance_meters = distance_matrix['rows'][0]['elements'][0]['distance']['value']

        list_place_with_distance.append(
            {
                'trip_detail_id': p['trip_detail_id'],
                'trip_id': p['trip_id'],
                'trip_name': p['trip_name'],
                'position_start': p['position_start'],
                'position_end': p['position_end'],
                'place_id': p['place_id'],
                'place_name': p['place_name'],
                'lat': p['lat'],
                'lng': p['lng'],
                'distance': distance_meters / 1000,
                'minPrice': p['minPrice'],
                'maxPrice': p['maxPrice'],
                'chkIn': p['chkIn'],

            }
        )
    sorted_list_descending = sorted(
        list_place_with_distance, key=lambda x: x["distance"])

    json_data = json.dumps(sorted_list_descending,
                           ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


def get_list_place_with_distance(request, pk):
    api_key = 'AIzaSyBOtQTtAbg0Rfl7RQ1WPjEjPw6Pg5pu9TA'
    gmaps = googlemaps.Client(key=api_key)
    lat_start_position = 0.0
    lng_start_position = 0.0
    data_list = []
    list_place_with_distance = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT  
                td.id as trip_detail_id,
                trip_id,
                t.name as trip_name,
                position_start,
                position_end,
                place_id,
                p.name as place_name,
                p.lat,
                p.lng,
                d.lat as start_lat,
                d.lng as start_lng
            FROM PLANTRIPDB.TripDetail as td
            inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
            inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
            inner join PLANTRIPDB.District as d on position_start = d.name
            where trip_id = {pk};
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "trip_detail_id": str(row[0]),
            "trip_id": str(row[1]),
            "trip_name": str(row[2]),
            "position_start": str(row[3]),
            "position_end": str(row[4]),
            "place_id": str(row[5]),
            "place_name": str(row[6]),
            "lat": str(row[7]),
            "lng": str(row[8]),
            "start_lat": str(row[9]),
            "start_lng": str(row[-1]),
        })

    # print(data_list[0]['lat'])

    # Find shortest path
    for p in data_list:
        point1 = (p['start_lat'], p['start_lng'])
        point2 = (p['lat'], p['lng'])

        distance_matrix = gmaps.distance_matrix(point1, point2)

        distance_meters = distance_matrix['rows'][0]['elements'][0]['distance']['value']

        list_place_with_distance.append(
            {
                'trip_detail_id': p['trip_detail_id'],
                'trip_id': p['trip_id'],
                'trip_name': p['trip_name'],
                'position_start': p['position_start'],
                'position_end': p['position_end'],
                'place_id': p['place_id'],
                'place_name': p['place_name'],
                'lat': p['lat'],
                'lng': p['lng'],
                'distance': distance_meters / 1000
            }
        )
    sorted_list_descending = sorted(
        list_place_with_distance, key=lambda x: x["distance"])

    json_data = json.dumps(sorted_list_descending,
                           ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response


@login_required
def update_payment(request, pk):
    user = request.user
    pay = Payment.objects.get(pk=pk)
    form = PaymentForm(request.POST, request.FILES, instance=pay)
    upload_img = get_image_url(pay.upload_img)

    if form.is_valid():
        print("FORM IS VALID")
        messages.success(request, "ชำระค่าบริการสำเร็จแล้ว.")
        form.save()
        return redirect('/test/payment/')
    else:
        print("form error:", form.errors)
        messages.error(
            request, "ชำระค่าบริการไม่สำเร็จ กรุณาตรวจสอบข้อมูลที่ป้อนและลองใหม่อีกครั้ง.")
        return render(
            request,
            "edit_payment.html", {
                'pay': pay,
                'upload_img': upload_img
            }
        )


@login_required
def payment(request, pk):
    pay = Payment.objects.get(pk=pk)
    upload_img = get_image_url(pay.upload_img)

    return render(
        request,
        "edit_payment.html", {
            'pay': pay,
            'upload_img': upload_img,
            'user_id': request.user.id,
        }
    )


@login_required
def index_payment(request):
    user_id = request.user.id
    pay = Payment.objects.filter(
        customer=request.user).filter(payment_status=False)
    p = Paginator(pay, 10)
    page_number = request.GET.get('page')

    datetime_pay = pay[0].payment_date
    day = datetime_pay.day
    month = datetime_pay.month
    year = datetime_pay.year

    print("date", day, month, year)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'payment': page_obj}
    return render(request, 'payment.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "รหัสผ่านถูกเปลี่ยนแล้ว."
    success_url = reverse_lazy('test:test_index')


def get_list_place(request):

    data_list = []
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                bp.id as place_id, bp.name as place_name, detail, lat, lng, district,
                address, timeOpen, timeClose, website,
                type_id, bt.name as type_name,
                place_user_id, au.username, au.email
                pic1, pic2, pic3, vr
            FROM PLANTRIPDB.BusinessPlace as bp
            INNER JOIN PLANTRIPDB.auth_user as au
                ON bp.place_user_id = au.id 
            INNER JOIN PLANTRIPDB.BusinessType as bt
                ON bp.type_id = bt.id               
        """)
        data_read = cursor.fetchall()
        print(data_read[0])

    for row in data_read:
        data_list.append({
            "place_id": str(row[0]),
            "place_name": str(row[1]),
            "detail": str(row[2]),
            "lat": str(row[3]),
            "lng": str(row[4]),
            "district": str(row[5]),
            "address": str(row[6]),
            "timeOpen": str(row[7]),
            "timeClose": str(row[8]),
            "website": str(row[9]),
            "type_id": str(row[10]),
            "type_name": str(row[11]),
            "place_user_id": str(row[12]),
            "username": str(row[13]),
            "email": str(row[14]),
            "pic1": str(row[15]),
            "pic2": str(row[16]),
            "pic3": str(row[17]),
            "vr": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response
    # return render(request, "image_template.html",)


def get_image_url(image_key):

    return "https://plantripbucket.s3.amazonaws.com/"+str(image_key)


def image_view(request, pk):

    instance = BusinessPlace.objects.get(pk=pk)
    context = {'pic1': instance.pic1.name}
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    try:
        response = s3.get_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=instance.pic1.name)

        url = s3.generate_presigned_url('get_object',
                                        Params={
                                            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                            'Key': instance.pic1.name,
                                        },
                                        ExpiresIn=3600)
        image_data = response['Body'].read()

        image_base64 = base64.b64encode(image_data).decode('utf-8')

        context = {
            'image_data': url,
        }
        print("Image=", type(image_data))
        print("Image-URL=", url)
        # return HttpResponse(image_data, content_type=content_type)
        return render(request, "image_template.html", context)

    except Exception as e:
        return HttpResponse('Image not found', status=404)
    # return render(request, 'image_template.html', context)


@login_required
def update_profile(request):

    if request.method == 'POST':
        pk = request.user.id
        username = request.user.username
        try:
            temp = request.POST.get('username')
            print("temp=", temp)
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            with connection.cursor() as cursor:
                sql = f"""
                    UPDATE PLANTRIPDB.auth_user
                    SET 
                        username = "{username}", 
                        first_name = "{first_name}", 
                        last_name = "{last_name}", 
                        email = "{email}"
                    WHERE id = {pk};
                    """
                cursor.execute(sql)
            messages.success(request, "แก้ไขโปรไฟลไฟลสำเร็จแล้ว.")
            return redirect('/test/index_business/')
        except Exception as e:
            print("Error=", e)
            messages.warning(
                request, "แก้ไขโปรไฟลไฟลไม่สำเร็จ กรุณาตรวจสอบข้อมูล.")
            return redirect('/test/index_business/')

    if request.user.is_authenticated:
        pk = request.user.id
        with connection.cursor() as cursor:
            sql = f"""
                SELECT id, username, first_name, last_name, email FROM PLANTRIPDB.auth_user where id = {pk};
            """
            cursor.execute(sql)
            data_read = cursor.fetchone()

        context = {
            "id": data_read[0],
            "username": data_read[1],
            "first_name": data_read[2],
            "last_name": data_read[3],
            "email": data_read[4],
        }
        return render(request, 'edit_profile.html', {'user': context})
    else:
        messages.success(request, "คุณต้องลงชื่อเข้าใช้ก่อน.")
        return redirect('/test/index_business/')


def payment_create(request):
    payment_date = datetime.now()
    if payment_date.day == 1:
        payment_status = False
        price = 300.00

        group_name = 'business'
        users_in_group = User.objects.filter(groups__name=group_name)
        print(users_in_group)
        try:
            for user in users_in_group:
                print("Add Payment to ", user.username,
                      " on [", str(payment_date), "], price=", price)
                p = Payment.objects.create(
                    payment_status=payment_status, price=price, payment_date=payment_date, customer=user)
                print("p=", p)
        except PageNotAnInteger:
            print("Payment Create Failed.")
            return HttpResponse("<h1>Payment Create Failed.</h1>")
        print("Payment Create Successfully.")
        return HttpResponse("<h1>Payment Create Successfully.</h1>")
    return HttpResponse("<h1>Payment Not Create.</h1>")


def getCountUsePlace(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
                SELECT 
                    count(*) as count_use_place,
                        place_id,
                        p.name as place_name,
                        trip_id
                FROM PLANTRIPDB.TripDetail as td
                inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
                inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
                where p.place_user_id = {request.user.id}
                group by place_id
                order by count_use_place DESC
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()

    for row in data_read:
        data_list.append({
            "count_use_place": row[0],
            "place_id": row[1],
            "place_name": row[2],
            "trip_id": row[-1],
        })
    return data_list


@login_required
def index(request):
    place_use = getCountUsePlace(request)
    place_score = getScorePlace(request)
    if request.method == 'POST':
        search_query = request.POST['search_query']
        print("search=", search_query)
        places = BusinessPlace.objects.filter(name__contains=search_query)
        if place_score == [] or None:
            return render(request, "index.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "index.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })
    else:
        user_id = request.user.id
        places = BusinessPlace.objects.filter(place_user_id=user_id)
        p = Paginator(places, 10)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        if place_score == [] or None:
            return render(request, "index.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           })
        else:
            return render(request, "index.html",
                          {'places': places, 'place_use': place_use[0], "place_use_nagative": place_use[-1],
                           'place_score': place_score[0], "place_score_nagative": place_score[-1]
                           })


def logout_user(request):
    logout(request)
    messages.success(request, "ออกจากระบบแล้ว.")
    return redirect("/",)


def getTotalPaymentValid(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT sum(price) as total_payment_valid
            FROM PLANTRIPDB.Payment
            WHERE payment_status = True
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchone()

    for row in data_read:
        data_list.append({
            "total_payment_valid": row,
        })
    return data_list[0]


def getCountPayment(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT count(*) as count_payment
            FROM PLANTRIPDB.Payment
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchone()

    for row in data_read:
        data_list.append({
            "count_payment": row,
        })
    return data_list[0]


def getCountPaymentIsNCheck(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT count(price) as count_payment_isn_check
            FROM PLANTRIPDB.Payment
            WHERE payment_status = False
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchone()

    for row in data_read:
        data_list.append({
            "count_payment_isn_check": row,
        })
    return data_list[0]


def getCountPaymentIsCheck(request):
    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT count(price) as count_payment_isn_check
            FROM PLANTRIPDB.Payment
            WHERE payment_status = True
            ;
        """
        cursor.execute(sql)
        data_read = cursor.fetchone()

    for row in data_read:
        data_list.append({
            "count_payment_is_check": row,
        })
    return data_list[0]


@login_required
def index_admin(request):
    totalPaymentValid = getTotalPaymentValid(request)
    countPayment = getCountPayment(request)
    countPaymentIsNCheck = getCountPaymentIsNCheck(request)
    countPaymentIsCheck = getCountPaymentIsCheck(request)
    context = {
        'totalPaymentValid': totalPaymentValid['total_payment_valid'],
        'countPaymentValid': countPayment['count_payment'],
        'countPaymentIsCheck': countPaymentIsCheck['count_payment_is_check'],
        'countPaymentIsNCheck': countPaymentIsNCheck['count_payment_isn_check']
    }
    return render(request, 'index_admin.html', context)


def index_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                user = request.user
            if user.is_staff:
                # admin_login_url = reverse('admin:login')
                return redirect('/test/index_admin/')
            elif user.groups.filter(name="business").exists():
                messages.success(request, 'ยินดีตอนรับสู่ PlanTrip')
                return redirect('/test/index_business/')
            else:
                messages.warning(
                    request, 'สำหรับผู้ใช้กิจการและผู้ดูแลระบบเท่านั้น.')
                return render(request, '../templates/main/home.html', {})

        else:
            messages.error(
                request, 'เข้าสู่ระบบไม่สำเร็จ กรุณาตรวจสอบ ชื่อผู้ใช้และรหัสผ่าน. ')
            return render(request, "login.html",)

    return render(request, "login.html",)


def signup_business(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 != password2:
                messages.error(
                    request, "รหัสผ่านทั้งสองไม่ตรงกัน กรุณาป้อนรหัสผ่านใหม่อีกครั้ง.")
                return render(request, 'singup.html', error_messages)

            instance_user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            instance_user.save()

            group = Group.objects.get(name='business')
            instance_user.groups.add(group)
            messages.success(request, 'ลงทะเบียนสำเร็จ.')
            return redirect('/test/login/')

        except Exception as error:
            print("ERROR singup_business: ", error)
            error_messages = {
                "error": True,
                "message": "สมัครใช้บริการไม่สำเร็จ."
            }
            messages.error(
                request, "เกิดข้อผิดพลาดขึ้น การสมัครใช้บริการไม่สำเร็จ กรุณาลองใหม่อีกครั้ง.")
            return render(request, 'singup.html', error_messages)
    return render(request, 'singup.html')


@login_required
def addnew(request):

    # เพิ่มโดยใช้ RAW SQL เลย
    user_id = request.user.id
    user_name = request.user.username
    hours = [str(hour).zfill(2) for hour in range(24)]
    minutes = [str(minute).zfill(2) for minute in range(61)]

    if request.method == "POST":
        from datetime import datetime
        hour_open = request.POST.get('hour-open')
        hour_close = request.POST.get('hour-close')
        minute_open = request.POST.get('minute-open')
        minute_close = request.POST.get('minute-close')

        name = request.POST.get('name')
        district = request.POST.get('district')
        type = request.POST.get('type')
        address = request.POST.get('address')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        detail = request.POST.get('detail')
        timeOpen = request.POST.get('timeOpen')
        timeClose = request.POST.get('timeClose')
        minPrice = request.POST.get('minPrice')
        maxPrice = request.POST.get('maxPrice')
        website = request.POST.get('website')
        pic1 = request.POST.get('pic1')
        pic2 = request.POST.get('pic2')
        pic3 = request.POST.get('name')
        vr = request.POST.get('vr')
        place_user = request.POST.get('place_user')

        time_open = str(hour_open) + ":" + str(minute_open) + str(":00")
        time_close = str(hour_close) + ":" + str(minute_close) + str(":00")

        place = BusinessPlace(
            name=name,
            district=district,
            type=BusinessType.objects.get(pk=int(type)),
            address=address,
            lat=lat,
            lng=lng,
            detail=detail,
            timeOpen=time_open,
            timeClose=time_close,
            minPrice=minPrice,
            maxPrice=maxPrice,
            website=website,
            pic1=pic1,
            pic2=pic2,
            pic3=pic3,
            vr=vr,
            place_user=User.objects.get(pk=int(place_user)),
        )
        # print("place,", place)

        # ลองหาวิธีเพิ่ม ข้อมูลที่ละตัวใน form
        form = BusinessPlaceForm(
            request.POST, request.FILES, instance=place
        )

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "เพิ่มกิจการสำเร็จแล้ว.")
                return redirect('/test/index_business/')
            except Exception as e:
                messages.error(
                    request, "เกิดข้อผิดพลาดขึ้น การเพิ่มกิจการไม่สำเร็จ กรุณาลองใหม่อีกครั้ง.")
                print('Error saving:', e)
    else:
        form = BusinessPlaceForm()
    return render(request, "form_add.html", {'form': form, 'user_id': user_id, 'username': user_name, 'hours': hours, 'minutes': minutes})


@login_required
def edit(request, pk):
    user_id = request.user.id
    user_name = request.user.username
    place = BusinessPlace.objects.get(pk=pk)
    pic1_url = get_image_url(place.pic1)
    pic2_url = get_image_url(place.pic2)
    pic3_url = get_image_url(place.pic3)

    print(place.minPrice)
    print(place.maxPrice)

    return render(
        request,
        "edit.html", {
            'place': place,
            'timeOpen': str(place.timeOpen),
            'timeClose': str(place.timeClose),
            'user_id': user_id,
            'username': user_name,
            'website': "" if place.website == None else place.website,
            'vr': "" if place.vr == None else place.vr,
            'pic1': pic1_url,
            'pic2': pic2_url,
            'pic3': pic3_url,
            'minPrice': place.minPrice,
            'maxPrice': place.maxPrice
        }
    )


@login_required
def update(request, pk):
    user_id = request.user.id
    user_name = request.user.username
    place = BusinessPlace.objects.get(pk=pk)
    form = BusinessPlaceEditForm(request.POST, request.FILES, instance=place)
    pic1_url = get_image_url(place.pic1)
    pic2_url = get_image_url(place.pic2)
    pic3_url = get_image_url(place.pic3)

    if form.is_valid():
        print("FORM IS VALID")
        messages.success(request, "แก้ไขกิจการสำเร็จแล้ว.")
        form.save()
        return redirect('/test/index_business/')
    else:
        messages.error(
            request, "การแก้ไขกิจการไม่สำเร็จ กรุณาตรวจสอบข้อมูลที่ป้อนและลองใหม่อีกครั้ง.")
        return render(
            request,
            "edit.html", {
                'place': place,
                'user_id': user_id,
                'username': user_name,
                'pic1': pic1_url,
                'pic2': pic2_url,
                'pic3': pic3_url}
        )


@login_required
def delete(request, pk):
    place = BusinessPlace.objects.get(pk=pk)
    place.delete()
    messages.success(request, "ลบกิจการสำเร็จแล้ว.")
    return redirect('/test/index_business/')
