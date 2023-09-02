# myapp/management/commands/add_data.py

from django.core.management.base import BaseCommand
from payment_app.models import Payment
from django.contrib.auth.models import User, Group
from datetime import datetime

class Command(BaseCommand):
    
    help = 'Add Payment periods to the database on mount.'

    def handle(self, *args, **options):
        payment_date = datetime.now()
        if payment_date.day == 1:
            payment_status = False
            price = 300.00
            
            group_name = 'business'
            users_in_group = User.objects.filter(groups__name=group_name)
            print(users_in_group)
            try:
                for user in users_in_group:
                    print("Add Payment to ", user.username, " on [", str(payment_date), "], price=", price)
                    p = Payment.objects.create(payment_status=payment_status, price=price, payment_date=payment_date, customer=user)
                    print("p=", p)
            except :
                print("Payment Create Failed.")    
            print("Payment Create Successfully.")
        print("Not datetime to Create payment.")
