import time
times=time.localtime()
hours=times[3]
print(input("time is what?"))
time_hours=input()
while (hours<time_hours):
    times=0
    times=time.localtime()
    hours=times[3]
    int(hours)
    min=times[4]
    int(min)
    s=times[5]
    int(s)
    if s==0:
        print("now is "+str(hours),":",str(min))
        time.sleep(1)
print("now is "+str(time_hours)+":00")
