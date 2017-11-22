fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]


def selectCharacter(movimientos):
    posicionInicial = (0,0)
    movimientosValor = {"up":1,"down":-1,"left":-1,"right":1}
    playerSelected = []
    for movimiento in movimientos:
        if movimiento == "up":
            posicionInicial = (0,posicionInicial[1]) if (posicionInicial[0] == -1) else posicionInicial
        elif movimiento == "down":
            posicionInicial = (-1,posicionInicial[1]) if (posicionInicial[0] == 0) else posicionInicial
        elif movimiento == "left":
            posicionInicial = (posicionInicial[0],5) if posicionInicial[1] <= 0 else (posicionInicial[0],posicionInicial[1]-1)
        else:
            posicionInicial = (posicionInicial[0],0) if posicionInicial[1] >= 5 else (posicionInicial[0],posicionInicial[1]+1)
        playerSelected.append(fighters[posicionInicial[0]][posicionInicial[1]])
    return playerSelected









moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']
#['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']
moves = ['right']*8
#['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']

print(selectCharacter(moves))
