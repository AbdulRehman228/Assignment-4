DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MINUTES_PER_HOUR : int = 60
SECONDS_PER_MINUTES : int = 60

def main():

   total_seconds= DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTES

   print(f"There are {total_seconds} seconds in a year")


if __name__ == '__main__':
    main()