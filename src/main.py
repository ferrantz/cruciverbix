import os

# numero = input('Selezionare il numero di lettere della parola: ')
numero = '10'
nome_file = 'lunghezza_' + numero + '.txt'
f = open(os.path.join(os.getcwd(), "data", nome_file), "r").read()
f = f.split(', ')

dict = {'0': 'd', '1': 'r', '2': 'o', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
lista_chiavi = [int(k) for k in dict.keys()]
lista_lettere = [v for v in dict.values()]




sostituisci = f

for i in range(int(numero)):
    if list(filter(lambda word: str(word[lista_chiavi[i]]) == lista_lettere[i], sostituisci)) == []:
        if lista_lettere[i] != '':
            sostituisci = []
        else:
            pass
    else:
        sostituisci = list(filter(lambda word: str(word[lista_chiavi[i]]) == lista_lettere[i], sostituisci))


stringa_sostituisci = str(sostituisci).replace('[', '').replace(']', '').replace("'", '')
print(stringa_sostituisci)

exit()
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[5]]) == lista_lettere[5], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[6]]) == lista_lettere[6], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[7]]) == lista_lettere[7], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[8]]) == lista_lettere[8], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[9]]) == lista_lettere[9], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[10]]) == lista_lettere[10], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[11]]) == lista_lettere[11], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[12]]) == lista_lettere[12], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[13]]) == lista_lettere[13], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[14]]) == lista_lettere[14], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[15]]) == lista_lettere[15], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[16]]) == lista_lettere[16], sostituisci))
except: 
    pass
try:
    sostituisci = list(filter(lambda word: str(word[lista_chiavi[17]]) == lista_lettere[17], sostituisci))
except: 
    pass

stringa_sostituisci = str(sostituisci).replace('[', '').replace(']', '').replace("'", '')
print(stringa_sostituisci)