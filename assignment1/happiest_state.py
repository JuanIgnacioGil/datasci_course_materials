# -*- encoding: utf-8 -*-
from __future__ import division
import sys
import json


###############################################################################

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    states=cargar_lista_estados()

    #Creamos un diccionario
    diccionario=crear_diccionario(sent_file)
    
    #Creamos un diccionario vacío con estados y vectores de sentimientos, número de tweets y medias
    resultados={}
    for key,value in states.iteritems():
        resultados[key]=[0,0,0]
    

    #Convertimos el archivo con los tweets en una estructura de python
    k=0
    for tweet_json in tweet_file:
        k+=1
        tweet_dict=json.loads(tweet_json)
        
        if 'delete' not in tweet_dict:
            
            #Decidimos el estado al que pertenece el tweet, si podemos
            estado=encontrar_estado(tweet_dict,states)
            
            if estado != None:
            
                words = tweet_dict['text'].split()
                words_utf8=[palabra.encode('utf-8') for palabra in words]
                
                #Para cada palabra, buscamos si está en el diccionario y calculamos el sentimiento del tweet
                sentimiento=0
                
                for palabra in words_utf8:
                    if palabra in diccionario:
                        sentimiento+=diccionario[palabra]
                
                #Actualizamos la lista de sentimientos por estado
                resultados[estado][0]+=sentimiento
                resultados[estado][1]+=1

    #Calculamos el sentimiento promedio
    for key,value in states.iteritems():
        if resultados[key][1]>0:
            resultados[key][2]=resultados[key][0]/resultados[key][1]

    #Ordenamos los estados por su sentimiento
    resultados=sorted(resultados.iteritems(), key=lambda (k,v): (v[2],k),reverse=True)

    #Guardamos los resultados
    file = open('estados.json', 'w+')
    file.write(json.dumps(resultados))
    file.close


    print resultados[0][0]



###################################################################################

def crear_diccionario(afinnfile):
    
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores

#######################################################################################

def encontrar_estado(tweet,states):
    
    estado=None

    if tweet['place'] == None:
        lugar=tweet['user']['location']
        
    else:

        if tweet['place']['country'] == 'United States':
            lugar=tweet['place']['full_name']
        else:
            lugar=None

    #Con la variable lugar intentamos asignarla a un estado
    if lugar != None:

        #Intentemos asignar estados al tweet
        for key, value in states.iteritems():
            if key in lugar or value in lugar:
                estado=key
                break

    return estado

#######################################################################################

def cargar_lista_estados():

    states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
    }

    return states



###################################################################################

if __name__ == '__main__':
    main()
