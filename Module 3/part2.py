# Ask the user for the current time in hours (0-23)
while True:
        current_time = int(input("What is the current time (in hours, 0-23)? "))
        if current_time >=0 and current_time < 24:
            break
        else:
            print("Please enter a valid hour between 0 and 23.")

# Ask the user for the number of hours to wait for the alarm
wait_hours = int(input("How many hours do you want to wait for the alarm? "))

# Calculate the alarm time
alarm_time = (current_time + wait_hours) % 24

# Display the result
print(f"\nThe alarm will go off at {alarm_time}:00 on a 24-hour clock.\n") 
