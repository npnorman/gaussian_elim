### This file represents the main file to be run.
### Nicholas Norman
### August 2024
### Guass-Elim

#goal: convert a matrix to row reduced echelon form
#input: augmented matrix given by the user
#output: the same matrix in row reduced echelon form

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
    width = validateNumber(width, 3, 1)
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

def printMatrix(mat):
    #goal is to print a matrix in a readable format
    #input: multidimensional array
    #output: readable matrix

    height = len(mat)
    width = len(mat[0])

    for i in range(0, height):

        print("| ", end="")

        for j in range(0, width):
            print(mat[i][j], end=" ")

        #line break
        print(" |")

if __name__ == "__main__":
    matrix = inputMatrix()

    printMatrix(matrix)