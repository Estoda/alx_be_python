
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = ""

match priority:
    case "high":
        reminder += f"'{task}' is a high priority task"
    case "medium":
        reminder += f"'{task}' is a medium priority task"
    case "low":
        reminder += f"'{task}' is a low priority task"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder: " + reminder)

# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ")
# time_bound = input("Is it time-bound? (yes/no): ")

# match priority:
#     case "high":
#         reminder = f"Reminder: '{task}' is a high priority task"
#     case _:
#         reminder = f"Note: '{task}' is a {priority} task"
# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# else:
#     reminder += ". Consider completing it when you have free time."

# print(reminder)

