# gaussian_elim

## Nicholas Norman, August 2024

As of August 2024, I am currently enrolled in a linear alegbra course. We are practicing with augmented matrices and putting them in row reduced echelon form. So, as practice into the perview of linear alebra and computer science, I have tasked myself with doing my best to write a program that takes a matrix and row reduces it.

### Goal

The goal is to row reduce a matrix

### Input

The input is given by the user (or potentially a file). It will be an augmented matrix, representing a set of linear equations.

### Output

The output is the matrix in row reduced echelon form, defined by the folowing criteria:

* (a) Every pivot point must be a 1
* (b) All pivot points must descend
* (c) Every number above and below a pivot point must be a 0

### Steps

Here is an example augmented matrix, defined as 3 x 4, 3 variables and 3 equations

3x<sub>1</sub> + 5x<sub>2</sub> + 1x<sub>3</sub> = 4<br>
0x<sub>1</sub> + 2x<sub>2</sub> + 4x<sub>3</sub> = 5<br>
0x<sub>1</sub> + 0x<sub>2</sub> + 7x<sub>3</sub> = 2
```
[3 5 1 | 4]
[0 2 4 | 5]
[0 0 7 | 2]
```

#### Functions:

* Input the matrix (take it in from the user and represent it using a 2D list in python)
* Define elementary row operations:
    * Scale: multiply a row by a scalar value
    * Interchange: swap two rows
    * Add: Add a multiple of a row to another row
* isConsistent, checks if the system is consistent by looking for inconsistent rows ex. `[0 0 0 | 1]` 0x<sub>1</sub> + 0x<sub>2</sub> + 0x<sub>3</sub> = 1, (0 != 1)
* RowReduce, using the elementary operations, checks for consistency and reduced the matrix
* findPivot: finds the index of the pivot point of a row
* sort: sorts by depth of pivot point and row index
* descend: sort rows using interchange in descending order

#### Examples

Scale ex.

2R<sub>2</sub> => R<sub>2</sub>
```
[3 5 1 | 4 ]
[0 4 8 | 10]
[0 0 7 | 2 ]
```
Interchange ex.

R<sub>1</sub> <=> R<sub>3</sub>
```
[0 0 7 | 2]
[0 2 4 | 5]
[3 5 1 | 4]
```
Add ex.

-2R<sub>1</sub> + R<sub>2</sub> => R<sub>2</sub>
```
[3  5  1 |  4]
[0 -8 -2 | -3]
[0  0  7 |  2]
```

### Tracking operations

When performing a row reduction, the operations performed can be given as a list to the user. The log does not automatically clear and must be cleared automatically.

`matrix.log()` Returns a list. `matrix.clearLog()` clears the log after use.