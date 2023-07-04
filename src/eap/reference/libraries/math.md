---
summary: The OutSystems Math library provides actions to compute complex math functions, such as logarithmic expression or pseudorandom number generation.
tags: 
locale: en-us
guid: 15770ae6-e5ec-4c50-8e90-84e9c6cdcec7
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Math

The OutSystems Math library provides actions to compute complex math functions, such as logarithmic expression or pseudorandom number generation.

## Actions

### Floor
Returns the largest long value less than or equal to the decimal number 'Number'

_Inputs_

Number : mandatory; data type Decimal         

The number to extract the largest long value less than or equal to it. 

_Outputs_

Floor; data type Decimal

The largest long value less than or equal to the number given

_Examples_ 
```
Floor(7.03) = 7
```
### Ceiling
Returns the smallest long value that is greater than or equal to the decimal number 'Number'.

_Inputs_

Number : mandatory; data type Decimal         

The number to extract the smallest long value greater than or equal to it. 

_Outputs_

Ceiling; data type Decimal

The smallest long value greater than or equal to the number given.

_Examples_ 
```
Ceiling(7.03) = 8
```
### LogE
Returns the logarithm of a specified decimal number (‘Number') in log base E.

_Inputs_

Number: mandatory; data type Decimal

The positive decimal number to calculate the logarithm.

_Outputs_

Log; data type Decimal

The logarithm of the specified given number in log base E.

_Exception message:_ The input number must be positive.

### Log10
Returns the logarithm of a specified decimal number (‘Number') in log base 10.

_Inputs_

Number: mandatory; data type Decimal

The positive decimal number to calculate the logarithm.

_Outputs_

Log; data type Decimal

The logarithm of the specified given number in log base 10.

_Exception message:_ The input number must be positive.

### Log2
Returns the logarithm of a specified decimal number (‘Number') in log base 2.

Inputs:

Number: mandatory; data type Decimal

The positive decimal number to calculate the logarithm.

Outputs:

Log; data type Decimal

The logarithm of the specified given number in log base 2.

_Exception message:_ The input number must be positive.

### Random

Generates a random number using a pseudorandom number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal').

_Inputs_

MinVal: mandatory; data type Long

The minimum value (inclusive) for the range of numbers to be considered. 

MaxVal: mandatory; data type Long

The maximum value (exclusive) for the range of numbers to be considered. 

_Outputs_

RandomNumber; data type Long

The randomly generated number from the specified range.
