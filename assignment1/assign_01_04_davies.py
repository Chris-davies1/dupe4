#Christian Davies
#CBIS 4210
#Assignment 01-03 - Clock-in Time Management System

#import date and time functions
from datetime import datetime, timedelta

#check the clock-in time
def check_clock_in_time(clock_in_time):
    standard_time = datetime.strptime("08:00", "%H:%M")
    time_difference = clock_in_time - standard_time

#provide feedback based on the time input
    if time_difference <= timedelta(minutes=0):
        print("You are on time. Great job!")
    elif time_difference <= timedelta(minutes=5):
        print("Cutting it close today, you can do better tomorrow.")
    elif time_difference <= timedelta(minutes=10):
        print("Your late arrival has resulted in a demerit.")
    elif time_difference <= timedelta(minutes=30):
        print("Please go see HR at the end of the day.")
    else:
        print("Significantly late. Immediate action may be required.")

#get the clock-in time from the user
def get_clock_in_time():
    while True:
        try:
            time_str = input("Enter clock-in time (HH:MM): ")
            clock_in_time = datetime.strptime(time_str, "%H:%M")
            return clock_in_time
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format.")

#main function to run the clock-in mangement program
def main():
    print("Employee Clock-In Tracking System")
    while True:
        clock_in_time = get_clock_in_time()
        check_clock_in_time(clock_in_time)

#ask the user if they want to enter another clock-in time
        continue_choice = input("Do you want to enter another clock-in time? (yes/no): ").lower()
        if continue_choice != 'yes':
#exit the system after no is entered
            print("Exiting the system. Have a great day!")
            break


if __name__ == "__main__":
    main()
