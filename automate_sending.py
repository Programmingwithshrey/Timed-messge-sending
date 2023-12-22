import datetime
target_date_str = input("Enter the target date (YYYY-MM-DD): ")
target_time_str = input("Enter the target time (HH:MM): ")

target_date = datetime.datetime.strptime(f"{target_date_str} {target_time_str}", "%Y-%m-%d %H:%M")
print(f"Target date and time set to: {target_date}")

while True:
    current_time = datetime.datetime.now()
    if current_time == target_time:
        print("current time now")
