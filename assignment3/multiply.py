import MapReduce
import sys

"""
    Problem 6
    Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B
    
    Map Input
    The input to the map function will be a row of a matrix represented as a list. Each list will be of the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers.
    
    The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B
    
    Reduce Output
    The output from the reduce function will also be a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.
    
    You can test your solution to this problem using matrix.json:
    
    $ python multiply.py matrix.json
    You can verify your solution by comparing your result with the file multiply.json.
    
"""

mr = MapReduce.MapReduce()



def mapper(record):
    
    """
        In the mapphase:
         for each element (i,j) of A, emit ((i,k), A[i,j]) for k in 1..N
         for each element (j,k) of B, emit ((i,k), B[j,k]) for i in 1..L
    """

    if record[0]=='a':
        for k in range(5):
            mr.emit_intermediate((record[1],k),[record[2],record[3]])
    if record[0]=='b':
        for i in range(5):
            mr.emit_intermediate((i,record[2]),[record[1],record[3]])


def reducer(key,record):
    """
    In the reduce phase, emit key = (i,k)
    value = Sumj (A[i,j] * B[j,k])
    """
    
    #Realizamos las multiplicaciones correspondientes
    valor=0

    for k in range(5):
        fila=[r[1] for r in record if r[0]==k]
        if len(fila)==2:
            valor+=fila[0]*fila[1]
               
    mr.emit((key[0],key[1],valor))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
