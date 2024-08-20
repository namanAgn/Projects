import time

print("Army management simulator")

# unit amounts
TROOPS_AMOUNT = 'army managment/units/troops.txt'
TANKS_AMOUNT = 'army managment/units/tanks.txt'
APC_AMOUNT = 'army managment/units/apcs.txt'
ARTIS_AMOUNT = 'army managment/units/artillitery.txt'
FIGHTERS_AMOUNT = 'army managment/units/fighters.txt'
BOMBERS_AMOUNT = 'army managment/units/bombers.txt'

# unit expenses
TROOPS_EXPENSE = 'army managment/balance/troopsexpense.txt'
TANKS_EXPENSE = 'army managment/balance/tanksexpense.txt'
APC_EXPENSE = 'army managment/balance/apcsexpense.txt'
ARTI_EXPENSE = 'army managment/balance/artiexpense.txt'
FIGHTERS_EXPENSE = 'army managment/balance/fightersexpense.txt'
BOMBERS_EXPENSE = 'army managment/balance/bombersexpense.txt'

# unit oil expense
TANKS_OIL_EXPENSE = 'army managment/balance/oil/tankoilexpense.txt'
APC_OIL_EXPENSE = 'army managment/balance/oil/apcoilexpense.txt'
FIGHTERS_OIL_EXPENSE = 'army managment/balance/oil/fightersoilexpense.txt'
BOMBERS_OIL_EXPENSE = 'army managment/balance/oil/bombersoilexpense.txt'

# unit ranks
TROOP_RANK = 'army managment/ranks/troopranks.txt'
TANK_RANK = 'army managment/ranks/tankranks.txt'
APC_RANK = 'army managment/ranks/apcranks.txt'
ARTI_RANK = 'army managment/ranks/artiranks.txt'
FIGHTER_RANK = 'army managment/ranks/fighterranks.txt'
BOMBER_RANK = 'army managment/ranks/bomberranks.txt'

# unit attributes

TROOP_HEALTH = 50
TROOP_AP = 25
TROOP_DEFENSE = 5
TROOP_SPEED = 15

TANK_HEALTH = 75
TANK_AP = 50
TANK_DEFENSE = 50
TANK_SPEED = 10

APC_HEALTH = 50
APC_AP = 25
APC_DEFENSE = 25
APC_SPEED = 25

ARTI_HEALTH = 25
ARTI_AP = 100
ARTI_DEFENSE = 10
ARTI_SPEED = 25

FIGHTER_HEALTH = 150
FIGHTER_AP = 125
FIGHTER_DEFENSE = 50
FIGHTER_SPEED = 100

BOMBER_HEALTH = 250
FIGHTER_AP = 250
FIGHTER_DEFENSE = 200
FIGHTER_SPEED = 50

def trainTroop(duration, min, max, rank, at1, at2, at3, at4):
  if duration > min and duration <= max:
    print(f"Troop promoted to <{rank}>")
    
    with open(TROOP_RANK, "r+") as troopRanks:
      with open(TROOPS_EXPENSE, "r+") as troopPrice:
        prevTroopPrice = int(troopPrice.read())
        troopPrice.seek(0)
        troopPrice.truncate()
        troopPrice.write(str(prevTroopPrice + duration * 3000))

        troopRanks.seek(0)
        troopRanks.truncate()
        troopRanks.write(rank)
        
    global TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED
    TROOP_HEALTH += at1
    TROOP_AP += at2
    TROOP_DEFENSE += at3
    TROOP_SPEED += at4

def addDays():
  with open("army managment/useful/days.txt", "r+") as daysPassed:
    days = int(daysPassed.read())
    days += 1
    if days == 7:
      daysPassed.seek(0)
      daysPassed.truncate()
      daysPassed.write('0')
      print("The week has passed, and your expenses have been deducted from your balance.")
      with open(TROOPS_EXPENSE , "r+") as troops:
        with open(TANKS_EXPENSE, "r+") as tanks:
          with open(APC_EXPENSE, "r+") as apcs:
            with open(ARTI_EXPENSE, "r+") as artis:
              with open(FIGHTERS_EXPENSE, "r+") as fighters:
                with open(BOMBERS_EXPENSE, "r+") as bombers:
                  troopsCost = int(troops.read())
                  tanksCost = int(tanks.read())
                  apcsCost = int(apcs.read())
                  artisCost = int(artis.read())
                  fightersCost = int(fighters.read())
                  bombersCost = int(bombers.read())
                  totalCost = troopsCost + tanksCost + apcsCost + artisCost + fightersCost + bombersCost
                  with open("army managment/balance/budget.txt", "r+") as budget:
                    totalBudget = int(budget.read())
                    budget.seek(0)
                    budget.truncate()
                    print(f"{totalCost} has been deducted from your account.")
                    budget.write(str(totalBudget - totalCost))
                  with open(TANKS_OIL_EXPENSE) as tankOil:
                    with open(APC_OIL_EXPENSE) as artiOil:
                      with open(FIGHTERS_OIL_EXPENSE) as fighterOil:
                        with open(BOMBERS_OIL_EXPENSE) as bomberOil:
                          tankOilPrice = int(tankOil.read())
                          artiOilPrice = int(artiOil.read())
                          fighterOilPrice = int(fighterOil.read())
                          bomberOilPrice = int(bomberOil.read())
                          totalOilCost = tankOilPrice + artiOilPrice + fighterOilPrice + bomberOilPrice
                          with open("army managment/balance/oilbudget.txt", "r+") as oilBudget:
                            totalOilBudget = int(oilBudget.read())
                            oilBudget.seek(0)
                            oilBudget.truncate()
                            oilBudget.write(str(totalOilBudget - totalOilCost))                 
                            print(f"{totalOilCost} oil units have been deducted from your oil account.")
      time.sleep(1)
    else:
      daysPassed.seek(0)
      daysPassed.truncate()
      daysPassed.write(str(days))
      time.sleep(1)

def main():

    print("You can do the following things: \n1 for recruit units \n2 for view active units \n3 for firing units \n4 for training units")
    activity = int(input('>>> '))
    time.sleep(1)
    if activity == 1:
      addDays()
      print("List of troops you can recruit and their cost: \n1 for SOLDIER - $1500/each \n2 for TANK - $5000, 3 oil/each \n3 for APC - $3500, 2 oil/each \n4 for ARTILLITERY - $4500/each \n5 for FIGHTER - $12000, 7 oil/each \n6 for BOMBER - $50000, 25 oil/each")
      recruitActivity = int(input(">>> "))
      if recruitActivity == 1:
        with open(TROOPS_AMOUNT, "r+") as troops:
          prevTroops = troops.read()
          print(f"You currently have {prevTroops} troops.")
          print("How many more troops do you want to recruit?: ")
          troopsRecruit = int(input(">>> "))
          if troopsRecruit <= 0:
            print(f"Can't recruit {troopsRecruit} troops.")
          else:
            print(f"Recruited {troopsRecruit} troops at the rate of ${troopsRecruit * 1500} per week.")
            totalTroops = int(prevTroops) + troopsRecruit
            troops.seek(0)
            troops.truncate()
            troops.write(str(totalTroops))
          with open(TROOPS_EXPENSE, "r+") as troopsExpense:
            prevTroopsExpense = troopsExpense.read()
            troopsExpense.seek(0)
            troopsExpense.truncate()
            troopsExpense.write(str(int(prevTroopsExpense) + troopsRecruit * 1500))
      elif recruitActivity == 2:
        with open(TANKS_AMOUNT, "r+") as tanks:
          prevTanks = tanks.read()
          print(f"You currently have {prevTanks} tanks.")
          print("How many more tanks do you want to recruit?: ")
          tanksRecruit = int(input(">>> "))
          if tanksRecruit <= 0:
            print(f"Can't recruit {tanksRecruit} tanks.")
          else:
            print(f"Recruited {tanksRecruit} tanks at the rate of ${tanksRecruit * 5000} and {tanksRecruit * 3} oil units per week.")
            totalTanks = int(prevTanks) + tanksRecruit
            tanks.seek(0)
            tanks.truncate()
            tanks.write(str(totalTanks))
          with open(TANKS_EXPENSE, "r+") as tanksExpense:
            prevTanksExpense = tanksExpense.read()
            tanksExpense.seek(0)
            tanksExpense.truncate()
            tanksExpense.write(str(int(prevTanksExpense) + tanksRecruit * 5000))
          with open(TANKS_OIL_EXPENSE, "r+") as tanksOil:
            prevOilAmount = tanksOil.read()
            tanksOil.seek(0)
            tanksOil.truncate()
            tanksOil.write(str(int(tanksRecruit * 3) + int(prevOilAmount)))
      elif recruitActivity == 3:
        with open(APC_AMOUNT, "r+") as apcs:
          prevAPCS = apcs.read()
          print(f"You currently have {prevAPCS} APCS.")
          print("How many more APCS do you want to recruit?: ")
          apcsRecruit = int(input(">>> "))
          if apcsRecruit <= 0:
            print(f"Can't recruit {apcsRecruit} APCS.")
          else:
            print(f"Recruited {apcsRecruit} APCS at the rate of ${apcsRecruit * 3500} and {apcsRecruit * 2} oil units per week.")
            totalAPCS = int(prevAPCS) + apcsRecruit
            apcs.seek(0)
            apcs.truncate()
            apcs.write(str(totalAPCS))
          with open(APC_EXPENSE, "r+") as apcsExpense:
            prevAPCSExpense = apcsExpense.read()
            apcsExpense.seek(0)
            apcsExpense.truncate()
            apcsExpense.write(str(int(prevAPCSExpense) + apcsRecruit * 3500))
          with open(APC_OIL_EXPENSE, "r+") as apcsOil:
            prevAPCsOilAmount = apcsOil.read()
            apcsOil.seek(0)
            apcsOil.truncate()
            apcsOil.write(str((apcsRecruit * 3) + int(prevAPCsOilAmount)))
      elif recruitActivity == 4:
        with open(ARTIS_AMOUNT, "r+") as arti:
          prevArtis = arti.read()
          print(f"You currently have {prevArtis} artillitery batteries.")
          print("How many more batteries do you want to recruit?: ")
          artisRecruit = int(input(">>> "))
          if artisRecruit <= 0:
            print(f"Can't recruit {artisRecruit} batteries.")
          else:
            print(f"Recruited {artisRecruit} batteries at the rate of ${artisRecruit * 4500} per week.")
            totalArtis = int(prevArtis) + artisRecruit
            arti.seek(0)
            arti.truncate()
            arti.write(str(totalArtis))
          with open(ARTI_EXPENSE, "r+") as artisExpense:
            prevArtisExpense = artisExpense.read()
            artisExpense.seek(0)
            artisExpense.truncate()
            artisExpense.write(str(int(prevArtisExpense) + artisRecruit * 4500))
      elif recruitActivity == 5:
        with open(FIGHTERS_AMOUNT, "r+") as fighters:
          prevFighters = fighters.read()
          print(f"You currently have {prevFighters} fighters.")
          print("How many more fighters do you want to recruit?: ")
          fightersRecruit = int(input(">>> "))
          if fightersRecruit <= 0:
            print(f"Can't recruit {fightersRecruit} fighters.")
          else:
            print(f"Recruited {fightersRecruit} fighters at the rate of ${fightersRecruit * 12000} and {fightersRecruit * 7} oil units per week.")
            totalFighters = int(prevFighters) + fightersRecruit
            fighters.seek(0)
            fighters.truncate()
            fighters.write(str(totalFighters))
          with open(FIGHTERS_EXPENSE, "r+") as fightersExpense:
            prevFightersExpense = fightersExpense.read()
            fightersExpense.seek(0)
            fightersExpense.truncate()
            fightersExpense.write(str(int(prevFightersExpense) + fightersRecruit * 12000))
          with open(FIGHTERS_OIL_EXPENSE, "r+") as fightersOil:
            prevFightersOilAmount = fightersOil.read()
            fightersOil.seek(0)
            fightersOil.truncate()
            fightersOil.write(str((fightersRecruit * 7) + int(prevFightersOilAmount)))
      elif recruitActivity == 6:
        with open(BOMBERS_AMOUNT, "r+") as bombers:
          prevBombers = bombers.read()
          print(f"You currently have {prevBombers} bombers.")
          print("How many more bombers do you want to recruit?: ")
          bombersRecruit = int(input(">>> "))
          if bombersRecruit <= 0:
            print(f"Can't recruit {bombersRecruit} bombers.")
          else:
            print(f"Recruited {bombersRecruit} bombers at the rate of ${bombersRecruit * 50000} and {bombersRecruit * 25} oil units per week.")
            totalBombers = int(prevBombers) + bombersRecruit
            bombers.seek(0)
            bombers.truncate()
            bombers.write(str(totalBombers))
          with open(BOMBERS_EXPENSE, "r+") as bombersExpense:
            prevBombersExpense = bombersExpense.read()
            bombersExpense.seek(0)
            bombersExpense.truncate()
            bombersExpense.write(str(int(prevBombersExpense) + bombersRecruit * 50000))
          with open(BOMBERS_OIL_EXPENSE, "r+") as bombersOil:
            prevBombersOilAmount = bombersOil.read()
            bombersOil.seek(0)
            bombersOil.truncate()
            bombersOil.write(str((bombersRecruit * 25) + int(prevBombersOilAmount)))
    elif activity == 2:
      time.sleep(1)
      addDays()
      print("Your balance is as follows: ")
      with open(TROOPS_EXPENSE) as troopExpense:
        with open(TROOPS_AMOUNT) as troops:
          troopAmount = troops.read()
          troopCost = troopExpense.read()
          print(f"You spend ${troopCost} per week on {troopAmount} troops.")
      with open(TANKS_EXPENSE) as tankExpense:
        with open(TANKS_AMOUNT) as tanks:
          with open(TANKS_OIL_EXPENSE) as tanksOils:
            tankOil = tanksOils.read()
            tankAmount = tanks.read()
            tankCost = tankExpense.read()
            print(f"You spend ${tankCost} and {tankOil} units of oil per week on {tankAmount} tanks.")
      with open(APC_EXPENSE) as apcExpense:
        with open(APC_AMOUNT) as apcs:
          with open(APC_OIL_EXPENSE) as apcOils:
            apcOil = apcOils.read()
            apcAmount = apcs.read()
            apcCost = apcExpense.read()
            print(f"You spend ${apcCost} and {apcOil} units of oil per week on {apcAmount} APCS.")
      with open(ARTI_EXPENSE) as artiExpense:
        with open(ARTIS_AMOUNT) as artis:
          artiAmount = artis.read()
          artisCost = artiExpense.read()
          print(f"You spend ${artisCost} per week on {artiAmount} artillitery batteries.")
      with open(FIGHTERS_EXPENSE) as fightersExpense:
        with open(FIGHTERS_AMOUNT) as fighters:
          with open(FIGHTERS_OIL_EXPENSE) as fightersOils:
            fightersOil = fightersOils.read()
            fightersAmount = fighters.read()
            fightersCost = fightersExpense.read()
            print(f"You spend ${fightersCost} and {fightersOil} units of oil per week on {fightersAmount} fighters.")
      with open(BOMBERS_EXPENSE) as bombersExpense:
        with open(BOMBERS_AMOUNT) as bombers:
          with open(BOMBERS_OIL_EXPENSE) as bomberOils:
            bomberOil = bomberOils.read()
            bomberAmount = bombers.read()
            bomberCost = bombersExpense.read()
            print(f"You spend ${bomberCost} and {bomberOil} units of oil per week on {bomberAmount} APCS.")
    elif activity == 3:
      time.sleep(1)
      addDays()
      with open(TROOPS_AMOUNT, "r+") as troops:
        with open(TANKS_AMOUNT, "r+") as tanks:
          with open(APC_AMOUNT, "r+") as apcs:
            with open(ARTIS_AMOUNT, "r+") as artis:
              with open(FIGHTERS_AMOUNT, "r+") as fighters:
                with open(BOMBERS_AMOUNT, "r+") as bombers:
                  troopCount = troops.read()
                  tankCount = tanks.read()
                  apcCount = apcs.read()
                  artisCount = artis.read()
                  fightersCount = fighters.read()
                  bombersCount = bombers.read()
                  print(f"You currently have: \n{troopCount} troops \n{tankCount} tanks \n{apcCount} APCS \n{artisCount} artillitery batteries \n{fightersCount} fighters \n{bombersCount} bombers")
                  print(f"Which unit would you like to fire?: (1 for troops, 2 for tanks, 3 for APCS, 4 for artillitery batteries, 5 for fighters, 6 for bombers)")
                  fireAmount = int(input(">>> "))
                  if fireAmount == 1:
                    print("How many troops would you like to fire?")
                    troopFireAmount = int(input(">>> "))
                    if troopFireAmount > int(troopCount):
                      print("Can't fire more troops that you already have.")
                    elif troopFireAmount <= 0:
                      print(f"Can't fire {troopFireAmount} troops.")
                    else:
                      print(f"Fired {troopFireAmount} troops.")
                      troops.seek(0)
                      troops.truncate()
                      troops.write(str(int(troopCount) - troopFireAmount))
                      with open(TROOPS_EXPENSE, "r+") as troopPrice:
                        troopCost = troopPrice.read()
                        troopPrice.seek(0)
                        troopPrice.truncate()
                        troopPrice.write(str(int(troopCost) - troopFireAmount * 1500))
                  elif fireAmount == 2:
                    print("How many tanks would you like to fire?")
                    tankFireAmount = int(input(">>> "))
                    if tankFireAmount > int(tankCount):
                      print("Can't fire more tanks that you already have.")
                    elif tankFireAmount <= 0:
                      print(f"Can't fire {tankFireAmount} tanks.")
                    else:
                      print(f"Fired {tankFireAmount} tanks.")
                      tanks.seek(0)
                      tanks.truncate()
                      tanks.write(str(int(tankCount) - tankFireAmount))
                      with open(TANKS_EXPENSE, "r+") as tankPrice:
                        tankCost = tankPrice.read()
                        tankPrice.seek(0)
                        tankPrice.truncate()
                        tankPrice.write(str(int(tankCost) - tankFireAmount * 5000))
                      with open(TANKS_OIL_EXPENSE, "r+") as tankOilPrice:
                        tankOilCost = tankOilPrice.read()
                        tankOilPrice.seek(0)
                        tankOilPrice.truncate()
                        tankOilPrice.write(str(int(tankOilCost) - tankFireAmount * 3))
                  elif fireAmount == 3:
                    print("How many APCS would you like to fire?")
                    apcFireAmount = int(input(">>> "))
                    if apcFireAmount > int(apcCount):
                      print("Can't fire more tanks that you already have.")
                    elif apcFireAmount <= 0:
                      print(f"Can't fire {apcFireAmount} APCS.")
                    else:
                      print(f"Fired {apcFireAmount} APCS.")
                      apcs.seek(0)
                      apcs.truncate()
                      apcs.write(str(apcCount - apcFireAmount))
                      with open(APC_EXPENSE, "r+") as apcPrice:
                        apcCost = apcPrice.read()
                        apcPrice.seek(0)
                        apcPrice.truncate()
                        apcPrice.write(str(int(apcCost) - apcFireAmount * 3500))
                      with open(APC_OIL_EXPENSE, "r+") as apcOilPrice:
                        apcOilCost = apcOilPrice.read()
                        apcOilPrice.seek(0)
                        apcOilPrice.truncate()
                        apcOilPrice.write(str(int(apcOilCost) - apcFireAmount * 2))
                  elif fireAmount == 4:
                    print("How many artillitery batteries would you like to fire?")
                    artiFireAmount = int(input(">>> "))
                    if artiFireAmount > int(artisCount):
                      print("Can't fire more artillitery batteries that you already have.")
                    elif artiFireAmount <= 0:
                      print(f"Can't fire {artiFireAmount} troops.")
                    else:
                      print(f"Fired {artiFireAmount} troops.")
                      artis.seek(0)
                      artis.truncate()
                      artis.write(str(int(artisCount) - artiFireAmount))
                      with open(ARTI_EXPENSE, "r+") as artiPrice:
                        artiCost = artiPrice.read()
                        artiPrice.seek(0)
                        artiPrice.truncate()
                        artiPrice.write(str(int(artiCost) - artiFireAmount * 4500))
                  elif fireAmount == 5:
                    print("How many fighters would you like to fire?")
                    fighterFireAmount = int(input(">>> "))
                    if fighterFireAmount > int(fightersCount):
                      print("Can't fire more fighters that you already have.")
                    elif fighterFireAmount <= 0:
                      print(f"Can't fire {fighterFireAmount} fighters.")
                    else:
                      print(f"Fired {fighterFireAmount} fighters.")
                      fighters.seek(0)
                      fighters.truncate()
                      fighters.write(str(int(fightersCount) - fighterFireAmount))
                      with open(FIGHTERS_EXPENSE, "r+") as fighterPrice:
                        fighterCost = fighterPrice.read()
                        fighterPrice.seek(0)
                        fighterPrice.truncate()
                        fighterPrice.write(str(int(fighterCost) - fighterFireAmount * 12000))
                      with open(FIGHTERS_OIL_EXPENSE, "r+") as fighterOilPrice:
                        fighterOilCost = fighterOilPrice.read()
                        fighterOilPrice.seek(0)
                        fighterOilPrice.truncate()
                        fighterOilPrice.write(str(int(fighterOilCost) - fighterFireAmount * 7))
                  elif fireAmount == 6:
                    print("How many bombers would you like to fire?")
                    bomberFireAmount = int(input(">>> "))
                    if bomberFireAmount > int(bombersCount):
                      print("Can't fire more tanks that you already have.")
                    elif bomberFireAmount <= 0:
                      print(f"Can't fire {bomberFireAmount} bombers.")
                    else:
                      print(f"Fired {bomberFireAmount} bombers.")
                      bombers.seek(0)
                      bombers.truncate()
                      bombers.write(str(bombersCount - bomberFireAmount))
                      with open(BOMBERS_EXPENSE, "r+") as bombersPrice:
                        bomberCost = bombersPrice.read()
                        bombersPrice.seek(0)
                        bombersPrice.truncate()
                        bombersPrice.write(str(int(bomberCost) - bomberFireAmount * 50000))
                      with open(BOMBERS_OIL_EXPENSE, "r+") as bombersOilPrice:
                        bombersOilCost = bombersOilPrice.read()
                        bombersOilPrice.seek(0)
                        bombersOilPrice.truncate()
                        bombersOilPrice.write(str(int(bombersOilCost) - bomberFireAmount * 25))
                        time.sleep(1)
    elif activity == 4:
      time.sleep(1)
      print("Price of training: \nTroop - $3000/week \nTank - $7000/week \nAPC - $5000/week \nArtillery Batteries - $6000/week \nFighters - $25000/week \nBombers - $75000/week")
      time.sleep(1)
      print("1 to train TROOPS \n2 to train TANKS \n3 to train APCs \n4 to train ARTILLERY \n5 to train FIGHTERS \n6 to train BOMBERS")
      trainActivity = int(input(">>> "))
      if trainActivity == 1:
        print("For how many weeks would you like to train?")
        troopAmountInput = int(input(">>> "))
        if troopAmountInput <= 0:
          print(f"Can't train for {troopAmountInput}.")

        trainTroop(troopAmountInput, 0, 2, "Corporal", 5, 5, 5, 5)
        trainTroop(troopAmountInput, 2, 4, "Sergant", 10, 10, 10, 10)
        trainTroop(troopAmountInput, 4, 6, "Lieutant", 20, 20, 20, 20)
        trainTroop(troopAmountInput, 6, 8, "Captain", 25, 25, 25, 25)
        trainTroop(troopAmountInput, 8, 10, "Lieutant Colonel", 30, 30, 30, 30)
        trainTroop(troopAmountInput, 10, 12, "General", 40, 40, 40, 40)
        trainTroop(troopAmountInput, 12, 14, "General Major", 45, 45, 45, 45)
        trainTroop(troopAmountInput, 16, 18, " 4 Star-General", 50, 50, 50, 50)


for i in range(7):
  main()
