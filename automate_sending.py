import datetime
import pyautogui
target_date = input("Enter the target date (YYYY-MM-DD): ")
target_time = input("Enter the target time (HH:MM): ")

target_dt = str(datetime.datetime.strptime(f"{target_date} {target_time}", "%Y-%m-%d %H:%M"))
print(f"Target date and time set to: {target_dt}")

messagee = input("Whats ur message:")

while True:
    current_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if current_time == target_dt:
        print("its time")
        break
