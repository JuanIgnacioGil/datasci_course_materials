# -*- encoding: utf-8 -*-
import sys
import json


###############################################################################

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Creamos un diccionario
    diccionario=crear_diccionario(sent_file)

    #Convertimos el archivo con los tweets en una estructura de python
    k=0
    for tweet_json in tweet_file:
        k+=1
        tweet_dict=json.loads(tweet_json)
        
        if 'delete' not in tweet_dict:
            words = tweet_dict['text'].split()
            words_utf8=[palabra.encode('utf-8') for palabra in words]
            
            #Para cada palabra, buscamos si está en el diccionario y calculamos el sentimiento del tweet
            sentimiento=0
            
            for palabra in words_utf8:
                if palabra in diccionario:
                    sentimiento+=diccionario[palabra]

            print sentimiento


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
