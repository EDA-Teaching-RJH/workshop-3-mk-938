day = input("Enter day of the week")
day = day.lower()
if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print ("it's a weekday")
elif day == "saturday" or day == "sunday":
    print ("it's a weekend!")
else: 
    print ("that's not a day of the week!")