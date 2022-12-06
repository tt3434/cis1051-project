# cis1051-project
Reminder Program

Name: Tiffany Truong

Video URL: https://youtu.be/S9B_-wcQRtI

Project Details:
I made my project in python. User inputs the message they want for their reminder. Then they are given a choice of having a specific reminder "hh:mm am/pm" or an interval timer of "seconds, minutes, or hours" from the time they set their reminder. 

If they chose a specific reminder, they put the time they want to set the reminder in "hh:mm AM/PM" format, or else the program asks them to prompt their answer. If the current time matches up with the time the user sets, the time and message the user set earlier will pop up. If the time the user set is in the future, they are asked if they want to view their future reminder or not. If they answer yes, the future time and message they set shows up. Then, it doesn't matter if the user answered yes or no to viewing the future reminder, the actual reminder will show up at the time they set it as.

If the user chose a interval reminder they are asked if they want the reminder within seconds, minutes, or hours from present time. Then the user will input a number. The program converts whatever the user inputs is such as hours, minutes, to seconds or just seconds, then counts down and will display the user's reminder message.

Difficulties:
I wanted an additional feature for the user to delete future reminders and the user being able to set a new reminder after the old one gets deleted, but I could not figure out a method to do so, I tried "dict.clear()" and "del dict[]" but I ran into errors of the dictionary or the values not clearing when I tried to set a new reminder and gettings output values from the first reminder. I believe it's because it's something with variables or values not being cleared and I'm not sure how to find a solution for this.

Things I learned:
I figured how after looking through python time library you can use time.sleep to count down any number, and I like how it simplified things. Also, intitally I had a seperate function to validate for valid characters when the user entered in "hh:mm AM/PM", but it did not check for format. I was able to find a source that I made a citation for in my code, which used datetime and could check if a input had a certain format like mm-dd-yyyy and I was able to edit it so it would check for hh:mm AM/PM format and if the input was wrong you can just do return of the function and it reprompts the user, which was something I never realized before. For context:

def specifictime(text):
    timeinput=input("Enter time (hh:mm AM/PM):")
    try:
        datetime.datetime.strptime(timeinput, '%I:%M %p')
    except ValueError:
        print("Incorrect format, Enter time (hh:mm AM/PM)")
        return specifictime(text)
#^^^ Citation: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python 
#Uses datetime, checks if input matches format, checks and reprompts if wrong input, I used it to check for hours, mins, and AM/PM.
