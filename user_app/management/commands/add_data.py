# myapp/management/commands/add_data.py

from django.core.management.base import BaseCommand
from payment_app.models import Payment
from django.contrib.auth.models import User, Group
from datetime import datetime

class Command(BaseCommand):
    help = 'Add Payment periods to the database on mount.'

    def handle(self, *args, **options):
        
        payment_status = False
        price = 300.00
        payment_date = datetime.now()
        
        group_name = 'bussiness'
        users_in_group = User.objects.filter(groups__name=group_name)
        for user in users_in_group:
            print("Add Payment to ", user.username, " on [", str(payment_date), "], price=", price)
            Payment.objects.create(payment_status=payment_status, price=price, payment_date=payment_date, customer=user)