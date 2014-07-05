import sys


###############################################################################

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Creamos un diccionario
    diccionario=crear_diccionario(sent_file)


###################################################################################

def crear_diccionario(afinnfile):
    
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


###################################################################################

if __name__ == '__main__':
    main()
