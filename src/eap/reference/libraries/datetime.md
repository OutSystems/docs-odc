---
summary: The OutSystems DateTime library provides actions to access and manipulate DateTime objects, such as retrieving the quarter of a specific date or determining if a date is set on a leap year.
tags: 
locale: en-us
guid: 9da728fe-ebdc-4114-af34-1ef4d2265e19
app_type: mobile apps, reactive web apps
---

# DateTime

The OutSystems DateTime library provides actions to access and manipulate DateTime objects, such as retrieving the quarter of a specific date or determining if a date is set on a leap year.

## Actions

### DiffMonths

Returns the difference in months between 'Datetime1' and ‘Datetime2'; i.e. the number of months between the two dates.

* Returns a positive number if ‘Datetime1' is less than ‘Datetime2';
* Returns a negative number if ‘Datetime1' is greater than ‘Datetime2'.
* Returns 0 if the two months are equal.

_Inputs_    

Datetime1 : mandatory; data type Date Time         

The first datetime.    

 Datetime2 : mandatory; data type Date Time         

The second datetime.

_Outputs_

DiffMonths; data type Integer

The difference in months between 'Datetime1' and ‘Datetime2'.

_Examples_
```
DiffMonths(#2022-08-31#, #2022-09-01) = 1
DiffMonths(#2022-08-10#, #2022-07-20) = -1
DiffMonths(#2022-08-20#, #2022-08-10) = 0
```
### DiffQuarters

Returns the difference in quarters between ‘Datetime1' and 'Datetime2'; i.e. the number of quarters between the two dates.

* Returns a positive number if ‘Datetime1' is less than ‘Datetime2';
* Returns a negative number if ‘Datetime1' is greater than ‘Datetime2'.
* Returns 0 if the two quarters are equal.

_Inputs_     

Datetime1 : mandatory; data type Date Time         

The first datetime.    

 Datetime2 : mandatory; data type Date Time         

The second datetime.

_Outputs_

DiffQuarters; data type Integer

The difference in quarters between 'Datetime1' and ‘Datetime2'.

_Examples_
```
DiffQuarters(#2022-09-30#, #2022-10-01) = 1
DiffQuarters(#2022-01-01#, #2022-02-01) = 0
DiffQuarters(#2022-04-01#, #2022-03-28) = -1
```

### DiffWeeks

Returns the difference in weeks between ‘Datetime1' and ‘Datetime2'; i.e. the number of weeks between the two dates.

* Returns a positive number if ‘Datetime1' is less than ‘Datetime2';
* Returns a negative number if ‘Datetime1' is greater than ‘Datetime2'.
* Returns 0 if the two weeks are equal (the difference between the dates is less than 7 days).

_Inputs_     

Datetime1 : mandatory; data type Date Time         

The first datetime.    

 Datetime2 : mandatory; data type Date Time         

The second datetime.

_Outputs_

DiffWeeks; data type Integer

The difference in weeks between 'Datetime1' and ‘Datetime2'.

_Examples_
```
DiffWeeks(#2022-08-18#, #2022-08-22) = 0
DiffWeeks(#2022-08-18#, #2022-08-25) = 1
DiffWeeks(#2022-08-18#, #2022-08-10) = -1
```

### DiffYears

Returns the difference in years between ‘Datetime1' and ‘Datetime2'; i.e. the number of years between the two dates.

* Returns a positive number if ‘Datetime1' is less than ‘Datetime2';
* Returns a negative number if ‘Datetime1' is greater than ‘Datetime2'.
* Returns 0 if the two years are equal.

_Inputs_     

Datetime1 : mandatory; data type Date Time         

The first datetime.    

 Datetime2 : mandatory; data type Date Time         

The second datetime.

_Outputs_

DiffYears; data type Integer

The difference in years between 'Datetime1' and ‘Datetime2'.

_Examples_
```
DiffYears(#2022-12-31#, #2023-01-01) = 1
DiffYears(#2022-08-18#, #2022-08-25) = 0
DiffYears(#2022-01-01#, #2021-12-31) = -1
```

### GetTicks 

Returns the number of ticks of 'Datetime’. A single tick represents 100 nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond.

_Inputs_     

Datetime : optional; data type Date Time         

The datetime to calculate the ticks from. If no value is given, the current datetime (in UTC) is used.

_Outputs_

Ticks; data type Long Integer

The number of ticks of the given datetime.

### Quarter

Returns the quarter of ‘Datetime’. 

_Inputs_     

Datetime : mandatory; data type Date Time         

The datetime to calculate the quarter from.

_Outputs_

Quarter; data type Integer

The quarter (1-4) of the given datetime.

_Examples_
```
Quarter(#2022-01-01#) = 1
```

### IsLeapYear 

Returns true if the year of ‘Datetime’ is a leap year.

The year is interpreted as a year in the Gregorian calendar.

_Inputs_

Datetime : mandatory; data type Date Time         

The datetime to determine whether it is in a leap year.

_Outputs_

IsLeapYear; data type Boolean

True if the year of the given datetime is a leap year.
