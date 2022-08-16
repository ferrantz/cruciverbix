import os, sys

f = open(os.path.join(sys.path[0], "parole.txt"), "r").readlines()
print('File aperto con successo')

lunghezza_2 = []
lunghezza_3 = []
lunghezza_3 = []
lunghezza_4 = []
lunghezza_5 = []
lunghezza_6 = []
lunghezza_7 = []
lunghezza_8 = []
lunghezza_9 = []
lunghezza_10 = []
lunghezza_11 = []
lunghezza_12 = []
lunghezza_13 = []
lunghezza_14 = []
lunghezza_15 = []
lunghezza_16 = []
lunghezza_17 = []
lunghezza_18 = []
lunghezza_19 = []
lunghezza_20 = []
lunghezza_21 = []
lunghezza_22 = []
lunghezza_23 = []
lunghezza_24 = []

for w in f:
    w = w.lower()
    w = w.replace("'", "").replace("\n", "")
    if len(w) == 2:
       lunghezza_2.append(w) 
    if len(w) == 3:
       lunghezza_3.append(w)
    if len(w) == 4:
       lunghezza_4.append(w)
    if len(w) == 5:
       lunghezza_5.append(w)
    if len(w) == 6:
       lunghezza_6.append(w)
    if len(w) == 7:
       lunghezza_7.append(w)
    if len(w) == 8:
       lunghezza_8.append(w)
    if len(w) == 9:
       lunghezza_9.append(w)
    if len(w) == 10:
       lunghezza_10.append(w)
    if len(w) == 11:
       lunghezza_11.append(w)
    if len(w) == 12:
       lunghezza_12.append(w)
    if len(w) == 13:
       lunghezza_13.append(w)
    if len(w) == 14:
       lunghezza_14.append(w)
    if len(w) == 15:
       lunghezza_15.append(w)
    if len(w) == 16:
       lunghezza_16.append(w)
    if len(w) == 17:
       lunghezza_17.append(w)
    if len(w) == 18:
       lunghezza_18.append(w)
    
print('Parole appendate alle rispettive liste con successo')


with open(os.path.join(sys.path[0], "lunghezza_2.txt"), 'w') as f:
    f.write(str(lunghezza_2).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_3.txt"), 'w') as f:
    f.write(str(lunghezza_3).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_4.txt"), 'w') as f:
    f.write(str(lunghezza_4).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_5.txt"), 'w') as f:
    f.write(str(lunghezza_5).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_6.txt"), 'w') as f:
    f.write(str(lunghezza_6).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_7.txt"), 'w') as f:
    f.write(str(lunghezza_7).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_8.txt"), 'w') as f:
    f.write(str(lunghezza_8).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_9.txt"), 'w') as f:
    f.write(str(lunghezza_9).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_10.txt"), 'w') as f:
    f.write(str(lunghezza_10).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_11.txt"), 'w') as f:
    f.write(str(lunghezza_11).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_12.txt"), 'w') as f:
    f.write(str(lunghezza_12).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_13.txt"), 'w') as f:
    f.write(str(lunghezza_13).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_14.txt"), 'w') as f:
    f.write(str(lunghezza_14).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_15.txt"), 'w') as f:
    f.write(str(lunghezza_15).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_16.txt"), 'w') as f:
    f.write(str(lunghezza_16).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_17.txt"), 'w') as f:
    f.write(str(lunghezza_17).replace('[', '').replace(']', '').replace("'", ""))
with open(os.path.join(sys.path[0], "lunghezza_18.txt"), 'w') as f:
    f.write(str(lunghezza_18).replace('[', '').replace(']', '').replace("'", ""))