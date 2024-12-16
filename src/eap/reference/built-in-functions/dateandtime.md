---
summary: OutSystems Developer Cloud (ODC) supports a variety of date and time manipulation functions for both server-side and client-side logic.
tags: date manipulation, time functions, server-side logic, client-side logic, database aggregates
locale: en-us
guid: 9f92e1f1-c921-4a83-b689-e0e554244c15
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Date and Time

## AddDays

Adds 'n' days to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add days to.

n
:    Type: Integer. Mandatory.  
The number of days to add.

### Output

Type: DateTime  

### Examples

```
AddDays(#2015-09-14#, 15) = #2015-09-29 00:00:00#
AddDays(#2015-12-31#, 1) = #2016-01-01 00:00:00#
AddDays(#2015-02-28#, 1) = #2015-03-01 00:00:00#
AddDays(#2016-02-28#, 1) = #2016-02-29 00:00:00#
```

## AddHours

Adds 'n' hours to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add hours to.

n
:    Type: Integer. Mandatory.  
The number of hours do add.

### Output

Type: DateTime  

### Examples

```
AddHours(#1982-05-21 22:20:30#, 1) = #1982-05-21 23:20:30#
AddHours(#2001-10-12 23:20:00#, 5) = #2001-10-13 04:20:00#
```

## AddMinutes

Adds 'n' minutes to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add minutes to.

n
:    Type: Integer. Mandatory.  
The number of minutes to add.

### Output

Type: DateTime  

### Examples

```
AddMinutes(#1982-05-21 22:20:30#, 1) = #1982-05-21 22:21:30#
AddMinutes(#2001-10-12 23:55:00#, 5) = #2001-10-13 00:00:00#
```

## AddMonths

Adds 'n' months to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add months to.

n
:    Type: Integer. Mandatory.  
The number of months to add.

### Output

Type: DateTime  

### Examples

```
AddMonths(#2001-09-14#, 2) = #2001-11-14 00:00:00#
AddMonths(#2001-12-14#, 2) = #2002-02-14 00:00:00#
AddMonths(#2003-01-31#, 1) = #2003-02-28#
AddMonths(#2004-01-31#, 1) = #2004-02-29#
```

## AddSeconds

Adds 'n' seconds to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add seconds to.

n
:    Type: Integer. Mandatory.  
The number of seconds to add.

### Output

Type: DateTime  

### Examples

```
AddSeconds(#2015-05-21 22:20:30#, 60) = #2015-05-21 22:21:30#
AddSeconds(#2003-10-21 23:59:50#, 11) = #2003-10-22 00:00:01#
```

## AddYears

Adds 'n' years to 'dt' and returns a valid Date Time.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to add years to.

n
:    Type: Integer. Mandatory.  
The number of years to add.

### Output

Type: DateTime  

### Examples

```
AddYears(#2001-09-14#, 3) = #2004-09-14 00:00:00#
AddYears(#2004-02-29#, 1) = #2005-02-28 00:00:00#
AddYears(#2004-02-29#, 4) = #2008-02-29 00:00:00#
```

## BuildDateTime

Returns a Date Time made up of the Date 'd' and Time 't'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

d
:    Type: Date. Mandatory.  
The Date to build the Date Time from.

t
:    Type: Time. Mandatory.  


### Output

Type: DateTime  

### Examples

```
BuildDateTime(#2015-07-14#, #12:30:34#) = #2015-07-14 12:30:34#
```

## CurrDate

* Client-side calls return the device date and time.
* Server-side calls return the current date in UTC.
* SQL query calls return the current date and time in UTC.

See [here](../../onboarding/intro.md#time) for further detail.

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Output

Type: Date  

## CurrDateTime

* Client-side calls return the device date and time. It also returns milliseconds.
* Server-side calls return the current date in UTC.
* SQL query calls return the current date and time in UTC.

See [here](../../onboarding/intro.md#time) for further detail.

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Output

Type: DateTime  

## CurrTime

* Client-side calls return the device date and time.
* Server-side calls return the current date in UTC.
* SQL query calls return the current date and time in UTC.

See [here](../../onboarding/intro.md#time) for further detail.

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Output

Type: Time  

## Day { #Day }

Returns the day of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to calculate the day from.

### Output

Type: Integer  

### Examples

```
Day(#2015-07-14#) = 14
```

## DayOfWeek

Returns the week day of 'dt', ranging from 0 (Sunday) to 6 (Saturday).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to calculate the day of the week from.

### Output

Type: Integer  

### Examples

```
DayOfWeek(#2001-09-14#) = 5
```

## DiffDays

Returns the difference in days between 'dt1' and 'dt2'; i.e. how many days have passed between these two dates:  
  
- Returns a positive number if 'dt1' is smaller than 'dt2';  
- Returns a negative number if 'dt1' is bigger than 'dt2';  
- Returns 0 if the two dates are equal.  
  
The Time component you provide in the parameters is ignored. The DiffDays function receives two Date Time parameters, and then replaces the Time component with 00:00:00. It calculates the elapsed time in milliseconds from the first date at 00:00:00 to the second date at 00:00:00, and then converts the difference in milliseconds into days.  
  
Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the UTC, regardless of the regional settings of the end-user.
  
The maximum supported value is (2^31)-1 days. This corresponds to approximately 5879489.8 years. If DiffDays(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt1
:    Type: DateTime. Mandatory.  
The first Date Time.

dt2
:    Type: DateTime. Mandatory.  
The second Date Time.

### Output

Type: Integer  

### Examples

```
DiffDays(#1982-05-19#, #1982-05-21#) = 2
DiffDays(#1982-05-21#, #1982-05-19#) = -2
DiffDays(#2005-05-11 00:00:00#, #2005-05-11 23:59:59#) = 0
DiffDays(#2004-09-01#, #2004-10-01#) = 31
DiffDays(#2004-09-01 23:00:00#, #2004-09-02 00:10:00#) = 1
DiffDays(#2004-09-01 23:00:00#, #2004-09-02 23:30:00#) = 1
DiffDays(#2014-03-30 00:00:00#, #2014-03-31 00:00:00#) = 1, assuming the GMT+1 time zone (2014 Daylight Saving Time starts in Europe on March 30 of 2014). If your server is in a different time zone, you will get different results.
DiffDays(#2014-10-25 00:00:00#, #2014-10-26 00:00:00#) = 1, assuming the GMT+1 time zone (2014 Daylight Saving Time ends in Europe on October 26 of 2014). If your server is in a different time zone, you will get different results.
```

## DiffHours

Returns the difference in hours between 'dt1' and 'dt2'; i.e. how many hours have passed between these two dates:  
  
- Returns a positive number if 'dt1' is smaller than 'dt2';  
- Returns a negative number if 'dt1' is bigger than 'dt2'.  
- Returns 0 if the two dates are equal.  
  
Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the UTC, regardless of the regional settings of the end-user.
  
The maximum supported value is (2^31)-1 hours. This corresponds to approximately 244978.74 years. If DiffHours(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt1
:    Type: DateTime. Mandatory.  
The first Date Time.

dt2
:    Type: DateTime. Mandatory.  
The second Date Time.

### Output

Type: Integer  

### Examples

```
DiffHours(#1982-05-21 22:20:30#, #1982-05-22 02:00:00#) = 4
DiffHours(#1982-05-22 02:00:00#, #1982-05-21 22:20:30#) = -4
DiffHours(#2005-05-11 10:59:00#, #2005-05-11 10:00:00#) = 0
DiffHours(#2005-05-11 10:00:00#, #2005-05-12 10:00:00#) = 24
DiffHours(#2005-05-11 10:59:00#, #2005-05-12 15:00:00#) = 29
DiffHours(#2006-03-25 15:00:00#, #2006-03-26 15:00:00#) = 24, assuming the GMT+1 time zone (2006 Daylight Saving Time starts in Europe on March 26 of 2006). If your server is in a different time zone, you will get different results.
DiffHours(#2006-10-28 15:00:00#, #2006-10-29 15:00:00#) = 24, assuming the GMT+1 time zone (2006 Daylight Saving Time ends in Europe on October 29 of 2006). If your server is in a different time zone, you will get different results.
```

## DiffMinutes

Returns the difference in minutes between 'dt1' and 'dt2'; i.e. how many minutes have passed between these two dates:  
  
- Returns a positive number if 'dt1' is smaller than 'dt2';  
- Returns a negative number if 'dt1' is bigger than 'dt2'.  
- Returns 0 if the two dates are equal.  
  
Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the UTC, regardless of the regional settings of the end-user.
  
The maximum supported value is (2^31)-1 minutes. This corresponds to approximately 4085.78 years. If DiffMinutes(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt1
:    Type: DateTime. Mandatory.  
The first Date Time.

dt2
:    Type: DateTime. Mandatory.  
The second Date Time.

### Output

Type: Integer  

### Examples

```
DiffMinutes(#1982-05-21 22:20:30#, #1982-05-21 22:26:00#) = 6
DiffMinutes(#1982-05-21 22:26:00#, #1982-05-21 22:20:30#) = -6
DiffMinutes(#1982-05-21 22:26:00#, #1982-05-21 22:26:59#) = 0
DiffMinutes(#1982-05-21 22:26:30#, #1982-05-21 22:27:20#) = 1
DiffMinutes(#1982-05-21 22:26:30#, #1982-05-21 22:27:40#) = 1
DiffMinutes(#2006-05-21 15:00:00#, #2006-05-22 15:00:00#) = 1440
DiffMinutes(#2006-03-25 15:00:00#, #2006-03-26 15:00:00#) = 1440, assuming the GMT+1 time zone (2006 Daylight Saving Time starts in Europe on March 26 of 2006). If your server is in a different time zone, you will get different results.
DiffMinutes(#2006-10-28 15:00:00#, #2006-10-29 15:00:00#) = 1440, assuming the GMT+1 time zone (2006 Daylight Saving Time ends in Europe on October 29 of 2006). If your server is in a different time zone, you will get different results.
```

## DiffSeconds

Returns the difference in seconds between 'dt1' and 'dt2'; i.e. how many seconds have passed between these two dates:  
  
- Returns a positive number if 'dt1' is smaller than 'dt2';  
- Returns a negative number if 'dt1' is bigger than 'dt2'.  
- Returns 0 if the two dates are equal.  
  
Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the UTC, regardless of the regional settings of the end-user.
  
The maximum supported value is (2^31)-1 seconds. This corresponds to approximately 68.10 years. If DiffSeconds(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt1
:    Type: DateTime. Mandatory.  
The first Date Time.

dt2
:    Type: DateTime. Mandatory.  
The second Date Time.

### Output

Type: Integer  

### Examples

```
DiffSeconds(#1982-05-21 22:20:30#, #1982-05-21 22:21:05#) = 35
DiffSeconds(#1982-05-21 22:21:05#, #1982-05-21 22:20:30#) = -35
DiffSeconds(#2006-05-21 15:00:00#, #2006-05-22 15:00:00#) = 86400
DiffSeconds(#2006-03-25 15:00:00#, #2006-03-26 15:00:00# ) = 86400, assuming the GMT+1 time zone (2006 Daylight Saving Time starts in Europe on March 26 of 2006). If your server is in a different time zone, you will get different results.
DiffSeconds(#2006-10-28 15:00:00#, #2006-10-29 15:00:00#) = 86400, assuming the GMT+1 time zone (2006 Daylight Saving Time ends in Europe on October 29 of 2006). If your server is in a different time zone, you will get different results.
```

## Hour

Returns the hour of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to extract the hours from.

### Output

Type: Integer  

### Examples

```
Hour(#1982-05-21 22:20:30#) = 22
```

## Minute

Returns the minute of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to extract the minutes from.

### Output

Type: Integer  

### Examples

```
Minute(#1982-05-21 22:20:30#) = 20
```

## Month

Returns the month of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to extract the month from.

### Output

Type: Integer  

### Examples

```
Month(#2001-09-14#) = 9
```

## NewDate { #NewDate }

Returns a Date made up of year 'y', month 'm' and day 'd'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

y
:    Type: Integer. Mandatory.  
The year of the Date.

m
:    Type: Integer. Mandatory.  
The month of the Date.

d
:    Type: Integer. Mandatory.  
The day of the Date.

### Output

Type: Date  

### Examples

```
NewDate(2002, 6, 3) = #2002-06-03#
```

## NewDateTime

Returns a Date Time made up of year 'y', month 'mo', day 'd', hour 'h', minute 'mi' and second 's'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

y
:    Type: Integer. Mandatory.  
The year of the Date Time.

mo
:    Type: Integer. Mandatory.  
The month of the Date Time.

d
:    Type: Integer. Mandatory.  
The day of the Date Time.

h
:    Type: Integer. Mandatory.  
The hours of the Date Time.

mi
:    Type: Integer. Mandatory.  
The minutes of the Date Time.

s
:    Type: Integer. Mandatory.  
The seconds of the Date Time.

### Output

Type: DateTime  

### Examples

```
NewDateTime(2002, 6, 3, 22, 0, 59) = #2002-06-03 22:00:59#
```

## NewTime

Returns a Time made up of hour 'h', minute 'm' and second 's'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

h
:    Type: Integer. Mandatory.  
The hours of the Time.

m
:    Type: Integer. Mandatory.  
The minutes of the Time.

s
:    Type: Integer. Mandatory.  
The seconds of the Time.

### Output

Type: Time  

### Examples

```
NewTime(22, 0, 59) = #22:00:59#
```

## Second { #Second }

Returns the seconds of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to extract the seconds from.

### Output

Type: Integer  

### Examples

```
Second(#2015-05-21 22:20:30#) = 30
```

## Year

Returns the year of 'dt'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The Date Time to extract the year from.

### Output

Type: Integer  

### Examples

```
Year(#2015-07-14#) = 2015
```
