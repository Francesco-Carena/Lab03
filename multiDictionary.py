import dictionary as d
import richWord
import richWord as rw
import time


class MultiDictionary:

    def __init__(self):
        self.italian = d.Dictionary()
        self.english = d.Dictionary()
        self.spanish = d.Dictionary()

        self.italian.loadDictionary("resources/Italian.txt")
        self.english.loadDictionary("resources/English.txt")
        self.spanish.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language == "english":
            self.english.printAll()
        elif language == "italian":
            self.italian.printAll()
        elif language == "spanish":
            self.spanish.printAll()

    def searchWord(self, words, language):
        words=words.split()
        analizzate=[]
        print("ricerca con in")
        if language == "italian":
            startTime=time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                if parola in self.italian.parole:
                    parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime
        elif language == "spanish":
            startTime = time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                if parola in self.spanish.parole:
                    parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime
        elif language == "english":
            startTime = time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                if parola in self.english.parole:
                    parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate,totaleTime

    def ricercaFor(self, words, language):
        words = words.split()
        analizzate = []
        print("ricerca con for")
        if language == "italian":
            startTime=time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                for p in self.italian.parole:
                    if p==parola:
                        parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime
        if language == "spanish":
            startTime=time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                for p in self.spanish.parole:
                    if p==parola:
                        parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime
        if language == "english":
            startTime=time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)
                for p in self.english.parole:
                    if p==parola:
                        parola_ricca.corretta=True
                analizzate.append(parola_ricca)
            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime

    def ricercaDicotomica(self, words, language):
        words = words.split()
        analizzate = []
        print("ricerca dicotomica")

        if language == "italian":
            startTime = time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)

                # Imposto i puntatori per la ricerca dicotomica
                inizio = 0
                fine = len(self.italian.parole) - 1

                while inizio <= fine:
                    mezzo = (inizio + fine) // 2

                    if self.italian.parole[mezzo] == parola:
                        parola_ricca.corretta = True
                        break  # Parola trovata, esco dal while!
                    elif self.italian.parole[mezzo] > parola:
                        fine = mezzo - 1  # Cerco nella prima metà
                    else:
                        inizio = mezzo + 1  # Cerco nella seconda metà

                analizzate.append(parola_ricca)

            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime

        elif language == "spanish":
            startTime = time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)

                inizio = 0
                fine = len(self.spanish.parole) - 1

                while inizio <= fine:
                    mezzo = (inizio + fine) // 2

                    if self.spanish.parole[mezzo] == parola:
                        parola_ricca.corretta = True
                        break
                    elif self.spanish.parole[mezzo] > parola:
                        fine = mezzo - 1
                    else:
                        inizio = mezzo + 1

                analizzate.append(parola_ricca)

            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime

        elif language == "english":
            startTime = time.time()
            for parola in words:
                parola_ricca = rw.RichWord(parola)

                inizio = 0
                fine = len(self.english.parole) - 1

                while inizio <= fine:
                    mezzo = (inizio + fine) // 2

                    if self.english.parole[mezzo] == parola:
                        parola_ricca.corretta = True
                        break
                    elif self.english.parole[mezzo] > parola:
                        fine = mezzo - 1
                    else:
                        inizio = mezzo + 1

                analizzate.append(parola_ricca)

            endTime = time.time()
            totaleTime = endTime - startTime
            return analizzate, totaleTime