def map_war(war) -> map:
    if len(war) != 4:
        return -1
    mapa = {
        "fun" : war[0],
        "work" : war[1],
        "duties" : war[2],
        "ppr" : war[3]
    }
    return mapa