def recruitUnit(filePath, filePath2, unit, cost):
  with open(filePath, "r+") as troops:
      prevTroops = troops.read()
      print(f"You currently have {prevTroops} {unit}.")
      print(f"How many more {unit} do you want to recruit?: ")
      troopsRecruit = int(input(">>> "))
      if troopsRecruit <= 0:
        print(f"Can't recruit {troopsRecruit} {unit}.")
      else:
        print(f"Recruited {troopsRecruit} {unit} at the rate of ${troopsRecruit * cost} per week.")
        totalTroops = int(prevTroops) + troopsRecruit
        troops.seek(0)
        troops.truncate()
        troops.write(str(totalTroops))
      with open(filePath2, "r+") as troopsExpense:
        prevTroopsExpense = troopsExpense.read()
        troopsExpense.seek(0)
        troopsExpense.truncate()
        troopsExpense.write(str(int(prevTroopsExpense) + troopsRecruit * cost))
        
def recruitUnit2(filePath, filePath2, filePath3, unit, cost, oilCost):
  with open(filePath, "r+") as apcs:
    prevAPCS = apcs.read()
    print(f"You currently have {prevAPCS} {unit}.")
    print(f"How many more {unit} do you want to recruit?: ")
    apcsRecruit = int(input(">>> "))
    if apcsRecruit <= 0:
      print(f"Can't recruit {apcsRecruit} {unit}.")
    else:
      print(f"Recruited {apcsRecruit} {unit} at the rate of ${apcsRecruit * cost} and {apcsRecruit * oilCost} oil units per week.")
      totalAPCS = int(prevAPCS) + apcsRecruit
      apcs.seek(0)
      apcs.truncate()
      apcs.write(str(totalAPCS))
    with open(filePath2, "r+") as apcsExpense:
      prevAPCSExpense = apcsExpense.read()
      apcsExpense.seek(0)
      apcsExpense.truncate()
      apcsExpense.write(str(int(prevAPCSExpense) + apcsRecruit * cost))
    with open(filePath3, "r+") as apcsOil:
      prevAPCsOilAmount = apcsOil.read()
      apcsOil.seek(0)
      apcsOil.truncate()
      apcsOil.write(str((apcsRecruit * oilCost) + int(prevAPCsOilAmount)))

def trainUnit(unitType, duration, min, max, rank, at1, at2, at3, at4, rankFilePath, expenseFilePath, cost, healthAttr, apAttr, defenseAttr, speedAttr):
  if duration > min and duration <= max:
      print(f"{unitType} promoted to <{rank}>")

      with open(rankFilePath, "r+") as rankFile:
          with open(expenseFilePath, "r+") as expenseFile:
              prevUnitPrice = int(expenseFile.read())
              expenseFile.seek(0)
              expenseFile.truncate()
              expenseFile.write(str(prevUnitPrice + duration * cost))

              rankFile.seek(0)
              rankFile.truncate()
              rankFile.write(rank)

      healthAttr += at1
      apAttr += at2
      defenseAttr += at3
      speedAttr += at4

      return healthAttr, apAttr, defenseAttr, speedAttr

def fireUnits(filePath, filePath2, unitType, unitCost):
  with open(filePath, "r+") as file:
    prevUnitCount = int(file.read()) 
    print(f"How many {unitType} would you like to fire?")
    unitFireAmount = int(input(">>> "))
    if unitFireAmount > int(prevUnitCount):
      print(f"Can't fire more {unitType} than you already have.")
    elif unitFireAmount <= 0:
      print(f"Can't fire {unitFireAmount} {unitType}.")
    else:
      print(f"Fired {unitFireAmount} {unitType}.")
      file.seek(0)
      file.truncate()
      file.write(str(int(prevUnitCount) - unitFireAmount))
      with open(filePath2, "r+") as unitPrice:
        prevUnitCost = int(unitPrice.read())
        unitPrice.seek(0)
        unitPrice.truncate()
        unitPrice.write(str(prevUnitCost - (unitFireAmount * unitCost)))
def fireUnits2(filePath, filePath2, filePath3, unitType, unitCost, unitOilPrice):
  with open(filePath, "r+") as file:
    prevUnitCount = int(file.read()) 
    print(f"How many {unitType} would you like to fire?")
    unitFireAmount = int(input(">>> "))
    print(f"How many {unitType} would you like to fire?")
    if unitFireAmount > int(prevUnitCount):
      print(f"Can't fire more {unitType} that you already have.")
    elif unitFireAmount <= 0:
      print(f"Can't fire {unitFireAmount} {unitType}.")
    else:
      print(f"Fired {unitFireAmount} {unitType}.")
      file.seek(0)
      file.truncate()
      file.write(str(prevUnitCount - unitFireAmount))
      with open(filePath2, "r+") as unitPrice:
        unitCost = int(unitPrice.read())
        unitPrice.seek(0)
        unitPrice.truncate()
        unitPrice.write(str(unitCost - (unitFireAmount * unitCost)))
      with open(filePath3, "r+") as unitOilPrice:
        unitOilCost = int(unitOilPrice.read())
        unitOilPrice.seek(0)
        unitOilPrice.truncate()
        unitOilPrice.write(str(unitOilCost - (unitFireAmount * unitOilCost)))

def checkBalance(filePath, filePath2, unitType):
  with open(filePath) as troopExpense:
    with open(filePath2) as troops:
      unitAmount = troops.read()
      unitCost = troopExpense.read()
      print(f"You spend ${unitCost} per week on {unitAmount} {unitType}.")

def checkBalance2(filePath, filePath2, filePath3, unitType):
  with open(filePath) as tankExpense:
    with open(filePath2) as tanks:
      with open(filePath3) as tanksOils:
        unitOil = tanksOils.read()
        unitAmount = tanks.read()
        unitCost = tankExpense.read()
        print(f"You spend ${unitCost} and {unitOil} units of oil per week on {unitAmount} {unitType}.")

def carrierRecruit(filePath, filePath2, filePath3, unitType, cost, oilAmount):
  with open(filePath, "r+") as carriers:
    prevCarriers = int(carriers.read())
    if prevCarriers == 0:
      print(f"CAUTION: You are about to spend {cost} on a {unitType}, Are you sure? (Enter 1 to confirm purchase, 2 to cancel)")
      unitInput = int(input(">>> "))
      if unitInput == 1:
        print(f"Purchased a {unitType} for {cost}.")
        with open("balance/budget.txt", "r+") as budget:
          prevBudget = int(budget.read())
          budget.seek(0)
          budget.truncate()
          budget.write(str(prevBudget - cost))
          with open(filePath2, "r+") as carrierOil:
            carrierOilAmount = int(carrierOil.read())
            carrierOil.seek(0)
            carrierOil.truncate()
            carrierOil.write(str(carrierOilAmount + oilAmount))
            with open(filePath3, "r+") as carrierAmount:
              prevCarrierAmount = int(carrierAmount.read())
              carrierAmount.seek(0)
              carrierAmount.truncate()
              carrierAmount.write(str(prevCarrierAmount + 1))
      elif unitInput == 2:
        print(f"{unitType} not purchased")
      elif unitInput > 2:
        print("Invalid input.")
    else:
      print("How many more carriers would you like to buy?")
      carrierPurchaseAmount = int(input(">>> "))
      with open("balance/budget.txt", "r+") as budget:
          prevBudget = int(budget.read())
          budget.seek(0)
          budget.truncate()
          budget.write(str(prevBudget - 500000))     
      with open(filePath2, "r+") as carrierOil:
        prevCarrierOilExpense = int(carrierOil.read())
        carrierOil.seek(0)
        carrierOil.truncate()
        carrierOil.write(str(prevCarrierOilExpense + (carrierPurchaseAmount * oilAmount)))
      with open(filePath3, "r+") as carrierAmount:
        prevCarrierAmount = int(carrierAmount.read())
        carrierAmount.seek(0)
        carrierAmount.truncate()
        carrierAmount.write(str(prevCarrierAmount + carrierPurchaseAmount))
        print(f"Purchased a {unitType} for {cost}.")