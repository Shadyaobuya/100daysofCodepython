import time,datetime

set_time=input("Set your alarm in 24 hour clock system (YYYY-M-D hh:mm:ss): ")
my_time=datetime.datetime.strptime(set_time, "%Y-%m-%d %H:%M:%S")
now=datetime.datetime.now()
#print(now)

if now<my_time:
    print("Not yet time")
elif now>my_time:
    print("You are late")
else:
    print("It's time to wake up now")









