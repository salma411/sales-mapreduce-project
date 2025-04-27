import sys

current_day = None
current_total = 0.0

for line in sys.stdin:
    try:
        # remove any spaces and split the line by tab
        day, amount = line.strip().split("\t")
        # convert amount to float
        amount = float(amount)
        # skip the header 
        if day == "Dayofweek":
            continue
        # if the day is the same as the current day, add to the total
        if current_day == day:
            current_total += amount
        else:
            # if the current day is not None, print the current day and total
            if current_day is not None:
                print(f"{current_day}\t{current_total:.2f}")
            # set the current day to the new day and reset the total
            current_day = day
            current_total = amount
    except Exception as e:
        # ignore any line that causes an error
        continue

# print the last day and total
if current_day is not None:
    print(f"{current_day}\t{current_total:.2f}")
