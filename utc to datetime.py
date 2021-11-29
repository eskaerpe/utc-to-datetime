from datetime import datetime #import the datetime module

# declare your UTC+ number
myUTC = int(7) #Change this number on this line depends your region

# time UTC+0
utcnow = datetime.utcnow()

#add the hour number from the "utcnow" variable with your UTC Time (myUTC)
myHour = int(datetime.strftime(utcnow,"%H")) + myUTC

date = datetime.strftime(utcnow, "Date : %A, %d %B %Y") 
time = datetime.strftime(utcnow, f"Time : {myHour}:%y")

print(date)
print(time)
