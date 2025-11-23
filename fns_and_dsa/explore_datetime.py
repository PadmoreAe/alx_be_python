from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculates and prints the date after adding the specified number of days."""
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    current_date = display_current_datetime()

    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days.")

    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
