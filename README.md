# cis1051-project
Reminder Program

Name: Tiffany Truong

Video URL: 

Project Details:
I made my project in python. User inputs the message they want for their reminder. Then they are given a choice of having a specific reminder "hh:mm am/pm" or an interval timer of "seconds, minutes, or hours" from the time they set their reminder. 

If they chose a specific reminder, they put the time they want to set the reminder in "hh:mm AM/PM" format, or else the program asks them to prompt their answer. If the current time matches up with the time the user sets, the time and message the user set earlier will pop up. If the time the user set is in the future, they are asked if they want to view their future reminder or not. If they answer yes, the future time and message they set shows up. Then, it doesn't matter if the user answered yes or no to viewing the future reminder, the actual reminder will show up at the time they set it as.

If the user chose a interval reminder they are asked if they want the reminder within seconds, minutes, or hours from present time. Then the user will input a number. The program converts whatever the user inputs is such as hours, minutes, to seconds or just seconds, then counts down and will display the user's reminder message.

Difficulties:
I wanted an additional feature for the user to delete future reminders and the user being able to set a new reminder after the old one gets deleted, but I could not figure out a method to do so, I tried "dict.clear()" and "del dict[]" but I ran into errors of the dictionary or the values not clearing when I tried to set a new reminder and output values from the first reminder. I believe it's because it's something with variables and I'm not sure how to find a solution for this.
