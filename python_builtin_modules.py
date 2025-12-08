# #math module provides access to the mathematical functions
# import math as m
# # print(m.ceil(2.0))  #ceil() function to round off value to next higher integer
# # print(m.ceil(2.3))
# # print(m.ceil(2.1))
# # #sqrt() function  #to get square root of a number
# # print(m.sqrt(81))
# # print(m.sqrt(64))

# # #pow() function  #to get power of a number
# # print(m.pow(2,5))
# # #print(m.pow(2,4,6)) #in math module pow() accepts only 2 params
# # print(pow(2,4,6))  #in built-in pow() , 3 params allowed (a^b) %c , c--is optional

# #fabs() function to get absolute value(output in + ve only)
# # print(m.fabs(4.670))
# # print(m.fabs(1.456000))
# # print(m.fabs(-8.9450))
# # print(m.fabs(-0.4567))

# # #degrees() and radians() functions
# # print(m.degrees(90))  #Convert angle x from radians to degrees. 1 radian ≈ 57.2958°
# # print(m.radians(90))  #Convert angle x from degrees to radians.

# print(m.factorial(6))
# print(m.factorial(10))
# print(m.factorial(0))
# print(m.factorial(1))
# print(m.factorial(2))
# #print(m.factorial(1.2))  #math.factorial() only works for non-negative integers.

# import math
# print(math.gamma(1.2 + 1)) #to get factorial for decimal values

# #to execute code without error
# try:
#     print(m.factorial(1.2))  #math.factorial() only works for non-negative integers.
# except:
#     print("value is not an integer")

# print(m.factorial(-4)) #Only non-negative integers (0, 1, 2, 3, …) are allowed.












# #datetime module to work with date and time
#Use date when you only care about the calendar date.
#Use datetime when you also need the time of day.
#import datetime
# today_is= datetime.date.today() #to get today's date
# print("today's date is:",today_is)
# print("current year is:",today_is.year)
# print("current month is:",today_is.month)
# print("current day is :",today_is.day)
# print("weekday is:",today_is.weekday())  #Monday is 0 and Sunday is 6
# print("ISO weekday is:",today_is.isoweekday())  #Monday is 1 and Sunday is 7
# print(datetime.date.today().year)  #datetime.date() requires three arguments, not one.
# mydate=datetime.date(2025,12,25) #custom date
# print(mydate.day)

#timedelta function to denstrate difference between two dates
# from datetime import timedelta
# today_now=datetime.date.today()
# #same_date_nextyear=datetime.date.timedelta(today_now,datetime.date(today_now.year+1,today_now.month,today_now.day))
# same_date_nextyear=today_now + timedelta(days=365)
# print("same date next year:",same_date_nextyear)
 
#to get next year same date using replace() function
# from datetime import date

# today = date.today()
# try:
#     next_year_same_date = today.replace(year=today.year + 1)
# except ValueError:
#     # Handles Feb 29 -> Feb 28
#     next_year_same_date = today.replace(month=2, day=28, year=today.year + 1)

# print(next_year_same_date)

# print(datetime.datetime.now())

"""#we can add or subtract days,hours,minutes(date,time) using timedelta,date functions. 
 but for months and years we have to use replace() function. 
 or use external libraries like dateutil.relativedelta because of different days in months(28,30,31) and leap years."""

#from datetime import date
# from dateutil.relativedelta import relativedelta
# today=date.today()
# next_months=today+relativedelta(months=1)
# last_month= today-relativedelta(months=1)
# next_year=today+relativedelta(years=1)
# last_years=today-relativedelta(years=2)
# print(today)
# print(next_months)
# print(last_month)
# print(next_year)
# print(last_years)

#difference between 2 different dates
# date1=date(1998,4,23)
# date2=date(2007,12,26)
# difference=date2-date1
# print(difference.days)

# print(3534/365)

# from datetime import date,timedelta
# today=date.today()
# birthday=date(1998,4,23)
# age=today.year-birthday.year
# if (today.month,today.day)<(birthday.month,birthday.day):
#     age=-1
# print("age is:",age)

#subscription renewal (it means add days)
# from datetime import date,timedelta
# from dateutil.relativedelta import relativedelta
# subscription_start=date(2024,8,15)
# subscription_end=subscription_start+relativedelta(years=3)
# print('subscription_end date is:',subscription_end)

# from datetime import date,timedelta
# manufacture_date=date(2025,8,20)
# validity_days=180
# expirydate=manufacture_date+timedelta(validity_days)
# print(expirydate)
# #check if expired or not
# today=date.day()
# if today>expirydate:
#     print("product expired")
# else:
#     print("product is valid")

# from datetime import date
# from dateutil.relativedelta import relativedelta

# billing_date = date(2025, 1, 1)
# next_billing = billing_date + relativedelta(months=1)

# print("Next Billing Date:", next_billing)

#warranty tracking calculation on electronics or other products
#from datetime import date,timedelta,datetime
# from dateutil.relativedelta import relativedelta
# purchase_on= date(2024,12,24)
# valid_days=730
# expire_on=purchase_on+timedelta(days=valid_days)
# print("warranty expires on:",expire_on)
# warranty_period= purchase_on+relativedelta(years=2)
# print("warranty valid till:",warranty_period)

# #date formatting using strftime() function
# dt = datetime.now()
# print(dt.strftime("%A, %B %d, %Y"))
# print(dt.strftime("%B %d, %Y"))
# print(dt.strftime("%d %B, %Y"))
# print(dt.strftime("%A, %d, %B, %Y"))
# print(dt.strftime("%m/%d/%Y")) #american style(month/day/year)
# print(dt.strftime("%d-%m-%Y")) #european style(day/month/year)
# print(dt.strftime("%B %d, %Y, %I:%M %p"))


# #pattern printing using spaces
# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
# for i in range(n-1,0,-1):
#     print(' '*(n-i)+'*'*i)

#attendance tracking or login times tracking
# from datetime import datetime
# login_time=datetime(2025,11,9,9,0)
# office_start=datetime(2025,11,28,9,30)
# if login_time>office_start:
#     delay=login_time-office_start
#     print("you are late by:",delay)
# else:
#     print("you are on time")

#EMI scheduling
# from datetime import date
# from dateutil.relativedelta import relativedelta

# emi_start = date(2025, 1, 10)
# for i in range(12):
#     print("EMI", i+1, ":", emi_start + relativedelta(months=i))

#parking billing calculation based on hours parked
# from datetime import datetime,timedelta,date
# from dateutil.relativedelta import relativedelta
# entry_time=datetime(2025,11,28,10,30)
# exit_time=datetime.now()
# total_time= exit_time-entry_time
# total_hours=total_time.total_seconds()/3600
# print("total hours parked:",total_hours)
# rate_per_hour=20
# if total_hours<1:
#     total_hours=1
# bill=total_hours*rate_per_hour
# print("total parking bill is:",bill)
#timezones handling with module pytz(external module need to install separately)

#Email library to send email reminders
# import smtplib
# import smtplib
# from datetime import datetime,date

# # ----- User email settings -----
# SENDER_EMAIL = "rayapatisuresh18@gmail.com"
# #APP_PASSWORD = "bavemobqhptsklvw"  # 16-character Gmail app password
# receiver = "muniraja.3275@gmail.com"

# # ----- Reminder list -----
# reminders = [
#     {"task": "Pay electricity bill", "date": "2025-11-29"},
#     {"task": "Pay electricity bill", "date": "2025-11-29"},
#     {"task": "Submit project report", "date": "2025-11-29"},
#     {"task": "Insurance renewal", "date": "2025-11-29"},
# ]

# # ----- Get today's date -----
# today = datetime.now().strftime("%Y-%m-%d")

# # ----- Check each reminder -----
# for r in reminders:
#     if r["date"] == today:
#         message = f"""Subject: Reminder - {r['task']}

# Hello,

# This is your automated reminder for the task: {r['task']}

# Date: {r['date']}

# Regards,
# Your Reminder Bot
# """

#         # ----- Send Email -----
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(SENDER_EMAIL, APP_PASSWORD)
#         server.sendmail(SENDER_EMAIL, receiver, message)
#         server.quit()

#         print(f"Reminder sent for: {r['task']}")

# receiver = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
# server.sendmail(SENDER_EMAIL, receiver, message)

# from datetime import date,datetime,timedelta
# today=date.today()
# #strftime() date to string. string format time
# today_date_str=today.strftime("%d %m,%Y") #when converting date to string , give date along with format that how you want
# today_date_str1=today.strftime("%d-%m-%Y")
# print(today)
# print(f"date to string format :{today_date_str}")

# #strptime() string parse time. to convert string to date , we have to give the format in which the string date is present
# randomstring_to_date=datetime.strptime(today_date_str,"%d %m,%Y") 
# print(f"string to date converted:{randomstring_to_date}")

# #dictionary update() method to merge two dictionaries
# d1={1:'a',2:'b'}
# d2={2:'c',4:'d'}
# d1.update(d2)
# print(d1)

#os module to work with operating system
import os
#print(dir(os))
os.getcwd()  #to get current working directory
print("current working directory is:",os.getcwd())
#os.mkdir('c:/october_14/python_test_folder')  #to create new directory
#os.makedirs('c:/october_14/python_test_folder/subfolder1/subfolder2')  #to create multiple directories
#print(os.listdir('c:/october_14'))  #to list all files and folders in a directory
print(os.listdir('c:/october_14/python_test_folder/subfolder1'))  #to list all files and folders in a directory
# #os.chdir("C:/")  #to change current working directory
