import datetime
import calendar
today = datetime.datetime.now()
print("Current Date is: ")
print(today.strftime("%Y-%m-%d %H:%M:%S")) 
yy = 2022
mm = 4
print(calendar.month(yy,mm))