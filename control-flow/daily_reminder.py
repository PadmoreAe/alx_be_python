# daily_reminder.py

print("Welcome to your Personal Daily Reminder!\n")

# Prompt user for task details
task = input("Enter your task: ").strip()

# Loop until valid priority is entered
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Loop until valid time-bound input is entered
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Process task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)

# Congratulatory message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
