# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts from year, month, day, hour, minute, second to fractional Julian date
# Parameters:
#  year: year of interest - int
#  month: month of interest - int
#  day: day of interest - int
#  hour: hour of interest - int
#  minute: minute of interest - int
#  second: second of interest - float
#  ...
# Output:
#  A description of the script output
#
# Written by Mandar Ajgaonkar
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')

# parse script arguments
if len(sys.argv)==7:
    try:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        day = int(sys.argv[3])
        hour = int(sys.argv[4])
        minute = int(sys.argv[5])
        second = float(sys.argv[6])
    except ValueError:
      print("Error: year, month, day, hour, minute, second must be numeric.")
      exit()
else:
  print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
  exit()

# main script for calculating fractional julian date
jd = day - 32075 + 1461*(year + 4800 - (14 - month)//12)//4 + 367*(month - 2 + (14 - month)//12*12)//12 - 3*((year + 4900 - (14 - month)//12)//100)//4
jd_midnight = jd - 0.5
d_frac = (second + 60*(minute + 60*hour))/86400
jd_frac = jd_midnight + d_frac

# print results
print(jd_frac)
