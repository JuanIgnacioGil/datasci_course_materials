import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):

    clase = record[0]
    order_id = record[1]
    
    mr.emit_intermediate(order_id,record)



def reducer(order_id,list_of_records):
    
    #Buscamos la orden
    order=[r for r in list_of_records if r[0] == "order"]
    

    for r in list_of_records:
        if r[0] == "line_item":
            linea=order[0]+r
            mr.emit(linea)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
