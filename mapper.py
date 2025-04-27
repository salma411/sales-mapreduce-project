import sys 
from datetime import datetime

for line in sys.stdin:
    try:
        # Remove any spaces and split the line by comma
        date, product, region, amount = line.strip().split(",")

        # Skip the header
        if date == "Date":
            continue

        # Convert the date string to a day name (e.g., "Monday")
        day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")

        # Output: DayOfWeek \t Amount
        print(f"{day}\t{amount}")

    except Exception as e:
        # Ignore any line that causes an error
        continue

