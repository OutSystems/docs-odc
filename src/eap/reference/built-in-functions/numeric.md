---
summary: Learn about the Max, Min, and Sign functions in OutSystems Developer Cloud (ODC), supporting both server-side and client-side logic.
tags: math functions, logic functions, server-side scripting, client-side scripting, data manipulation
locale: en-us
guid: 53534fc8-41ba-4ee0-9be4-dff58493264c
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

# Numeric

## Max

Returns the largest number of 'n' and 'm'.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  

m
:    Type: Decimal. Mandatory.  

### Output

Type: Decimal  

### Examples

```
Max(-10.89, -2.3) = -2.3
Max(10.89, 2.3) = 10.89
```

## Min

Returns the smallest number of 'n' and 'm'.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  

m
:    Type: Decimal. Mandatory.  

### Output

Type: Decimal  

### Examples

```
Min(-10.89, -2.3) = -10.89
Min(10.89, 2.3) = 2.3
```

## Sign

Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number from which to calculate the sign value.

### Output

Type: Integer  

### Examples

```
Sign(-10.89) = -1
Sign(2.3) = 1
Sign(0.0) = 0
```
