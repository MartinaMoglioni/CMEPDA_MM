import numpy as np
import string
import time
import matplotlib.pyplot as plt
from collections import Counter

chapter_one = open('AK_LT_Chapter1.txt')
time0 = time.time()
'''
Il comando open permette di aprire il file.txt
'''

word = dict()
'''
dict() crea un dizionario con caratteri come chiavi e contatori come
valori corrispondenti.
Ora voglio che la prima volta che il programma vede un carattere, aggiunga
un elemento nel dizionario. Dopodiché aumentera il valore di un file
oggetto già esistente.
'''
for line in chapter_one:
    line = line.rstrip()
    '''
    Il metodo rstrip() restituisce una copia della stringa
    in cui tutti i caratteri sono stati rimossi dalla
    fine della stringa (caratteri di spaziatura predefiniti).
    '''
    line = line.translate(line.maketrans('', '', string.punctuation))
    '''
    Il metodo translate() + string.punctuation permette di
    rimuovere tutta la punteggiatura dal file di testo
    '''
    line = line.lower()
    '''
    Il metodo string.lower() converte tutti i caratteri maiuscoli
    in una stringa in caratteri minuscoli e li restituisce
    '''
    words = line.split()
    ''' Il metodo split() divide una stringa in un elenco in cui
    ogni parola è un elemento dell'elenco.
    '''
    for i in words:
        if i not in word:
            word[i] = 1
        else:
            word[i] += 1
    '''
    Il ciclo for attraversa la stringa. Ogni volta nel ciclo, se la parola i
    non è nel dizionario, creiamo un nuovo elemento con la chiave ed il valore
    iniziale 1 (visto che abbiamo visto questa parola una volta).
    Se è già nel dizionario incremento word[i].
    '''
time1 = time.time()
print(time1-time0, 'mele pere banane?')
#print(word)
plt.bar(list(word.keys()), word.values(), color='g')
'''
Plotta una figura a barre con le chiavi ed i conteggi
'''
plt.show()
frequency = str(word.keys())
'''
Mi creo una stringa, mo è
tutto uguale a prima ma qui prendo
solo le parole e conto le lettere
'''
time2 = time.time()
d = dict()
for c in frequency:
    c = c.rstrip()
    c = c.translate(c.maketrans('', '', string.punctuation))
    c = c.lower()
    letter = c.split()
    for j in letter:
        if j not in d:
            d[j] = 1
        else:
            d[j] = d[j] + 1
time3=time.time()
print(time3-time2, 'mele pere banane?')
print(d)
pippo=list(d.keys())
pippo = pippo.sort()
print(pippo)
plt.bar(list(d.keys()), d.values(), color='r')
plt.grid()
plt.show()
frequency = frequency.translate(frequency.maketrans('','',string.punctuation))
frequency = frequency.rstrip()
print(Counter(frequency))
'''
No Maria io esco
'''
