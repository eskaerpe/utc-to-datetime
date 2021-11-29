from datetime import datetime #import the datetime module

# declare your UTC+ number
myUTC = int(7) #Change this number on this line depends your region

# time UTC+0
utcnow = datetime.utcnow()

#add the hour number from the "utcnow" variable with your UTC Time (myUTC)
myHour = int(datetime.strftime(utcnow,"%H")) + myUTC

day = datetime.strftime(utcnow, "%A")
date_num = datetime.strftime(utcnow, "%d")
month = datetime.strftime(utcnow, "%B")
year = datetime.strftime(utcnow, "%Y")
hour = datetime.strftime(utcnow, "%H")
minute = datetime.strftime(utcnow, "%M")
second = datetime.strftime(utcnow, "%S")


#Fix the issues 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if myHour > 24:
    myHour -= 24
    day_locate = days.index(day) #Find where is the "day" location on the array

    if day_locate > 6:
        day = days[0]
    else:
    	day = days[(day_locate+1)]


print(f"{myHour}:{minute}:{second}")
print(f"{day}, {date_num} {month} {year}")

