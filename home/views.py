from django.shortcuts import render,redirect
from flask import jsonify
from .models import *
import logging
from django.contrib.auth.decorators import login_required
from users.models import Profile
logger = logging.getLogger(__name__)
import boto3
import json

@login_required
def home(request):

    profile = Profile.objects.filter(user = request.user).first()
    expenses = Expense.objects.filter(user = request.user)
    
    if request.method == 'POST' and 'salary' in request.POST :
        new_salary = float(request.POST.get('salary'))
        salary = profile.income
        balance = profile.balance
        update_balance = balance + new_salary - salary

        profile.income = new_salary
        profile.balance = update_balance
        profile.save()
        return redirect('/')
        
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type') 

        expense = Expense(name=text , amount=amount , expense_type=expense_type , user= request.user)
        expense.save()
        
        if expense_type == 'Positive':
            profile.balance = profile.balance + float(amount)
        else:
            profile.expenses = profile.expenses + float(amount)
            profile.balance = profile.balance - float(amount)
            
        profile.save()
        return redirect('/')
    
    context = {'profile' : profile , 'expenses' : expenses}
    return render(request , 'home/home.html' , context)

@login_required
def bills(request):
    profile = Profile.objects.filter(user = request.user).first()
    bills = Bill.objects.filter(user = request.user)
    if request.method =='POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        note = request.POST.get('note')
        bill = Bill(name=text, amount=amount, user=request.user,note=note)
        bill.save()
        return redirect('/bills')
    bills = Bill.objects.filter(user = request.user)
    context = {'bills' : bills}
    return render(request , 'home/bills.html',context)

@login_required
def payment(request):
    profile = Profile.objects.filter(user = request.user).first()
    bills = Bill.objects.filter(user = request.user)
    if request.method =='POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        note = request.POST.get('note')
        bill = Bill(name=text, amount=amount, user=request.user,note=note)
        bill.save()
        return redirect('/bills')
    bills = Bill.objects.filter(user = request.user)
    context = {'bills' : bills}
    return render(request , 'home/payment.html',context)

@login_required
def past_expenditure(request):
    s3_client = boto3.client('s3', aws_access_key_id='AKIASU7QEJDNO5VAA4FM', aws_secret_access_key= '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')
    response = s3_client.get_object(Bucket = 'past-expenses',Key='past_expense.json')
    data = response['Body'].read().decode('utf-8')
    
    data = json.loads(data)
    print(data)
    context = {'past_expense' : data }
    
    return render(request , 'home/pastExpenditure.html',context)

@login_required
def profile(request):
    return render(request , 'home/pastExpenditure.html')
