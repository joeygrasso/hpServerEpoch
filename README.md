# hpServerEpoch
Estimated date of manufacture of an HP Proliant server based on its serial number.

## Requirements
The hpServerEpoch tool requires python 3.x+. It is not compatible with legacy
python.

## Use
Assuming you are in the same directory as the script.

### Estimation with Month and Year
```
> python3 hpServerEpoch.py USE7231983
> The server USE7231983 estimated date of manufacture is June 2017
```
### Estimation with Date Range and Year
```
> python3 hpServerEpoch.py -d USE7231983
> The server USE7231983 estimated date of manufacture is between June 04, 2017 and June 11, 2017
```
## Brief Explanation of HP Proliant Server Serial Numbers
Server serial numbers are constructed using a documented scheme on HP's web
site. The 10 character HP Proliant serial number is broken into 5 parts.
1. Country of Manufacture
2. Facility or Region Identifier
3. Year of manufacture
4. Week of manufacture
5. Unique unit identifier.

Ex. USE7231983
US | E | 7 | 23 | 1092
 1   2   3   4      5

## Assumptions About the Estimation
* It is not clear that the week number in the serial is 0-indexed.
* Since the year is a single digit, the logic assumes the server was 
manufactured in the last decade.