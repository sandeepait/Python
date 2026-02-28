from unittest import case


def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Unknown"

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return "Weekend"
        case "Monday" | "Tuesday" | "Wednesday"| "Thursday" | "Friday":
            return "Not a weekend"
        case _:
            return "Unknown"

print(day_of_week(7))
print(day_of_week(1))
print(day_of_week(9))
print(is_weekend("Saturday"))
print(is_weekend("Friday"))
print(is_weekend("Sunday"))
print(is_weekend("Pizza"))