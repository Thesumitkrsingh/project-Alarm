import datetime
from playsound import playsound
hour=int(input("enter hour: "))
minute =int(input("enter minute: "))
now=datetime.datetime.now()
alarmTime=now.replace(hour=hour,minute=minute, microsecond=0)
if alarmTime.hour < 12:
    am_pm = "AM"
else:
    am_pm = "PM"

if now >= alarmTime and am_pm == "PM":
    print("Wake up! (PM)")
    playsound("oversimplified-alarm-clock-113180.mp3")
elif now >= alarmTime and am_pm == "AM":
    print("Wake up! (AM)")

    playsound("oversimplified-alarm-clock-113180.mp3")
else:
    print("Not time yet...")