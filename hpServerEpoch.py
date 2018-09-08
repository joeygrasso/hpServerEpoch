"""
hpServerEpoch.py
Author: Joey Grasso | me@joeygrasso.com | github.com/joeygrasso |
A quick cli that takes a hp server serial argument and uses their documented
scheme to calculate an approximate date of manufacture. This is helpful for 
dating hardware.

Ex: 1123445555 (10 Char Serial for HP Proliant Servers)
[11]   - Country Code of Manufacture Site
[2]    - Supply Site/Vendor Code 
[3]    - Year of Manufacture
[44]   - Week Number of Manufacture
[5555] - Unique Unit Identifier
"""

from datetime import datetime
from datetime import timedelta
import argparse

def main():
    description_text = ("Convert HP Server Serial Numbers Into Estimated Date "
        "of Manufacture")
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument("--date", "-d", 
         help="output includes the estimated dates of manufacture", action="store_true")
    parser.add_argument("serial", action="store", help="HP Server Serial",
         type=str)
    args = parser.parse_args()

    # Is the input a valid Serial
    if validateInput(args.serial):
        server_epoch = calculateDateRange(args.serial[3:6])
        # If -d or --date flag is set use more verbose output
        if args.date:
            print("The server {0} estimated date of manufacture is between {1} and {2}"
                .format(
                    args.serial, 
                    server_epoch['week_start'].strftime("%B %d, %Y"), 
                    server_epoch['week_end'].strftime("%B %d, %Y"))
                 )
        else:
            print("The server {0} estimated date of manufacture is {1} {2}".format(
                    args.serial, 
                    server_epoch['week_start'].strftime("%B"), 
                    server_epoch['manufacture_year'])
                 )
    else:
        print("Please check your input and ensure it is a valid serial "
            "number.")

def validateInput(serial):
    # Valid if:
      # Serial is 10 Chars long && The 4-6 Char are numbers
    if len(serial) == 10 and serial[3:6].isdigit():
        return True
    return False

def calculateDateRange(serial_nums):
    # This assumes the server manufacture date is within the same decade.
    date_range = {}
    year_num = int(serial_nums[0])
    week_num = int(serial_nums[1:])

    # Get Friendly Year
    current_year = datetime.now().year
    current_year_last = current_year % 100 % 10
    if current_year_last < year_num:
        # Manufacture year is in the previous decade.
        friendly_year = (current_year - 10) + (year_num - current_year_last)
    else:
        # Manufacture year is in the current decade.
        friendly_year = current_year - (current_year_last - year_num)
    
    # Get Date Range for Manufacture based on week number.
    # Making an assumption that serial numbers are not 0-indexed
    if week_num != 0:
        week_num -= 1
    week_start = datetime.strptime(str(friendly_year) + " " + str(week_num) 
        + ' 0', "%Y %W %w").date()
    week_end = week_start + timedelta(days=7)
    
    date_range['manufacture_year'] = friendly_year
    date_range['week_start'] = week_start
    date_range['week_end'] = week_end

    return date_range

if __name__ == "__main__":
    main()