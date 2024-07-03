#impoting datetime module

from datetime import datetime, timedelta

# displaying the current datetime
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {formatted_date}")


# future date
def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days = number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after {number_of_days}: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

