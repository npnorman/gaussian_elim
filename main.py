### This file represents the main file to be run.
### Nicholas Norman
### August 2024
### Guass-Elim

import copy

#goal: convert a matrix to row reduced echelon form
#input: augmented matrix given by the user
#output: the same matrix in row reduced echelon form

#define a matrix object to have functions inside

class Matrix:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.data = []

    def load(self, matrix):
        #goal: load a matrix into the system
        #input: a list representing a matrix
        #output: changes matrix object

        self.data = copy.deepcopy(matrix)
    
    def display(self):
        #goal is to print a matrix in a readable format
        #input: multidimensional array
        #output: readable matrix

        for i in range(0, self.height):

            print("| ", end="")

            for j in range(0, self.width):
                print(self.data[i][j], end=" ")

            #line break
            print("|")

    def scale(self, row, scalar):
        #goal: multiply a row by a scalar value
        #input: matrix row that needs to be scaled
        #output: changed matrix

        for i in range(0, self.width):
            #multiply item by scalar value
            self.data[row][i] = self.data[row][i] * scalar

    def interchange(self, row1, row2):
        #goal: interchange 2 rows
        #input: matrix and 2 rows
        #output: changed rows

        #basic swap function
        tmpRow = self.data[row2]
        self.data[row2] = self.data[row1]
        self.data[row1] = tmpRow

    def add(self, scalar, row1, row2):
        #goal add row 1 * scalar to row2 (scalar * row1) + row2 => row2
        #input: row1 to multiply by scalar and add to row2
        #output: new row2

        #for each column
        for i in range(0, self.width):
            self.data[row2][i] = (scalar * self.data[row1][i]) + self.data[row2][i]

#starting with input:
def inputMatrix():

    matrix = []

    #goal: take an inputted matrix from the user
    #input: height, width, numbers in matrix
    #output: multidimensional list for program

    print("Row Reduce your matrix: Please input te matrix in the following way, height x width:")
    height = input("Height of desired matrix: ")
    width = input("Width of desired matrix: ")

    #validate width and height
    width = validateNumber(width, 3, 2)
    height = validateNumber(height, 3, 1)

    #take in array numbers
    for i in range(0, height):
        #for each row

        #create a row for the array
        matrix.append([])

        for j in range(0, width):
            #for each column inside of a row
            tmp = input(f"[{i}][{j}]: ")
            tmp = float(tmp)

            #add to array
            matrix[i].append(tmp)

    return matrix

def validateNumber(num, default, limit):
    #given a string, validate its a number and if not set to default
    #input: string and default number
    #output: number

    if(num.isnumeric()):
        #it is a number, convert
        num = int(num)
        if(num < limit):
            print("undefined range, defaulting to {}".format(default))
            num = default
    else:
        print("Not a valid number, defaulting to {}".format(default))
        num = default

    return num

if __name__ == "__main__":

    #input the matrix
    ##matrix = inputMatrix()
    matrix = [[1,3,7,9],[0,5,2,1],[0,0,3,7]]

    myMatrix = Matrix(3,4)
    myMatrix.load(matrix)
    
    myMatrix.display()

    #test scalar operation
    print("\nscale row 2 by 3 => 0 15 6 3")
    myMatrix.scale(1,3)
    myMatrix.display()

    #test interchange operation
    myMatrix.load(matrix) #reset matrix
    print("resetting matrix to original")
    print("\nInterchange row 1 and 3")
    myMatrix.interchange(0,2)
    myMatrix.display()

    #test add operation
    myMatrix.load(matrix) #reset matrix
    print("resetting matrix to original")
    print("\nAdding -2R1 + R2 => R2; should expect R2 = [-2 -1 -12 -17]")
    myMatrix.add(-2, 0, 1)
    myMatrix.display()