task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder ="'" + str(task) + "' is a " + str(priority) + " priority task." 

match priority:
    case "high":
        reminder = "Reminder:", reminder
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(reminder)
        elif time_bound == "no":
            reminder += " Consider completing it when you have free time."
            print(reminder)
    case "low":
        reminder = "Note: " + reminder
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(reminder)
        elif time_bound == "no":
            reminder += " Consider completing it when you have free time." 
            print(reminder)
    case "medium":
        reminder = "Note:", reminder
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(reminder)
        elif time_bound == "no":
            reminder += " Consider completing it when you have free time." 
            print(reminder)
    case _:
            print("Non")
