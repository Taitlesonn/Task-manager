from odczyt import odczyt
import os

class duties(object):
    #ImportantForTheUser - od 1 do 100 
    def __init__(self, ImportantForTheUser: int, NumberOfTasks: int):
        self.iftu = ImportantForTheUser
        self.NumOfTasks = NumberOfTasks
        self.zadania = odczyt("duties")
        self.id = 3

    def RemoveTask(self, indexNum: int):
        p = os.getcwd()
        ListOfFile = os.listdir(f"{p}/cls/zadania")
        if f"duties{indexNum}.json" in ListOfFile:
            try:
                os.remove(f"{p}/cls/zadania/fun{indexNum}.json")
            except:
                print("Problem z usunięciem pliku")
        else:
            print("Nie ma takiego pliku")
        ListOfFile = os.listdir(f"{p}/cls/zadania")
        i = 1
        for f in ListOfFile:
            if f[0] == 'd' and f[1] == 'u':
                try:
                    os.rename(f"{p}/cls/zadania/{f}", f"{p}/cls/zadania/fun{i}.json")
                    i += 1
                except:
                    print("Problem z mian nazy pliku")

    def CreateWork(self, time: int, title: str, description: str, date: str, flagi: list):
        
        #Plik JSON
        zadanie = {
            "flagi" : flagi,
            "id" : self.id,
            "time" : time,
            "title" : title,
            "description" : description,
            "date" : date,
        }