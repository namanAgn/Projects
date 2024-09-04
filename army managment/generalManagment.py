
def hireGeneral(GENERAL_NAME, GENERAL_STRENGHT, GENERAL_TRAIT, GENERAL_PRICE, filePath):
    print(f"Details of {GENERAL_NAME}:")
    print(f"Leadership: {GENERAL_STRENGHT} \nTrait: {GENERAL_TRAIT} \nSalary: {GENERAL_PRICE}")
    print(f"Would you like to hire General {GENERAL_NAME} (1 to hire, 2 to not)")
    generalSelect = int(input(">>> "))
    if generalSelect == 1:
      print(f"Hired General {GENERAL_NAME}")
      with open(filePath, "r+") as generalSalary:
        generalSalary.seek(0)
        generalSalary.truncate()
        generalSalary.write(str(GENERAL_PRICE))
    elif generalSelect == 2:
      print(f"{GENERAL_NAME} was not hired.")

def checkGeneral(generalSalary, generalName):
  if generalSalary > 0:
    print(generalName)
def checkSalary(generalSalary, generalName):
  if generalSalary > 0:
    print(f"{generalName}: \n {generalSalary}")
def checkStats(generalSalary, filePath, generalName, generalTrait, generalStrenght):
  if generalSalary > 0:
    with open(filePath, "r+") as rank:
      generalRank = rank.read()
      print(f"{generalName}: \nRank: {generalRank} \nTrait: {generalTrait} \nLoyalty/Leadership: {generalStrenght}")
def fireGeneral(filePath, filePath2, generalName):
  print(f"Fired {generalName}")
  with open(filePath, "r+") as generalRank:
    with open(filePath2, "r+") as generalSalary:
      generalSalary.seek(0)
      generalSalary.truncate()
      generalSalary.write("0")

      generalRank.seek(0)
      generalRank.truncate()
      generalRank.write("Private")
def checkName(generalSalary, generalName):
  if generalSalary > 0:
    print(generalName)
def trainGeneral(filePath, filePath2, value1, value2, prevStrenght, strenght, rank, salary, name):
      print(f"How long would you like to train {name}?")
      duration = int(input(">>> "))
      if duration <= 0:
        print(f"Can't train general for {duration}")
      else:
        with open(filePath, "r+") as rank:
          with open(filePath2, "r+") as fileSalary:
            if duration > value1 and duration <= value2:
              print(f"General {name} has been promoted to {rank}")
              print(f"General {name}'s salary now is {salary}")
              rank.seek(0)
              rank.truncate()
              rank.write(rank)
              fileSalary.seek(0)
              fileSalary.truncate()
              fileSalary.write(str(salary))
              prevStrenght + strenght
