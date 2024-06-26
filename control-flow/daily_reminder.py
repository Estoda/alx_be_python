task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder ="'" +  str(task) + "' is a " + str(priority) + " priority task" 

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print("Reminder:", reminder)
        elif time_bound == "no":
            reminder += ". Consider completing it when you have free time."
            print("Reminder:", reminder)
    case "low":
        reminder = "Note:" + reminder
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print("Note:", reminder)
        elif time_bound == "no":
            reminder += ". Consider completing it when you have free time." 
            print("Note:", reminder)
    case "medium":
        reminder = "Note: " + reminder
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print("Note:", reminder)
        elif time_bound == "no":
            reminder += ". Consider completing it when you have free time." 
            print("Note:", reminder)

