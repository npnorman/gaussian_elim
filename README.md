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