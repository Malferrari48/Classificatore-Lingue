import string
import logging

fila = 0
f = 0
totale = 0
frequenza = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
             'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,
             'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
dizionario = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
              'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
italiano = {'A': 11.745, 'B': 0.927, 'C': 4.501, 'D': 3.736, 'E': 11.792, 'F': 1.153, 'G': 1.644, 'H': 0.636,
            'I': 10.143, 'J': 0.011, 'K': 0.009, 'L': 6.510, 'M': 2.512, 'N': 6.883, 'O': 9.832, 'P': 3.056, 'Q': 0.505,
            'R': 6.367, 'S': 4.981, 'T': 5.623, 'U': 3.011, 'V': 2.097, 'W': 0.033, 'X': 0.003, 'Y': 0.020, 'Z': 1.181}
tedesco = {'A': 6.516, 'B': 1.886, 'C': 2.732, 'D': 5.076, 'E': 16.396, 'F': 1.656, 'G': 3.009, 'H': 4.577, 'I': 6.550,
           'J': 0.268, 'K': 1.417, 'L': 3.437, 'M': 2.534, 'N': 9.776, 'O': 2.594, 'P': 0.670, 'Q': 0.018, 'R': 7.003,
           'S': 7.270, 'T': 6.154, 'U': 4.166, 'V': 0.846, 'W': 1.921, 'X': 0.034, 'Y': 0.039, 'Z': 1.134}
spagnolo = {'A': 11.525, 'B': 2.215, 'C': 4.019, 'D': 5.010, 'E': 12.181, 'F': 0.692, 'G': 1.768, 'H': 0.703,
            'I': 6.247, 'J': 0.493, 'K': 0.011, 'L': 4.967, 'M': 3.157, 'N': 6.712, 'O': 8.683, 'P': 2.510, 'Q': 0.877,
            'R': 6.871, 'S': 7.977, 'T': 4.632, 'U': 2.927, 'V': 1.138, 'W': 0.017, 'X': 0.215, 'Y': 1.008, 'Z': 0.467}
francese = {'A': 7.636, 'B': 0.901, 'C': 3.260, 'D': 3.669, 'E': 14.715, 'F': 1.066, 'G': 0.866, 'H': 0.737, 'I': 7.529,
            'J': 0.613, 'K': 0.049, 'L': 5.456, 'M': 2.968, 'N': 7.095, 'O': 5.796, 'P': 2.521, 'Q': 1.362, 'R': 6.693,
            'S': 7.948, 'T': 7.244, 'U': 6.311, 'V': 1.838, 'W': 0.074, 'X': 0.427, 'Y': 0.128, 'Z': 0.326}
inglese = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966,
           'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
           'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}
portoghese = {'A': 14.634, 'B': 1.043, 'C': 3.882, 'D': 4.992, 'E': 12.570, 'F': 1.023, 'G': 1.303, 'H': 0.781,
              'I': 6.186, 'J': 0.397, 'K': 0.015, 'L': 2.779, 'M': 4.738, 'N': 4.446, 'O': 9.735, 'P': 2.523,
              'Q': 1.204, 'R': 6.530, 'S': 6.805, 'T': 4.336, 'U': 3.639, 'V': 1.575, 'W': 0.037, 'X': 0.253,
              'Y': 0.006, 'Z': 0.470}


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='errori.log', level=logging.CRITICAL,
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        leggere("testo.txt")
    except IOError:
        logging.critical("E' avvenuto un errore nell'apertura del file")
        print("Il file non esiste")
    else:
        print(str(charCount()) + " caratteri")
        print(str(wordCount()) + " parole")
        print(str(rowCount()) + " righe")
        charFreq()
        print("Lingua " + lingua())
        statFile()
        chiudere()


def charCount(char=''):
    global fila
    global totale
    lunghezza = int(len(fila))
    carattere = 0
    if int(len(fila)) != 0:
        for i in range(0, len(fila)):
            if fila[i] == '\n' or fila[i] == '\r' or fila[i] == '\t' or fila[i] == ' ':
                lunghezza = lunghezza - 1
        totale = lunghezza
        if char == '':
            return lunghezza
        else:
            for i in range(0, len(fila)):
                if fila[i] == char:
                    carattere = carattere + 1
            return carattere
    return 0


def wordCount():
    global fila
    if int(len(fila)) != 0:
        parole = 0
        ultimo = len(fila) - 1
        for i in range(0, len(fila)):
            if fila[i] == '\n' or fila[i] == '\r' or fila[i] == '\t' or i == ultimo or fila[i] == ' ':
                parole = parole + 1
        return parole
    return 0


def rowCount():
    global fila
    if int(len(fila)) != 0:
        linee = 0
        if len(fila) != 0:
            linee = 1
        for i in range(0, len(fila)):
            if fila[i] == '\n':
                linee = linee + 1
        return linee
    return 0


def leggere(filename):
    global fila
    global f
    f = open(filename, "r")
    fila = f.read()
    return f


def chiudere():
    global f
    f.close()
    return


def charFreq():
    global frequenza
    global dizionario
    if int(len(fila)) != 0:
        for i in string.ascii_uppercase[:26]:
            for j in range(0, len(fila)):
                if fila[j] == i:
                    frequenza[i] = frequenza[i] + 1
        for i in string.ascii_lowercase[:26]:
            for j in range(0, len(fila)):
                if fila[j] == i:
                    frequenza[i] = frequenza[i] + 1
        for i in string.ascii_uppercase[:26]:
            frequenza[i] = (frequenza[i]) * 100.0 / totale
        for i in string.ascii_lowercase[:26]:
            frequenza[i] = (frequenza[i]) * 100.0 / totale
        for i in string.ascii_uppercase[:26]:
            dizionario[i] = frequenza[i]
        for i in string.ascii_lowercase[:26]:
            dizionario[i.upper()] = dizionario[i.upper()]+frequenza[i]


def lingua():
    global filename
    global dizionario
    global italiano
    global tedesco
    global francese
    global spagnolo
    global inglese
    global portoghese
    global finlandese
    global turco
    ita = 0
    eng = 0
    spa = 0
    fra = 0
    ger = 0
    port = 0
    if int(len(fila)) != 0:
        for i in string.ascii_uppercase[:26]:
            if dizionario[i] != 0:
                ita = (ita + (dizionario[i] - italiano[i]) * (dizionario[i] - italiano[i]))
                eng = (eng + (dizionario[i] - inglese[i]) * (dizionario[i] - inglese[i]))
                ger = (ger + (dizionario[i] - tedesco[i]) * (dizionario[i] - tedesco[i]))
                spa = (spa + (dizionario[i] - spagnolo[i]) * (dizionario[i] - spagnolo[i]))
                fra = (fra + (dizionario[i] - francese[i]) * (dizionario[i] - francese[i]))
                port = (port + (dizionario[i] - portoghese[i]) * (dizionario[i] - portoghese[i]))
        return min({'italiano': ita, 'inglese': eng, 'tedesco': ger, 'spagnolo': spa, 'francese': fra,
                    'portoghese': port}.items(), key=lambda x: x[1])[0]


def statFile():
    r = open("dizionario.txt", "w")
    r.write(str(dizionario))
    r.close()


if __name__ == '__main__':
    main()
