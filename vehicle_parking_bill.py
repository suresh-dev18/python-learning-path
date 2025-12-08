# # Vehicle Parking Bill Generator

# import datetime

# class ParkingLot:
#     def __init__(self):
#         # Hourly rates for different vehicle types
#         self.rates = {
#             "car": 50,       # ₹50 per hour
#             "bike": 20,      # ₹20 per hour
#             "truck": 100     # ₹100 per hour
#         }
#         self.records = {}

#     def park_vehicle(self, vehicle_number, vehicle_type):
#         if vehicle_type not in self.rates:
#             print("Invalid vehicle type. Choose car, bike, or truck.")
#             return
#         entry_time = datetime.datetime.now()
#         self.records[vehicle_number] = {
#             "type": vehicle_type,
#             "entry": entry_time
#         }
#         print(f"Vehicle {vehicle_number} parked at {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")

#     def exit_vehicle(self, vehicle_number):
#         if vehicle_number not in self.records:
#             print("Vehicle not found in records.")
#             return
#         exit_time = datetime.datetime.now()
#         entry_time = self.records[vehicle_number]["entry"]
#         vehicle_type = self.records[vehicle_number]["type"]

#         # Calculate duration in hours
#         duration = (exit_time - entry_time).total_seconds() / 3600
#         duration_hours = max(1, int(duration))  # round up to at least 1 hour

#         # Calculate bill
#         rate = self.rates[vehicle_type]
#         bill_amount = duration_hours * rate

#         print("\n--- Parking Bill ---")
#         print(f"Vehicle Number : {vehicle_number}")
#         print(f"Vehicle Type   : {vehicle_type}")
#         print(f"Entry Time     : {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
#         print(f"Exit Time      : {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
#         print(f"Duration       : {duration_hours} hour(s)")
#         print(f"Rate per Hour  : ₹{rate}")
#         print(f"Total Bill     : ₹{bill_amount}")
#         print("--------------------\n")

#         # Remove record after billing
#         del self.records[vehicle_number]


# # Example usage
# # if __name__ == "__main__":
# #     lot = ParkingLot()
# #     lot.park_vehicle("KA01AB1234", "car")
# #     input("Press Enter when vehicle exits...")  # simulate waiting
# #     lot.exit_vehicle("KA01AB1234")





# #vehicle parking billing calculation based on hours parked
# from datetime import datetime, timedelta

# def calculate_parking_bill(entry_time, exit_time, rate_per_hour=20):
#     duration = exit_time - entry_time
#     hours = duration.total_seconds() / 3600
#     bill = round(hours * rate_per_hour, 2)
#     return duration, bill

# print("=== PARKING BILLING SYSTEM ===")

# vehicle = input("Enter Vehicle Number: ")

# entry_str = input("Enter Entry Time (YYYY-MM-DD HH:MM): ")
# exit_str = input("Enter Exit Time  (YYYY-MM-DD HH:MM): ")

# try:
#     entry_time = datetime.strptime(entry_str, "%Y-%m-%d %H:%M")
#     exit_time = datetime.strptime(exit_str, "%Y-%m-%d %H:%M")

#     if exit_time < entry_time:
#         print("Error: Exit time cannot be earlier than Entry time!")
#         exit()

#     duration, bill = calculate_parking_bill(entry_time, exit_time)

#     print("\n--- BILL SUMMARY ---")
#     print("Vehicle Number :", vehicle)
#     print("Entry Time     :", entry_time)
#     print("Exit Time      :", exit_time)
#     print("Duration       :", duration)
#     print("Total Bill     : ₹", bill)

#     # Save in file
#     with open("parking_log.txt", "a") as f:
#         f.write(f"{vehicle} | {entry_time} | {exit_time} | {duration} | ₹{bill}\n")

#     print("\nBill generated and saved in parking_log.txt")

# except ValueError:
#     print("Invalid date format! Please use YYYY-MM-DD HH:MM")


# from datetime import date, timedelta
# import smtplib

# due_date = date(2025,12,2)
# reminder_date = due_date - timedelta(days=3)

# today = date.today()

# if today == reminder_date:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("rayapatisuresh18@gmail.com", "19980423vK@1")

#     msg = f"Subject: Payment Reminder\n\nYour due date is on {due_date}."
#     server.sendmail("rayapatisuresh18@gmail.com", "muniraja.3275@gmail.com", msg)

#     print("Reminder email sent!")
# else:
#     print("No reminder needed today.")


import smtplib
from datetime import datetime,date

# ----- User email settings -----
SENDER_EMAIL = "rayapatisuresh18@gmail.com"
APP_PASSWORD = "bavemobqhptsklvw"  # 16-character Gmail app password
receiver = "muniraja.3275@gmail.com"

# ----- Reminder list -----
reminders = [
    {"task": "Pay electricity bill", "date": "2025-11-29"},
    {"task": "Pay electricity bill", "date": "2025-11-29"},
    {"task": "Submit project report", "date": "2025-11-29"},
    {"task": "Insurance renewal", "date": "2025-11-29"},
]

# ----- Get today's date -----
today = datetime.now().strftime("%Y-%m-%d")

# ----- Check each reminder -----
for r in reminders:
    if r["date"] == today:
        message = f"""Subject: Reminder - {r['task']}

Hello,

This is your automated reminder for the task: {r['task']}

Date: {r['date']}

Regards,
Your Reminder Bot
"""

        # ----- Send Email -----
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver, message)
        server.quit()

        print(f"Reminder sent for: {r['task']}")

# receiver = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
# server.sendmail(SENDER_EMAIL, receiver, message)
