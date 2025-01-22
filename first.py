import calendar

def display_calendar():
    """
    Displays the calendar for the specified month and year.
    """
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        print(calendar.month(year, month))
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")

if __name__ == "__main__":
    display_calendar()