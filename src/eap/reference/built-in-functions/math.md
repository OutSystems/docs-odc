---
locale: en-us
guid: f8d8203c-888c-4073-8e85-454190db47f7
app_type: mobile apps, reactive web apps
platform-version: odc
---
# Math

## Abs

Returns the absolute value (unsigned magnitude) of the decimal number 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to extract the absolute value from.

### Output

Type: Decimal  

### Examples

```
Abs(-10.89) = 10.89
```

## Mod

Returns the remainder of decimal division of 'n' by 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The dividend in the modulo operation.

m
:    Type: Decimal. Mandatory.  
The divisor in the modulo operation.

### Output

Type: Decimal  

### Examples

```
Mod(10, 3) = 1
Mod(4, 3.5) = 0.5
```

## Power

Returns 'n' raised to the power of 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The base value.

m
:    Type: Decimal. Mandatory.  
The exponent value.

### Output

Type: Decimal  

### Examples

```
Power(100, 2) = 10000
Power(-10.89, 2.3) = 0
Power(-10.89, -5) = -6.52920946044017E-06
```

## Round 

Returns the Decimal number 'n' rounded to a specific number of 'fractional digits'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

n
:    Type: Decimal. Mandatory.  
The Decimal number to round

fractionalDigits
:    Type: Integer.  
Use it to specify the number of fractional digits that n has to be rounded to. The default value is 0. Note: In aggregates this parameter is not specified.

### Output

Type: Decimal  

## Sqrt 

Returns the square root of the Decimal number 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to calculate the square root from.

### Output

Type: Decimal  

### Examples

```
Sqrt(2.3) = 1.51657508881031
```

## Trunc

Returns the Decimal number 'n' truncated to integer removing the decimal part of 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to truncate.

### Output

Type: Decimal  

### Examples

```
Trunc(-10.89) = -10
Trunc(7.51) = 7
```
