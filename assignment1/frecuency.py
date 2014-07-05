# -*- encoding: utf-8 -*-
from __future__ import division
import sys
import json
from collections import Counter



###############################################################################

def main():
    tweet_file = open(sys.argv[1])
    
    #Convertimos el archivo con los tweets en una estructura de python
    listaconrepeticiones=[]
    
    for tweet_json in tweet_file:
        tweet_dict=json.loads(tweet_json)
        
        if 'delete' not in tweet_dict:
            palabras= tweet_dict['text'].split()

            for palabra in palabras:
                listaconrepeticiones.append(palabra.encode('utf-8'))
                    
    
    #Número total de palabras
    total=len(listaconrepeticiones)
    
    #Creamos el diccionario que contendrá las frecuencias
    contador=Counter(listaconrepeticiones)
    frecuencias=contador.most_common()

    #Imprimimos las frecuencias
    for palabra,repeticiones in frecuencias:
        print palabra+' '+repr(repeticiones/total)





###################################################################################

if __name__ == '__main__':
    main()
