import sys
import json
import gui
import anaplays
import war

sys.path.append('./cls')
from cls import fun, work, duties, PrivateProjects


zabawa = fun.fun(0, 0)
praca = work.work(0, 0)
obowiazki = duties.duties(0, 0)
prywatneProjekty = PrivateProjects.ppr(0, 0)

def init():
    with open("start.json", "r") as f:
        dane = json.load(f)

        zabawa.iftu = dane["fun"]["iftu"]
        zabawa.NumOfTasks = dane["fun"]["NumberOfTasks"]

        praca.iftu = dane["work"]["iftu"]
        praca.NumOfTasks = dane["work"]["NumberOfTasks"]

        obowiazki.iftu = dane["duties"]["iftu"]
        obowiazki.NumOfTasks = dane["duties"]["NumberOfTasks"]

        prywatneProjekty.iftu = dane["PrivateProjects"]["iftu"]
        prywatneProjekty.NumOfTasks = dane["PrivateProjects"]["NumberOfTasks"]




#rozmiar GUI
def loda_deta_for_gui():
    with open("FGui.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    init()
    Awar = war.map_war([zabawa.iftu, praca.iftu, obowiazki.iftu, prywatneProjekty.iftu])
    if Awar == -1:
        print("ERROR")
    GUI_DETA = loda_deta_for_gui()
    anaplays.Anal_iza([zabawa.zadania, praca.zadania, obowiazki.zadania, prywatneProjekty.zadania], Awar)

    #gui.Gmain(GUI_DETA["with"], GUI_DETA["hight"])
    
    
