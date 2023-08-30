import json
from django.conf import settings
from django.shortcuts import render, redirect
from businessplace_app.api.serializers import BusinessPlaceSerializer
from test_app.forms import BusinessPlaceEditForm, BusinessPlaceForm, EmployeeForm
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

# Create your views here.

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
        # print("row=", row, "\n\n\n")
        # place
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


def index(request):
    user_id = request.user.id
    user_name = request.user.username
    places = BusinessPlace.objects.filter(place_user_id=user_id)
    return render(request, "index.html", {'places': places})


def addnew(request):
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
        website = request.POST.get('website')
        pic1 = request.POST.get('pic1')
        pic2 = request.POST.get('pic2')
        pic3 = request.POST.get('name')
        vr = request.POST.get('vr')
        place_user = request.POST.get('place_user')

        time_open = str(hour_open) + ":" + str(minute_open)
        time_close = str(hour_close) + ":" + str(minute_close)

        time_format = "%H:%M"
        timeOpen_object = datetime.strptime(time_open, time_format).time()
        timeClose_object = datetime.strptime(time_close, time_format).time()

        # instances = {
        #     "timeOpen": timeOpen_object,
        #     "timeClose": timeClose_object,
        # }
        
        place = BusinessPlace(
            name=name, 
            district=district, 
            type=BusinessType.objects.get(pk=int(type)), 
            address=address, 
            lat=lat, 
            lng=lng, 
            detail=detail, 
            timeOpen=timeOpen_object, 
            timeClose=timeClose_object,
            website=website,
            pic1=pic1,
            pic2=pic2,
            pic3=pic3,
            vr=vr,
            place_user=User.objects.get(pk=int(place_user)),
        )
        print("place,", place)

        # ลองหาวิธีเพิ่ม ข้อมูลที่ละตัวใน form
        form = BusinessPlaceForm(
            request.POST, request.FILES, instance=place
            # request.POST, request.FILES,
            )
        form.timeOpen = time_open
        form.timeClose = time_close
        # print("type,", type)
        # print("place_user,", place_user)
        # print("tiemOpen,", form.timeOpen)
        # print("tiemClose,", form.timeClose)

        if form.is_valid():
            try:
                form.save()
                return redirect('/test/')
            except Exception as e:
                print('Error saving:', e)
    else:
        form = BusinessPlaceForm()
    return render(request, "form_add.html", {'form': form, 'user_id': user_id, 'username': user_name, 'hours': hours, 'minutes': minutes})


def edit(request, pk):
    user_id = request.user.id
    user_name = request.user.username
    place = BusinessPlace.objects.get(pk=pk)
    pic1_url = get_image_url(place.pic1)
    pic2_url = get_image_url(place.pic2)
    pic3_url = get_image_url(place.pic3)
    print("pic1=", pic1_url)
    print("type.id=", place.type.id)
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


def update(request, pk):
    user_id = request.user.id
    user_name = request.user.username
    place = BusinessPlace.objects.get(pk=pk)
    form = BusinessPlaceEditForm(request.POST, request.FILES, instance=place)
    pic1_url = get_image_url(place.pic1)
    pic2_url = get_image_url(place.pic2)
    pic3_url = get_image_url(place.pic3)

    if form.is_valid():
        print("FORM IS NOT VALID")
        form.save()
        return redirect('/test/')
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


def delete(request, pk):
    place = BusinessPlace.objects.get(pk=pk)
    place.delete()
    return redirect('/test/')
