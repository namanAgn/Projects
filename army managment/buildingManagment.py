def buildBuilding(amount, buildingType, buildingFilePath, cost):
  print(f"Built {amount} {buildingType}.")
  with open(buildingFilePath, "r+") as buildingAmount:
    prevBuildingAmount = int(buildingAmount.read())              
    buildingAmount.seek(0)
    buildingAmount.truncate()
    buildingAmount.write(str(prevBuildingAmount + amount))
  with open("balance/budget.txt", "r+") as balance:
    prevBalance = int(balance.read())
    balance.seek(0)
    balance.truncate()
    balance.write(str(prevBalance - cost))
def destroyBuilding(buildingLoc, buildingExpense, destroyingAmount, value):
  with open(buildingLoc, "r+") as buildingAmount:
    prevBuildingAmount = int(buildingAmount.read())
    if prevBuildingAmount == 0:
      print("You have 0 of this building. You cant destroy more.")
    elif prevBuildingAmount < destroyingAmount:
      buildingAmount.seek(0)
      buildingAmount.truncate()
      buildingAmount.write("0")

      with open(buildingExpense, "r+") as buildingExpenses:
        prevBuildingExpense = int(buildingExpenses.read())
        buildingExpenses.seek(0)
        buildingExpenses.truncate()
        buildingExpenses.write(str(prevBuildingExpense - (destroyingAmount * value)))
      with open("budget/balance.txt", "r+") as balance:
        prevBalance = int(balance.read())
        balance.seek(0)
        balance.truncate()
        balance.write(str(prevBalance + value))

    else:
      buildingAmount.seek(0)
      buildingAmount.truncate()
      buildingAmount.write(str(prevBuildingAmount - destroyingAmount))

      with open(buildingExpense, "r+") as buildingExpenses:
        prevBuildingExpense = int(buildingExpenses.read())
        buildingExpenses.seek(0)
        buildingExpenses.truncate()
        buildingExpenses.write(str(prevBuildingExpense - (destroyingAmount * value)))
      with open("budget/balance.txt", "r+") as balance:
        prevBalance = int(balance.read())
        balance.seek(0)
        balance.truncate()
        balance.write(str(prevBalance + value))
