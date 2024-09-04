def updateStats(statUpdate):
  global TROOP_AP, TROOP_HEALTH, TROOP_DEFENSE, TROOP_SPEED
  TROOP_AP += statUpdate
  TROOP_HEALTH += statUpdate
  TROOP_DEFENSE += statUpdate
  TROOP_SPEED += statUpdate
  global TANK_AP, TANK_HEALTH, TANK_DEFENSE, TANK_SPEED
  TANK_AP += statUpdate
  TANK_HEALTH += statUpdate
  TANK_DEFENSE += statUpdate
  TANK_SPEED += statUpdate
  global APC_AP, APC_HEALTH, APC_DEFENSE, APC_SPEED
  APC_AP += statUpdate
  APC_HEALTH += statUpdate
  APC_DEFENSE += statUpdate
  APC_SPEED += statUpdate
  global ARTI_AP, ARTI_HEALTH, ARTI_DEFENSE, ARTI_SPEED
  ARTI_AP += statUpdate
  ARTI_HEALTH += statUpdate
  ARTI_DEFENSE += statUpdate
  ARTI_SPEED += statUpdate

  global FIGHTER_AP, FIGHTER_HEALTH, FIGHTER_DEFENSE, FIGHTER_SPEED
  FIGHTER_AP += statUpdate
  FIGHTER_HEALTH += statUpdate
  FIGHTER_DEFENSE += statUpdate
  FIGHTER_SPEED += statUpdate
  global BOMBER_AP, BOMBER_HEALTH, BOMBER_DEFENSE, BOMBER_SPEED
  BOMBER_AP += statUpdate
  BOMBER_HEALTH += statUpdate
  BOMBER_DEFENSE += statUpdate
  BOMBER_SPEED += statUpdate
  global STEALTH_AP, STEALTH_HEALTH, STEALTH_DEFENSE, STEALTH_SPEED
  STEALTH_AP += statUpdate
  STEALTH_HEALTH += statUpdate
  STEALTH_DEFENSE += statUpdate
  STEALTH_SPEED += statUpdate
  global TRANSPORT_AP, TRANSPORT_HEALTH, TRANSPORT_DEFENSE, TRANSPORT_SPEED
  TRANSPORT_AP += statUpdate
  TRANSPORT_HEALTH += statUpdate
  TRANSPORT_DEFENSE += statUpdate
  TRANSPORT_SPEED += statUpdate

  global FRIGATE_AP, FRIGATE_HEALTH, FRIGATE_DEFENSE, FRIGATE_SPEED
  FRIGATE_AP += statUpdate
  FRIGATE_HEALTH += statUpdate
  FRIGATE_DEFENSE += statUpdate
  FRIGATE_SPEED += statUpdate
  global DESTROYER_AP, DESTROYER_HEALTH, DESTROYER_DEFENSE, DESTROYER_SPEED
  DESTROYER_AP += statUpdate
  DESTROYER_HEALTH += statUpdate
  DESTROYER_DEFENSE += statUpdate
  DESTROYER_SPEED += statUpdate
  global BATTLESHIP_AP, BATTLESHIP_HEALTH, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED
  BATTLESHIP_AP += statUpdate
  BATTLESHIP_HEALTH += statUpdate
  BATTLESHIP_DEFENSE += statUpdate
  BATTLESHIP_SPEED += statUpdate
  global CARRIER_AP, CARRIER_HEALTH, CARRIER_DEFENSE, CARRIER_SPEED
  CARRIER_AP += statUpdate
  CARRIER_HEALTH += statUpdate
  CARRIER_DEFENSE += statUpdate
  CARRIER_SPEED += statUpdate

def addDays():
  import time
  with open("useful/days.txt", "r+") as daysPassed:
    days = int(daysPassed.read())
    days += 1
    if days == 7:
      daysPassed.seek(0)
      daysPassed.truncate()
      daysPassed.write('0')
      print("The week has passed, and your expenses have been deducted from your balance.")
      with open('balance/ground/troopsexpense.txt' , "r+") as troops:
        with open('balance/ground/tanksexpense.txt', "r+") as tanks:
          with open('balance/ground/apcsexpense.txt', "r+") as apcs:
            with open('balance/ground/artiexpense.txt', "r+") as artis:
              with open('balance/aerial/fightersexpense.txt', "r+") as fighters:
                with open('balance/aerial/bombersexpense.txt', "r+") as bombers:
                  troopsCost = int(troops.read())
                  tanksCost = int(tanks.read())
                  apcsCost = int(apcs.read())
                  artisCost = int(artis.read())
                  fightersCost = int(fighters.read())
                  bombersCost = int(bombers.read())
                  totalCost = troopsCost + tanksCost + apcsCost + artisCost + fightersCost + bombersCost
                  with open("balance/budget.txt", "r+") as budget:
                    with open('balance/oil/ground/tankoilexpense.txt') as tankOil:
                      with open('balance/oil/ground/apcoilexpense.txt') as artiOil:
                        with open('balance/oil/aerial/fightersoilexpense.txt') as fighterOil:
                          with open('balance/oil/aerial/bombersoilexpense.txt') as bomberOil:
                            tankOilPrice = int(tankOil.read())
                            artiOilPrice = int(artiOil.read())
                            fighterOilPrice = int(fighterOil.read())
                            bomberOilPrice = int(bomberOil.read())
                            totalOilCost = tankOilPrice + artiOilPrice + fighterOilPrice + bomberOilPrice
                            with open("balance/oilbudget.txt", "r+") as oilBudget:
                              totalOilBudget = int(oilBudget.read())
                              oilBudget.seek(0)
                              oilBudget.truncate()
                              oilBudget.write(str(totalOilBudget - totalOilCost))                 
                              print(f"{totalOilCost} oil units have been deducted from your oil account.")
                              with open('generals/general 1/salary.txt') as salary1:
                                with open('generals/general 2/salary2.txt') as salary2:
                                  with open('generals/general 3/salary3.txt') as salary3:
                                    with open('generals/general 4/salary4.txt') as salary4:
                                      with open('generals/general 5/salary5.txt') as salary5:
                                        with open('generals/general 6/salary6.txt') as salary6:
                                          gen1Salary = int(salary1.read())
                                          gen2Salary = int(salary2.read())
                                          gen3Salary = int(salary3.read())
                                          gen4Salary = int(salary4.read())
                                          gen5Salary = int(salary5.read())
                                          gen6Salary = int(salary6.read())
                                          totalSalary = gen1Salary + gen2Salary + gen3Salary + gen4Salary + gen5Salary + gen6Salary
                                          print(f"You have paid your generals ${totalSalary} in salaries.")
                                          totalBudget = int(budget.read())
                                          budget.seek(0)
                                          budget.truncate()
                                          budget.write(str(totalBudget - (totalCost + totalSalary)))    
                with open('buildings/expense/vehiclefactexpense.txt', "r+") as expense1:
                  with open('buildings/expense/bankexpense.txt', "r+") as expense2:                      
                    with open('building/expense/barracksexpense.txt', "r+") as expense3:
                      with open('buildings/expense/commcenterexpense.txt', "r+") as expense4:                      
                        with open('buildings/expense/powerplantexpense.txt', "r+") as expense5:
                          with open('buildings/expense/researchlabexpense.txt', "r+") as expense6:                      
                            with open('buildings/expense/airbaseexpense.txt', "r+") as expense7:
                              buildingExpense1 = int(expense1.read())                      
                              buildingExpense2 = int(expense2.read())                      
                              buildingExpense3 = int(expense3.read())                      
                              buildingExpense4 = int(expense4.read())                      
                              buildingExpense5 = int(expense5.read())                      
                              buildingExpense6 = int(expense6.read())                      
                              buildingExpense7 = int(expense7.read())                      
                              totalBuildingExpense = buildingExpense1 + buildingExpense2 + buildingExpense3 + buildingExpense4 + buildingExpense5 + buildingExpense6 + buildingExpense7
                              totalBudget = int(budget.read())
                              budget.seek(0)
                              budget.truncate()
                              print(f"{totalCost + totalSalary + totalBuildingExpense} has been deducted from your account.")
                              budget.write(str(totalBudget - (totalCost + totalSalary + totalBuildingExpense)))    
      time.sleep(1)
    else:
      daysPassed.seek(0)
      daysPassed.truncate()
      daysPassed.write(str(days))
      time.sleep(1)
