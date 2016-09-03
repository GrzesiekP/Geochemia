from tkinter.messagebox import showinfo

def IdentifySeparator(line):
    commas = 0
    semicolons = 0
    separator = ""
    for char in line:
        if char == ",":
            commas += 1
        elif char == ";":
            semicolons += 1

    if commas > semicolons:
        separator = ","
    elif commas < semicolons:
        separator = ";"
    
    return separator

def convert(input, output):

    #tworzenie list konkretnych zmiennych
    lines = []
    probki = []
    probki_unique = []
    zwiazki = []
    zwiazki_unique = []
    wartosci = []
    jednostki = []

    #zmiana pliku na list? list rozdzielonych ; lub ,
    for line in input:
        line_separator = IdentifySeparator(line)
        lines.append(line.split(line_separator))

    input.close()

    #tworzenie listy zwierajacej same wyniki bez naglowkow i ostatniej pustej linijki
    wyniki = lines[1:]

    #wypelnianie list zmiennych wartosciami z pliku
    for line in wyniki:
        nazwa_probki = line[0]
        zwiazek = line[1]
        wartosc = line[2]
        jednostka = line[3]
    
        probki.append(nazwa_probki)
        zwiazki.append(zwiazek)
        wartosci.append(wartosc)
        jednostki.append(jednostka)

        if nazwa_probki not in probki_unique:
            probki_unique.append(nazwa_probki)

        if zwiazek not in zwiazki_unique:
            zwiazki_unique.append(zwiazek)

    #tworzenie pierwszego wiersza do raportu wyjsciowego
    naglowki = ["Nr probki"]
    for x in zwiazki_unique:
        naglowki.append(x)

    #tworzenie raportu i dodawanie do niego pierwszego wiersza
    raport = []
    raport.append(naglowki)

    #dodanie wiersza (w kazdym wierszu tyle liczba miejsc = liczba unikalnych zwiazkow w pliku + 1 (nazwa probki)) dla kazdej probki.
    for nr_probki in probki_unique:
        wynik_dla_probki = []
        for item in naglowki:
            wynik_dla_probki.append("brak")
        for wynik in wyniki:
            if wynik[0] == nr_probki and wynik_dla_probki[0] == "brak":
                wynik_dla_probki[0] = wynik[0]
        raport.append(wynik_dla_probki)

    #wpisywanie wartosci do raportu
    for wynik in wyniki:
        numer_pr = wynik[0]
        zwiazek = wynik[1]
        wartosc = wynik[2]
        wiersz = probki_unique.index(numer_pr) + 1
        wiersz = raport[wiersz]
        pos_zwiazku = zwiazki_unique.index(zwiazek) + 1
        wiersz[pos_zwiazku] = wartosc

    #konwertowanie raportu do stringu do zpaisu w pliku
    string = ""
    for row in raport:
        for item in row:
            string = string + item + ";"
            str_len = len(string)
        string = string[:str_len-1]
        string += "\n"

    print (string)
    print ("=========================================")

    #zapisywanie do pliku
    output.write(string)
    output.close()

    showinfo("Wykonano", "Konwersja wykonana")

    

