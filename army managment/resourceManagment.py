def updateCapacity(enterdAmount, amount):
  with open("useful/unitcapacity.txt", "r+") as capacity:
    prevCapacity = int(capacity.read())
    capacity.seek(0)
    capacity.truncate()
    capacity.write(str(prevCapacity + enterdAmount * amount))
def updateCapacity2(value):
  with open("useful/unitcapacity.txt") as unitCapacity:
    prevUnitCapacity = int(unitCapacity.read())
    unitCapacity.seek(0)
    unitCapacity.truncate()
    unitCapacity.write(str(prevUnitCapacity - value))  
def updateMoney(amount):
  with open('buildings/weekly income/moneyincome.txt', "r+") as moneyIncome:
    prevMoneyIncome = int(moneyIncome.read())
    moneyIncome.seek(0)
    moneyIncome.truncate()
    moneyIncome.write(str(prevMoneyIncome + amount))
def updateOil(amount):
  with open('buildings/weekly income/oilincome.txt', "r+") as oilIncome:
    prevOilIncome = int(oilIncome.read())
    oilIncome.seek(0)
    oilIncome.truncate()
    oilIncome.write(str(prevOilIncome + amount * 25))
def updateResearch(amount):
  with open('buildings/weekly income/researchincome.txt', "r+") as researchIncome:
    prevResearchIncome = int(researchIncome.read()) 
    researchIncome.seek(0)
    researchIncome.truncate()           
    researchIncome.write(str(prevResearchIncome + amount * 25))