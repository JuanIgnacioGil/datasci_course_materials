# -*- encoding: utf-8 -*-
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
            hashtags= tweet_dict['entities']['hashtags']

            if hashtags != []:
                for hs in hashtags:
                    listaconrepeticiones.append(hs['text'].encode('utf-8'))

    
    #Creamos el diccionario que contendrá las frecuencias
    contador=Counter(listaconrepeticiones)
    frecuencias=contador.most_common()
    
    #Guardamos los resultados
    file = open('hashtags.json', 'w+')
    file.write(json.dumps(frecuencias))
    file.close

    #Imprimimos los diez primero hashtags
    for hashtag,repeticiones in frecuencias[:10]:
        print hashtag+' '+repr(repeticiones)



###################################################################################

if __name__ == '__main__':
    main()
