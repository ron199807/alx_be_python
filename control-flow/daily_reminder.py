# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match Case (Python 3.10+) or if-elif ladder
match priority:

    case priority == "high":
        reminder = f"'{task}' is a high priority task"
        print(reminder)

    case priority == "medium":
         reminder = f"'{task}' is a medium priority task"
         print(reminder)
    case priority == "low":
        reminder = f"'{task}' is a low priority task"
        print(reminder)
    
    case _:
        reminder = f"'{task}' has an unspecified priority"
        print(reminder)

# Check time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

