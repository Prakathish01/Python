# Switch

def is_finder(day):
    match day:
        case "Sunday" | "Saturday":
            return "Weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Working day"


print(is_finder(input("Enter the day :")))
