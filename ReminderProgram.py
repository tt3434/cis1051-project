#reminderprogram

import time
import datetime
current_time = time.strftime("%-I:%M %p")
print("Current Time:", current_time)
#%-I = hour, %M = min, %p = am/pm

dict={}

def validtype(reminder_type):
    valid_input=['specific','interval']
    reminder_type = reminder_type.lower()
    if valid_input.count(reminder_type) == 0:
        print("Invalid answer!")
        return False
    return True

def specifictime(text):
    timeinput=input("Enter time (hh:mm AM/PM):")
    try:
        datetime.datetime.strptime(timeinput, '%I:%M %p')
    except ValueError:
        print("Incorrect format, Enter time (hh:mm AM/PM)")
        return specifictime(text)
    #^^^ Citation: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python 
    #Uses datetime, checks if input matches format, checks and reprompts if wrong input, I used it to check for hours, mins, and AM/PM.
    dict[timeinput]=text
    td=list(dict.keys())
    #print(td)
    #print(dict)
    a=(td[0])
    b=(dict[timeinput])
    #print(a)
    #print(b)
    loop=True
    j=True
    f= True
    while loop:
        date_time = time.strftime("%-I:%M %p")
        if a == date_time:
            print("Time:", a, "Message:",b)
            loop=False
        elif j:
            while f:
                answer= str(input("Would you like to view your future reminder?"))
                if answer == 'yes':
                    print("Future Reminder:","Time:", a, "Message:",b)
                    f=False
                    j=False
                elif answer == "no":
                    f=False
                    j=False
       
def HoursMinutesSeconds(text):
    x=False
    while not x:
        reminder_interval_hms=input("Enter (hours), (minutes), or (seconds)? ")
        if reminder_interval_hms =="hours":
            reminder_hours = float(input("In how many hours? "))
            reminder_hours = (reminder_hours * 60) * 60 
            time.sleep(reminder_hours)
            print("Message:",text)
            x=True
            
        elif reminder_interval_hms =="minutes":
            reminder_minutes = float(input("In how many minutes? "))
            reminder_minutes = reminder_minutes * 60
            time.sleep(reminder_minutes)
            print("Message:",text)
            x=True

        elif reminder_interval_hms =="seconds":
            reminder_seconds = float(input("In how many seconds? "))
            reminder_seconds = reminder_seconds
            time.sleep(reminder_seconds)
            print("Message:",text)
            x=True

def remindertype(reminder_type):
    if reminder_type =='specific':
        specifictime(text) 
    elif reminder_type =='interval':
        HoursMinutesSeconds(text)
   
def userinput(validtype):
    reminder_type=str(input("Enter (specific) hh:mm or (interval) hours,minutes,seconds? "))
    while not validtype(reminder_type):
        reminder_type=str(input("Enter (specific), hh:mm or (interval), hours,minutes,seconds? "))
    else:
        remindertype(reminder_type)

text = str(input("What shall I remind you about? "))
userinput(validtype)
