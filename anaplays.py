def bucket_sort(lista, war):
    # Tworzymy kubełki dla wszystkich wartości w `war`
    buckets = [[] for _ in war]
    
    for i in lista:
        buckets[war.index(i)].append(i)
    
    posortowane = []

    for bucket in buckets:
        posortowane.extend(bucket)
    
    return posortowane




def Anal_iza(zadania, waz: map):
    #Pod nazwą typu zadania w mapie jest wartość ważności dla użytkownika
    zad = []
    for z in zadania:
        for za in z:
            zad.append(za)
    zad = []
    for i in zadania:
        match(zad["id"]):
            case 1:
                zad.append(waz["fun"])
            case 2:
                zad.append(waz["work"])
            case 3:
                zad.append(waz["duties"])
            case 4:
                zad.append(waz["prr"])
            case _:
                zad.append(0)
    war = [waz["fun"], waz["work"], waz["duties"], waz["prr"]]
    
    zad = bucket_sort(zad, war)


