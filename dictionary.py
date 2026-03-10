class Dictionary:
    def __init__(self):
        self.parole=[]

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            riga = file.readline()
            while riga:
                self.parole.append(riga.strip())
                riga = file.readline()
            file.close()

    def printAll(self):
        for parola in self.parole:
            print(parola)

    @property
    def dict(self):
        return self._dict