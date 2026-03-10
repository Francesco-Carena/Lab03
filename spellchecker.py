import time

import multiDictionary
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDictionary = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        print("\n"+txtIn)
        txtIn = txtIn.strip().lower()
        txtIn = replaceChars(txtIn)
        #ricerca con in
        paroleAnalizzate,tempo = self.multiDictionary.searchWord(txtIn, language)
        print("\nParole sbagliate:")
        for parolaRicca in paroleAnalizzate:
            if not parolaRicca.corretta:
                print(f"{parolaRicca}")
        print(f"tempo impiegato per la ricerca: {tempo}")
        #ricerca con for
        paroleAnalizzate, tempo = self.multiDictionary.ricercaFor(txtIn, language)
        print("\nParole sbagliate:")
        for parolaRicca in paroleAnalizzate:
            if not parolaRicca.corretta:
                print(f"{parolaRicca}")
        print(f"tempo impiegato per la ricerca: {tempo}")
        #ricerca dicotomica
        paroleAnalizzate, tempo = self.multiDictionary.ricercaDicotomica(txtIn, language)
        print("\nParole sbagliate:")
        for parolaRicca in paroleAnalizzate:
            if not parolaRicca.corretta:
                print(f"{parolaRicca}")
        print(f"tempo impiegato per la ricerca: {tempo}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def stampaTutto(self,language):
        self.multiDictionary.printDic(language)


def replaceChars(text):
    chars="\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text=text.replace(c,"")
    return text