import random
import numpy as np
import pandas as pd


def attack(physical, type, attackerType1, attackerType2, defenderType1, defenderType2, power, accuracy, attck,
           targetDef, spattck, targetSpDef):
    missed = False
    if accuracy != 100:
        i = random.randint(0, 100)
        if i > accuracy:
            missed = True
            return 0, False, False, False, False, missed
    if physical:
        damage = ((42 * power * (attck / targetDef) / 50) + 2)
    else:
        damage = ((42 * power * (spattck / targetSpDef) / 50) + 2)
    critflag = False
    superEff = False
    doesntEff = False
    notVeryEff = False
    crit = random.randint(0, 15)
    if crit == 3:
        critical = 1.5
        critflag =True
    else:
        critical = 1
    if attackerType1 == type or attackerType2 == type:
        stab = 1.5
    else:
        stab = 1
    randn = random.uniform(.85, 1)
    modifier = critical * stab * randn
    damage *= modifier
    effectiveness1 = checkEff(type, defenderType1)
    effectiveness2 = checkEff(type, defenderType2)
    if effectiveness1 == 2 and effectiveness2 == 2:
        damage *= 4
        superEff = True
    if effectiveness2 == 1 and effectiveness1 == 1:
        damage *= 1
    if effectiveness2 == 2 and effectiveness1 == 1:
        damage *= 2
        superEff = True
    if effectiveness1 == 2 and effectiveness2 == 1:
        damage *= 2
        superEff = True
    if effectiveness1 == 0 or effectiveness2 == 0:
        damage = 0
        doesntEff = True
    if effectiveness1 == 1 / 2 and effectiveness2 == 1:
        damage /= 2
        notVeryEff = True
    if effectiveness1 == 1 and effectiveness2 == 1 / 2:
        damage /= 2
        notVeryEff = True
    return damage, critflag, superEff, doesntEff, notVeryEff, missed


def checkEff(movetype, defendertype):
    t = "normal,fighting,flying,poison,ground,rock,bug,ghost,steel,fire,water,grass,electric,psychic," \
        "ice,dragon,dark,fairy "
    t = t.split(",")
    damage_array = np.array([
        [2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [4, 2, 1, 1, 2, 4, 1, 0, 4, 2, 2, 2, 2, 1, 4, 2, 4, 1],
        [2, 4, 2, 2, 2, 1, 4, 2, 1, 2, 2, 4, 1, 2, 2, 2, 2, 2],
        [2, 2, 2, 1, 1, 1, 2, 1, 0, 2, 2, 4, 2, 2, 2, 2, 2, 4],
        [2, 2, 0, 4, 2, 4, 1, 2, 4, 4, 2, 1, 4, 2, 2, 2, 2, 2],
        [2, 1, 4, 2, 1, 2, 4, 2, 1, 4, 2, 2, 2, 2, 4, 2, 2, 2],
        [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 4, 2, 4, 2, 2, 4, 1],
        [0, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 1, 2],
        [2, 2, 2, 2, 2, 4, 2, 2, 1, 1, 1, 2, 1, 2, 4, 2, 2, 4],
        [2, 2, 2, 2, 2, 1, 4, 2, 4, 1, 1, 4, 2, 2, 4, 1, 2, 2],
        [2, 2, 2, 2, 4, 4, 2, 2, 2, 4, 1, 1, 2, 2, 2, 1, 2, 2],
        [2, 2, 1, 1, 4, 4, 1, 2, 1, 1, 4, 1, 2, 2, 2, 1, 2, 2],
        [2, 2, 4, 2, 0, 2, 2, 2, 2, 2, 4, 1, 1, 2, 2, 1, 2, 2],
        [2, 4, 2, 4, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 2],
        [2, 2, 4, 2, 4, 2, 2, 2, 1, 1, 1, 4, 2, 2, 1, 4, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 4, 2, 0],
        [2, 1, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 1, 1],
        [2, 4, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 4, 4, 2]
    ])
    chart = pd.DataFrame(data=damage_array / 2, index=t, columns=t)
    return int(chart.loc[movetype][defendertype])


def battleString(pokemon1, pokemon2, move, damage, critflag, superEff, doesntEff, notVeryEff, missed):
    print(pokemon1.toString() + " used " + str(move) + ". The opposing " + pokemon2.toString() + " took " + str(damage))
    if missed:
        print("The attack missed!")
        return
    if critflag:
        print("It was a critical hit!")
    if superEff:
        print("It was super effective!")
    if doesntEff:
        print("It doesn't effect the opposing " + pokemon2.toString())
    if notVeryEff:
        print("It was not very effective!")
