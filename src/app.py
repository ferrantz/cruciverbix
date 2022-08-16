# streamlit run src/app.py     

import streamlit as st
import os 
import streamlit.components.v1 as components

code = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6470640016513895"
     crossorigin="anonymous"></script>
<!-- Test -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6470640016513895"
     data-ad-slot="6078343400"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>'''


components.html( # iframe
    code
)


st.title('Cruciverbix')
st.write('Tool per trovare la parola che ti manca al cruciverba') # aggiungi sorriso
st.number_input("Selezionare il numero di lettere della parola: ", min_value = 2, max_value = 18, key = "numero")
nome_file = 'lunghezza_' + str(st.session_state.numero) + '.txt'
f = open(os.path.join(os.getcwd(), "data", nome_file), "r").read()
f = f.split(', ')

nomi_dizionari = ['dict_' + str(valore) for valore in range(st.session_state.numero)]

for casella in range(st.session_state.numero):
    printa = st.text_input("Casella " + str(casella + 1), key = str(casella), max_chars = 1)
    nomi_dizionari[casella] = {casella: printa.lower()}

dict = {}
for numero_di_dizionari in range(len(nomi_dizionari)):
    dict.update(nomi_dizionari[numero_di_dizionari])
lista_chiavi = [int(k) for k in dict.keys()]
lista_lettere = [v for v in dict.values()]
sostituisci = f

if st.button('Premere pulsante per ricerca'):
    for i in range(int(st.session_state.numero)):
        if list(filter(lambda word: str(word[lista_chiavi[i]]) == lista_lettere[i], sostituisci)) == []:
            if lista_lettere[i] != '':
                sostituisci = []
            else:
                pass
        else:
            sostituisci = list(filter(lambda word: str(word[lista_chiavi[i]]) == lista_lettere[i], sostituisci))
    stringa_sostituisci = str(sostituisci).replace('[', '').replace(']', '').replace("'", '')
    st.title(stringa_sostituisci)
    if len(sostituisci) == 1:
        st.title('Hai trovato la parola che cercavi!')
        st.balloons()
    if len(sostituisci) == 0:
        st.title('Non riesco a trovare la parola')
else:
    pass