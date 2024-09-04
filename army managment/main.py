import time

# TODOS
# Add a resource simulation (basically completed)
# Just need to add text files for resources and add to them at end of week

# Add properties for the user to make money
# Almost completed, working on managing buildings

# Update addDays() to take expense of newly added units

# Add technology
# Not even started 

print("Army management simulator")

# buildings income
MONEY_INCOME = 'buildings/weekly income/moneyincome.txt'
OIL_INCOME = 'buildings/weekly income/oilincome.txt'
RESEARCH_INCOME = 'buildings/weekly income/researchincome.txt'

# buildings
AIRBASE = 'buildings/airbase.txt'
BANK = 'buildings/bank.txt'
BARRACKS = 'buildings/barracks.txt'
COMM_CENTER = 'buildings/barracks.txt'
POWER_PLANT = 'buildings/powerplant.txt'
RESEARCH_LAB = 'buildings/reserachlab.txt'
VEHICLE_FACTORY = 'buildings/vehiclefact.txt'

# building levels
AIRBASE_RANK = 'buildings/level/airbaserank.txt'
BANK_RANK = 'buildings/level/bankrank.txt'
BARRACKS_RANK = 'buildings/level/barracksrank.txt'
COMM_CENTER_RANK = 'buildings/level/commcenterrank.txt'
POWER_PLANT_RANK = 'buildings/level/powerplantrank.txt'
RESEARCH_LAB_RANK = 'buildings/level/researchlabrank.txt'
VEHICLE_FACTORY_RANK = 'buildings/level/vehiclefactrank.txt'

# building expenses
AIRBASE_EXPENSE = 'buildings/expense/airbaseexpense.txt'
BANK_EXPENSE = 'buildings/expense/bankexpense.txt'
BARRACKS_EXPENSE = 'building/expense/barracksexpense.txt'
COMM_CENTER_EXPENSE = 'buildings/expense/commcenterexpense.txt'
POWER_PLANT_EXPENSE = 'buildings/expense/powerplantexpense.txt'
RESEARCH_LAB_EXPENSE = 'buildings/expense/researchlabexpense.txt'
VEHICLE_FACTORY_EXPENSE = 'buildings/expense/vehiclefactexpense.txt'

# generals
GENERAL_1_NAME = 'Thaldrak Ironfist'
GENERAL_1_STRENGHT = 50
GENERAL_1_TRAIT = 'Charismatic'
GENERAL_1_PRICE = 7500

GENERAL_2_NAME = 'Velara Moonstrike'
GENERAL_2_STRENGHT = 25
GENERAL_2_TRAIT = 'Cunning'
GENERAL_2_PRICE = 5000

GENERAL_3_NAME = 'Grimwald Bloodhelm'
GENERAL_3_STRENGHT = 75
GENERAL_3_TRAIT = 'Merciful'
GENERAL_3_PRICE = 12500

GENERAL_4_NAME = 'Kaelus Stormspear'
GENERAL_4_STRENGHT = 60
GENERAL_4_TRAIT = 'Ruthless'
GENERAL_4_PRICE = 10000

GENERAL_5_NAME = 'Zerathar Voidhammer'
GENERAL_5_STRENGHT = 45
GENERAL_5_TRAIT = 'Psychopathic'
GENERAL_5_PRICE = 6000

GENERAL_6_NAME = 'Azura Starwind'
GENERAL_6_STRENGHT = 85
GENERAL_6_TRAIT = 'Patient'
GENERAL_6_PRICE = 17500

# general ranks
GENERAL_1_RANK = 'generals/general 1/rank.txt'
GENERAL_2_RANK = 'generals/general 2/rank2.txt'
GENERAL_3_RANK = 'generals/general 3/rank3.txt'
GENERAL_4_RANK = 'generals/general 4/rank4.txt'
GENERAL_5_RANK = 'generals/general 5/rank5.txt'
GENERAL_6_RANK = 'generals/general 6/rank6.txt'

# general salaries
GENERAL_1_SALARY = 'generals/general 1/salary.txt'
GENERAL_2_SALARY = 'generals/general 2/salary2.txt'
GENERAL_3_SALARY = 'generals/general 3/salary3.txt'
GENERAL_4_SALARY = 'generals/general 4/salary4.txt'
GENERAL_5_SALARY = 'generals/general 5/salary5.txt'
GENERAL_6_SALARY = 'generals/general 6/salary6.txt'

# unit amounts
TROOPS_AMOUNT = 'units/ground/troops.txt'
TANKS_AMOUNT = 'units/ground/tanks.txt'
APC_AMOUNT = 'units/ground/apcs.txt'
ARTIS_AMOUNT = 'units/ground/artillitery.txt'

FIGHTERS_AMOUNT = 'units/aerial/fighters.txt'
BOMBERS_AMOUNT = 'units/aerial/bombers.txt'
TRANSPORT_JETS_AMOUNT = 'units/aerial/transportjets.txt'
STEALTH_JETS_AMOUNT = 'units/aerial/stealthjets.txt'

BATTLESHIP_AMOUNT = 'units/naval/battleships.txt'
CARRIER_AMOUNT = 'units/naval/carriers.txt'
DESTROYER_AMOUNT = 'units/naval/destroyers.txt'
FRIGATE_AMOUNT = 'units/naval/frigates.txt'

# unit expenses
TROOPS_EXPENSE = 'balance/ground/troopsexpense.txt'
TANKS_EXPENSE = 'balance/ground/tanksexpense.txt'
APC_EXPENSE = 'balance/ground/apcsexpense.txt'
ARTI_EXPENSE = 'balance/ground/artiexpense.txt'

FIGHTERS_EXPENSE = 'balance/aerial/fightersexpense.txt'
BOMBERS_EXPENSE = 'balance/aerial/bombersexpense.txt'
STEALTH_JETS_EXPENSE = 'balance/aerial/stealthexpense.txt'
TRANSPORT_JETS_EXPENSE = 'balance/aerial/transportexpense.txt'

FRIGATE_EXPENSE = 'balance/naval/frigatesexpense.txt'
DESTROYER_EXPENSE = 'balance/naval/destroyerexpense.txt'
BATTLESHIP_EXPENSE = 'balance/naval/battleshipexpense.txt'
CARRIER_EXPENSE = 'balance/naval/carriersexpense.txt'

# unit oil expense
TANKS_OIL_EXPENSE = 'balance/oil/ground/tankoilexpense.txt'
APC_OIL_EXPENSE = 'balance/oil/ground/apcoilexpense.txt'

FIGHTERS_OIL_EXPENSE = 'balance/oil/aerial/fightersoilexpense.txt'
BOMBERS_OIL_EXPENSE = 'balance/oil/aerial/bombersoilexpense.txt'
STEALTH_JETS_OIL_EXPENSE = 'balance/oil/aerial/stealthoilexpense.txt'
TRANSPORT_JETS_OIL_EXPENSE = 'balance/oil/aerial/transportoilexpense.txt'

FRIGATE_OIL_EXPENSE = 'balance/oil/naval/frigateoilexpense.txt'
DESTROYER_OIL_EXPENSE = 'balance/oil/naval/destroyeroilexpense.txt'
BATTLESHIP_OIL_EXPENSE = 'balance/oil/naval/battleshipoilexpesene.txt'
CARRIER_OIL_EXPENSE = 'balance/oil/naval/carrieroilexpense.txt'

# unit ranks
TROOP_RANK = 'ranks/ground/troopranks.txt'
TANK_RANK = 'ranks/ground/tankranks.txt'
APC_RANK = 'ranks/ground/apcranks.txt'
ARTI_RANK = 'ranks/ground/artiranks.txt'

FIGHTER_RANK = 'ranks/aerial/fighterranks.txt'
BOMBER_RANK = 'ranks/aerial/bomberranks.txt'
STEALTH_JETS_RANK = 'ranks/aerial/stealthranks.txt'
TRANSPORT_JETS_RANK = 'ranks/aerial/transportranks.txt'

FRIGATE_RANK = 'ranks/naval/frigateranks.txt'
DESTROYER_RANK = 'ranks/naval/destroyerranks.txt'
BATTLESHIP_RANK = 'ranks/naval/battleshipranks.txt'
CARRIER_RANK = 'ranks/naval/carrierranks.txt'

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
BOMBER_AP = 250
BOMBER_DEFENSE = 200
BOMBER_SPEED = 50

STEALTH_HEALTH = 100
STEALTH_AP = 25
STEALTH_DEFENSE = 200
STEALTH_SPEED = 400

TRANSPORT_HEALTH = 350
TRANSPORT_AP = 50
TRANSPORT_DEFENSE = 150
TRANSPORT_SPEED = 100



FRIGATE_HEALTH = 75
FRIGATE_AP = 75
FRIGATE_DEFENSE = 50
FRIGATE_SPEED = 75

DESTROYER_HEALTH = 50
DESTROYER_AP = 250
DESTROYER_DEFENSE = 150
DESTROYER_SPEED = 50

BATTLESHIP_HEALTH = 250
BATTLESHIP_AP = 500
BATTLESHIP_DEFENSE = 300
BATTLESHIP_SPEED = 25

CARRIER_HEALTH = 1500
CARRIER_AP = 2000
CARRIER_DEFENSE = 1000
CARRIER_SPEED = 10

from unitManagment import recruitUnit, recruitUnit2, trainUnit, fireUnits, fireUnits2, checkBalance, checkBalance2, carrierRecruit
from generalManagment import hireGeneral, checkGeneral, checkName, checkSalary, checkStats, fireGeneral, trainGeneral
from buildingManagment import buildBuilding, destroyBuilding
from resourceManagment import updateCapacity, updateMoney, updateOil, updateResearch, updateCapacity2
from utils import updateStats, addDays

def main():
    print("You can do the following things: \n1 for RECRUIT UNITS \n2 for VIEWING ACTIVE UNITS \n3 for FIRING UNITS \n4 for TRAINING UNITS \n5 to RECRUIT GENERALS \n6 to MANAGE GENERALS \n7 to TRAIN GENERALS \n8 to BUILD BUILDINGS \n9 to MANAGE BUILDINGS")
    activity = int(input('>>> '))
    time.sleep(1)
    if activity == 1:
      addDays()
      print("List of troops you can recruit and their cost: \n1 for SOLDIER - $1,500/each \n2 for TANK - $5,000, 3 oil/each \n3 for APC - $3,500, 2 oil/each \n4 for ARTILLITERY - $4,500/each \n5 for FIGHTER - $12,000, 7 oil/each \n6 for BOMBER - $50,000, 25 oil/each \n7 for STEALTH JET - $1,000,000 (once), 75 oil/each \n8 for TRANSPORT JET - $100,000, 50 oil/each \n9 for FRIGATE - $75,000, 15 oil/each \n10 for DESTROYER - $100,000, 35 oil/each \n11 for BATTLESHIP - $150,000, 50 oil/each \n12 for AIRCRAFT CARRIER - $500,000 (once), 120 oil/each")      
      recruitActivity = int(input(">>> "))
      if recruitActivity == 1:
        recruitUnit(TROOPS_AMOUNT, TROOPS_EXPENSE, "troop(s)", 1500)
      elif recruitActivity == 2:
        recruitUnit2(TANKS_AMOUNT, TANKS_EXPENSE, TANKS_OIL_EXPENSE, "tank(s)", 5000, 3)
      elif recruitActivity == 3:
        recruitUnit2(TANKS_AMOUNT, TANKS_EXPENSE, TANKS_OIL_EXPENSE, "APC(s)", 3500, 2)
      elif recruitActivity == 4:
        recruitUnit(ARTIS_AMOUNT, ARTI_EXPENSE, "Aritillery batteries(y)", 4500)
      elif recruitActivity == 5:
        recruitUnit2(FIGHTERS_AMOUNT, FIGHTERS_EXPENSE, FIGHTERS_OIL_EXPENSE, "fighter(s)", 12000, 7)
      elif recruitActivity == 6:
        recruitUnit2(BOMBERS_AMOUNT, BOMBERS_EXPENSE, BOMBERS_OIL_EXPENSE, "bomber(s)", 50000, 25)
      elif recruitActivity == 7:
        carrierRecruit(STEALTH_JETS_AMOUNT, STEALTH_JETS_EXPENSE, STEALTH_JETS_AMOUNT, "stealth jet", 1000000, 75)
      elif recruitActivity == 8:
        recruitUnit2(TRANSPORT_JETS_AMOUNT, TRANSPORT_JETS_EXPENSE, TRANSPORT_JETS_OIL_EXPENSE, "transport jet(s)", 10000, 50)
      elif recruitActivity == 9:
        recruitUnit2(FRIGATE_AMOUNT, FRIGATE_EXPENSE, FRIGATE_OIL_EXPENSE, "frigate(s)", 75000, 15)
      elif recruitActivity == 10:
        recruitUnit2(DESTROYER_AMOUNT, DESTROYER_EXPENSE, DESTROYER_OIL_EXPENSE, "destroyer(s)", 100000, 35)
      elif recruitActivity == 11:
        recruitUnit2(BATTLESHIP_AMOUNT, BATTLESHIP_EXPENSE, BATTLESHIP_OIL_EXPENSE, "battleship(s)", 150000, 50)
      elif recruitActivity == 12:
        carrierRecruit(CARRIER_AMOUNT, CARRIER_EXPENSE, CARRIER_AMOUNT, "carrier", 500000, 120)
      elif recruitActivity > 12:
        print("Invalid input.")
    elif activity == 2:
      time.sleep(1)
      addDays()
      print("Your balance is as follows: ")
      checkBalance(TROOPS_EXPENSE, TROOPS_AMOUNT, "troop(s)")
      checkBalance2(TANKS_EXPENSE, TANKS_AMOUNT, TANKS_OIL_EXPENSE, "tank(s)")
      checkBalance2(APC_EXPENSE, APC_AMOUNT, APC_OIL_EXPENSE, "APC(s)")
      checkBalance(ARTI_EXPENSE, ARTIS_AMOUNT, "artillery battery(ies)")

      checkBalance2(FIGHTERS_EXPENSE, FIGHTERS_AMOUNT, FIGHTERS_OIL_EXPENSE, "fighter(s)")
      checkBalance2(BOMBERS_EXPENSE, BOMBERS_AMOUNT, BOMBERS_OIL_EXPENSE, "bomber(s)")
      checkBalance2(STEALTH_JETS_EXPENSE, STEALTH_JETS_AMOUNT, STEALTH_JETS_OIL_EXPENSE, "stealth jet(s)")
      checkBalance2(TRANSPORT_JETS_EXPENSE, TRANSPORT_JETS_AMOUNT, TRANSPORT_JETS_OIL_EXPENSE, "transport jet(s)")

      checkBalance2(FRIGATE_EXPENSE, FRIGATE_AMOUNT, FRIGATE_OIL_EXPENSE, "frigate(s)")
      checkBalance2(DESTROYER_EXPENSE, DESTROYER_AMOUNT, DESTROYER_OIL_EXPENSE, "destroyer(s)")
      checkBalance2(BATTLESHIP_EXPENSE, BATTLESHIP_AMOUNT, BATTLESHIP_OIL_EXPENSE, "battleship(s)")
      checkBalance2(CARRIER_EXPENSE, CARRIER_AMOUNT, CARRIER_OIL_EXPENSE, "aircraft carrier(s)")
    elif activity == 3:
      time.sleep(1)
      addDays()
      with open(TROOPS_AMOUNT, "r+") as troops:
        with open(TANKS_AMOUNT, "r+") as tanks:
          with open(APC_AMOUNT, "r+") as apcs:
            with open(ARTIS_AMOUNT, "r+") as artis:
              with open(FIGHTERS_AMOUNT, "r+") as fighters:
                with open(BOMBERS_AMOUNT, "r+") as bombers:
                  with open(STEALTH_JETS_AMOUNT, "r+") as stealthJets:
                    with open(TRANSPORT_JETS_AMOUNT, "r+") as transportJets:
                      with open(FRIGATE_AMOUNT, "r+") as frigates:
                        with open(DESTROYER_AMOUNT, "r+") as destroyers:
                          with open(BATTLESHIP_AMOUNT, "r+") as battleships:
                            with open(CARRIER_AMOUNT, "r+") as carriers:
                              troopCount = troops.read()
                              tankCount = tanks.read()
                              apcCount = apcs.read()
                              artisCount = artis.read()
                              fightersCount = fighters.read()
                              bombersCount = bombers.read()
                              stealthJetsCount = stealthJets.read()
                              transportJetsCount = transportJets.read()
                              frigatesCount = frigates.read()
                              destroyersCount = destroyers.read()
                              battleshipsCount = battleships.read()
                              carriersCount = carriers.read()
                              print(f"You currently have: \n{troopCount} troops \n{tankCount} tanks \n{apcCount} APCS \n{artisCount} artillitery batteries \n{fightersCount} fighters \n{bombersCount} bombers \n{stealthJetsCount} stealth jets \n{transportJetsCount} transport jets \n{frigatesCount} frigates \n{destroyersCount} destroyers \n{battleshipsCount} battleships \n{carriersCount} carriers")
                              print(f"Which unit would you like to fire?: (1 for troops, 2 for tanks, 3 for APCS, 4 for artillitery batteries, 5 for fighters, 6 for bombers etc.)")
                              fireAmount = int(input(">>> "))
                              if fireAmount == 1:
                                fireUnits(TROOPS_AMOUNT, TROOPS_EXPENSE, 'troop(s)', 1500)
                              elif fireAmount == 2:
                                fireUnits2(TANKS_AMOUNT, TANKS_EXPENSE, TANKS_OIL_EXPENSE, "tank(s)", 5000, 3)
                              elif fireAmount == 3:
                                fireUnits2(APC_AMOUNT, APC_EXPENSE, APC_OIL_EXPENSE, "APC(s)", 3500, 2)              
                              elif fireAmount == 4:
                                fireUnits(ARTIS_AMOUNT, ARTI_EXPENSE, 'artillery batteries(y)', 4500)
                              elif fireAmount == 5:
                                fireUnits2(FIGHTERS_AMOUNT, FIGHTERS_EXPENSE, FIGHTERS_OIL_EXPENSE, "fighter(s)", 12000, 7) 
                              elif fireAmount == 6:
                                fireUnits2(BOMBERS_AMOUNT, BOMBERS_EXPENSE, BOMBERS_OIL_EXPENSE, "bomber(s)", 50000, 25) 
                              elif fireAmount == 7:
                                fireUnits2(STEALTH_JETS_AMOUNT, STEALTH_JETS_EXPENSE, STEALTH_JETS_OIL_EXPENSE, "stealth jet(s)", 1000000, 75) 
                              elif fireAmount == 8:
                                fireUnits2(TRANSPORT_JETS_AMOUNT, TRANSPORT_JETS_EXPENSE, TRANSPORT_JETS_OIL_EXPENSE, "transport jet(s)", 100000, 50)
                              elif fireAmount == 9:
                                fireUnits2(FRIGATE_AMOUNT, FRIGATE_EXPENSE, FRIGATE_OIL_EXPENSE, "frigate(s)", 75000, 15)            
                              elif fireAmount == 10:
                                fireUnits2(DESTROYER_AMOUNT, DESTROYER_EXPENSE, DESTROYER_OIL_EXPENSE, "destroyer(s)", 100000, 35) 
                              elif fireAmount == 11:
                                fireUnits2(BATTLESHIP_AMOUNT, BATTLESHIP_EXPENSE, BATTLESHIP_OIL_EXPENSE, "battleship(s)", 150000, 50) 
                              elif fireAmount == 12:
                                fireUnits2(CARRIER_AMOUNT, CARRIER_EXPENSE, CARRIER_OIL_EXPENSE, "carrier(s)", 500000, 120) 
                              elif fireAmount > 12:
                                print("Invalid input.")
    elif activity == 4:
      addDays()
      print("Price of training: \nTroop - $3,000/week \nTank - $7,000/week \nAPC - $5,000/week \nArtillery Batteries - $6,000/week \nFighters - $25,000/week \nBombers - $75,000/week \nStealth Jets - $50,000 \nTransport Jets - $150,000 \nFrigates - $100,000 \nDestroyer - $125,000 \nBattleship - $200,000 \nCarrier - $150,000")
      time.sleep(1)
      print("1 to train TROOPS \n2 to train TANKS \n3 to train APCs \n4 to train ARTILLERY \n5 to train FIGHTERS \n6 to train BOMBERS \n7 to train STEALTH JETS \n8 to train TRANSPORT JETS \n9 to train FRIGATES \n10 to train DESTROYERS \n11 to train BATTLESHIPS \n12 to train CARRIERS")
      trainActivity = int(input(">>> "))
      if trainActivity == 1:
        print("For how many weeks would you like to train?")
        troopAmountInput = int(input(">>> "))
        if troopAmountInput <= 0:
          print(f"Can't train for {troopAmountInput}.")
        else:
          trainUnit("Troop", troopAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, TROOP_RANK, TROOPS_EXPENSE, 3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
          trainUnit("Troop", troopAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, TROOP_RANK, TROOPS_EXPENSE,  3000, TROOP_HEALTH, TROOP_AP, TROOP_DEFENSE, TROOP_SPEED)
      elif trainActivity == 2:
        print("For how many weeks would you like to train?")
        tankAmountInput = int(input(">>> "))
        if tankAmountInput <= 0:
          print(f"Can't train for {tankAmountInput}.")
        else:
          trainUnit("Tank", tankAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, TANK_RANK, TANKS_EXPENSE, 7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
          trainUnit("Tank", tankAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, TANK_RANK, TANKS_EXPENSE,  7000, TANK_HEALTH, TANK_AP, TANK_DEFENSE, TANK_SPEED)
      elif trainActivity == 3:
        print("For how many weeks would you like to train?")
        apcAmountInput = int(input(">>> "))
        if apcAmountInput <= 0:
          print(f"Can't train for {apcAmountInput}.")
        else:
          trainUnit("APC", apcAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, APC_RANK, APC_EXPENSE, 5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)
          trainUnit("APC", apcAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, APC_RANK, APC_EXPENSE,  5000, APC_HEALTH, APC_AP, APC_DEFENSE, APC_SPEED)  
      elif trainActivity == 4:
        print("For how many weeks would you like to train?")
        artiAmountInput = int(input(">>> "))
        if artiAmountInput <= 0:
          print(f"Can't train for {artiAmountInput}.")
        else:
          trainUnit("Artillery batteries", artiAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, ARTI_RANK, ARTI_EXPENSE, 6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)
          trainUnit("Artillery batteries", artiAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, ARTI_RANK, ARTI_EXPENSE,  6000, ARTI_HEALTH, ARTI_AP, ARTI_DEFENSE, ARTI_SPEED)  
      elif trainActivity == 5:
        print("For how many weeks would you like to train?")
        fighterAmountInput = int(input(">>> "))
        if fighterAmountInput <= 0:
          print(f"Can't train for {fighterAmountInput}.")
        else:
          trainUnit("Fighter", fighterAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, FIGHTER_RANK, FIGHTERS_EXPENSE, 25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED)
          trainUnit("Fighter", fighterAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, FIGHTER_RANK, FIGHTERS_EXPENSE,  25000, FIGHTER_HEALTH, FIGHTER_AP, FIGHTER_DEFENSE, FIGHTER_SPEED) 
      elif trainActivity == 6:
        print("For how many weeks would you like to train?")
        bomberAmountInput = int(input(">>> "))
        if bomberAmountInput <= 0:
          print(f"Can't train for {bomberAmountInput}.")
        else:
          trainUnit("Bomber", bomberAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, BOMBER_RANK, BOMBERS_EXPENSE, 75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED)
          trainUnit("Bomber", bomberAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, BOMBER_RANK, BOMBERS_EXPENSE,  75000, BOMBER_HEALTH, BOMBER_AP, BOMBER_DEFENSE, BOMBER_SPEED) 
      elif trainActivity == 7:
        print("For how many weeks would you like to train?")
        stealthAmountInput = int(input(">>> "))
        if stealthAmountInput <= 0:
          print(f"Can't train for {stealthAmountInput}.")
        else:
          trainUnit("Stealth Jet", stealthAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE, 50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
          trainUnit("Stealth Jet", stealthAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, STEALTH_JETS_RANK, STEALTH_JETS_EXPENSE,  50000, STEALTH_HEALTH, STEALTH_AP, STEALTH_DEFENSE, STEALTH_SPEED)
      elif trainActivity == 8:
        print("For how many weeks would you like to train?")
        transportAmountInput = int(input(">>> "))
        if transportAmountInput <= 0:
          print(f"Can't train for {transportAmountInput}.")
        else:
          trainUnit("Transport Jet", transportAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE, 150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)
          trainUnit("Transport Jet", transportAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, TRANSPORT_JETS_RANK, TRANSPORT_JETS_EXPENSE,  150000, TRANSPORT_HEALTH, TRANSPORT_AP, TRANSPORT_DEFENSE, TRANSPORT_SPEED)  
      elif trainActivity == 9:
        print("For how many weeks would you like to train?")
        frigateAmountInput = int(input(">>> "))
        if frigateAmountInput <= 0:
          print(f"Can't train for {frigateAmountInput}.")
        else:
          trainUnit("Frigate", frigateAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, FRIGATE_RANK, FRIGATE_EXPENSE, 100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)
          trainUnit("Frigate", frigateAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, FRIGATE_RANK, FRIGATE_EXPENSE,  100000, FRIGATE_HEALTH, FRIGATE_AP, FRIGATE_DEFENSE, FRIGATE_SPEED)  
      elif trainActivity == 10:
        print("For how many weeks would you like to train?")
        destroyerAmountInput = int(input(">>> "))
        if destroyerAmountInput <= 0:
          print(f"Can't train for {destroyerAmountInput}.")
        else:
          trainUnit("Destroyer", destroyerAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, DESTROYER_RANK, DESTROYER_EXPENSE, 125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED)
          trainUnit("Destroyer", destroyerAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, DESTROYER_RANK, DESTROYER_EXPENSE,  125000, DESTROYER_HEALTH, DESTROYER_AP, DESTROYER_DEFENSE, DESTROYER_SPEED) 
      elif trainActivity == 11:
        print("For how many weeks would you like to train?")
        battleshipAmountInput = int(input(">>> "))
        if battleshipAmountInput <= 0:
          print(f"Can't train for {battleshipAmountInput}.")
        else:
          trainUnit("Battleship", battleshipAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, BATTLESHIP_RANK, BATTLESHIP_EXPENSE, 200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED)
          trainUnit("Battleship", battleshipAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, BATTLESHIP_RANK, BATTLESHIP_EXPENSE,  200000, BATTLESHIP_HEALTH, BATTLESHIP_AP, BATTLESHIP_DEFENSE, BATTLESHIP_SPEED) 
      elif trainActivity == 12:
        print("For how many weeks would you like to train?")
        carrierAmountInput = int(input(">>> "))
        if carrierAmountInput <= 0:
          print(f"Can't train for {carrierAmountInput}.")
        else:
          trainUnit("Aircraft Carrier", carrierAmountInput, 0, 2, "Level-1", 5, 5, 5, 5, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 2, 4, "Level-2", 10, 10, 10, 10, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 4, 6, "Level-3", 15, 15, 15, 15, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 6, 8, "Level-4", 20, 20, 20, 20, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 8, 10, "Level-5", 25, 25, 25, 25, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 10, 12, "Level-6", 30, 30, 30, 30, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 12, 14, "Level-7", 35, 35, 35, 35, CARRIER_RANK, CARRIER_EXPENSE, 150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED)
          trainUnit("Aircraft Carrier", carrierAmountInput, 16, 18, "Level-8", 40, 40, 40, 40, CARRIER_RANK, CARRIER_EXPENSE,  150000, CARRIER_HEALTH, CARRIER_AP, CARRIER_DEFENSE, CARRIER_SPEED) 
    elif activity == 5:
      addDays()
      time.sleep(1)
      print("List of generals for hire: ")
      print(f"1 for {GENERAL_1_NAME} \n2 for {GENERAL_2_NAME} \n3 for {GENERAL_3_NAME} \n4 for {GENERAL_4_NAME} \n5 for {GENERAL_5_NAME} \n6 for {GENERAL_6_NAME}")
      generalSelection = int(input(">>> "))
      if generalSelection == 1:
        hireGeneral(GENERAL_1_NAME, GENERAL_1_STRENGHT, GENERAL_1_TRAIT, GENERAL_1_PRICE, GENERAL_1_SALARY)
      elif generalSelection == 2:
        hireGeneral(GENERAL_2_NAME, GENERAL_2_STRENGHT, GENERAL_2_TRAIT, GENERAL_2_PRICE, GENERAL_2_SALARY)
      elif generalSelection == 3:
        hireGeneral(GENERAL_3_NAME, GENERAL_3_STRENGHT, GENERAL_3_TRAIT, GENERAL_3_PRICE, GENERAL_3_SALARY)
      elif generalSelection == 4:
        hireGeneral(GENERAL_4_NAME, GENERAL_4_STRENGHT, GENERAL_4_TRAIT, GENERAL_4_PRICE, GENERAL_4_SALARY)
      elif generalSelection == 5:
        hireGeneral(GENERAL_5_NAME, GENERAL_5_STRENGHT, GENERAL_5_TRAIT, GENERAL_5_PRICE, GENERAL_5_SALARY)
      elif generalSelection == 6:
        hireGeneral(GENERAL_6_NAME, GENERAL_6_STRENGHT, GENERAL_6_TRAIT, GENERAL_6_PRICE, GENERAL_6_SALARY)
      elif generalSelection > 6:
        print("Invalid input.")
    elif activity == 6:
      addDays()
      with open(GENERAL_1_SALARY, "r+") as SALARY_1:
        with open(GENERAL_2_SALARY, "r+") as SALARY_2:
          with open(GENERAL_3_SALARY, "r+") as SALARY_3:
            with open(GENERAL_4_SALARY, "r+") as SALARY_4:
              with open(GENERAL_5_SALARY, "r+") as SALARY_5:
                with open(GENERAL_6_SALARY, "r+") as SALARY_6:

                  general1Salary = int(SALARY_1.read())
                  general2Salary = int(SALARY_2.read())
                  general3Salary = int(SALARY_3.read())
                  general4Salary = int(SALARY_4.read())
                  general5Salary = int(SALARY_5.read())
                  general6Salary = int(SALARY_6.read())

                  print("Your hired generals: ")
                  checkGeneral(general1Salary, GENERAL_1_NAME)
                  checkGeneral(general2Salary, GENERAL_2_NAME)
                  checkGeneral(general3Salary, GENERAL_3_NAME)
                  checkGeneral(general4Salary, GENERAL_4_NAME)
                  checkGeneral(general5Salary, GENERAL_5_NAME)
                  checkGeneral(general6Salary, GENERAL_6_NAME)

                  print("1 to view your general's salaries \n2 to view your general's stats \n3 to fire your generals")
                  generalChoice = int(input(">>> "))
                  if generalChoice == 1:
                    print("Your general's salaries are as follows: ")
                    checkSalary(general1Salary, GENERAL_1_NAME)
                    checkSalary(general2Salary, GENERAL_2_NAME)
                    checkSalary(general3Salary, GENERAL_3_NAME)
                    checkSalary(general4Salary, GENERAL_4_NAME)
                    checkSalary(general5Salary, GENERAL_5_NAME)
                    checkSalary(general6Salary, GENERAL_6_NAME)
                  elif generalChoice == 2:
                    print("Your general's stats are as follows: ")
                    checkStats(general1Salary, GENERAL_1_RANK, GENERAL_1_NAME, GENERAL_1_TRAIT, GENERAL_1_STRENGHT)
                    checkStats(general2Salary, GENERAL_2_RANK, GENERAL_2_NAME, GENERAL_2_TRAIT, GENERAL_2_STRENGHT)
                    checkStats(general3Salary, GENERAL_3_RANK, GENERAL_3_NAME, GENERAL_3_TRAIT, GENERAL_3_STRENGHT)
                    checkStats(general4Salary, GENERAL_4_RANK, GENERAL_4_NAME, GENERAL_4_TRAIT, GENERAL_4_STRENGHT)
                    checkStats(general5Salary, GENERAL_5_RANK, GENERAL_5_NAME, GENERAL_5_TRAIT, GENERAL_5_STRENGHT)
                    checkStats(general6Salary, GENERAL_6_RANK, GENERAL_6_NAME, GENERAL_6_TRAIT, GENERAL_6_STRENGHT)
                  elif generalChoice == 3:
                    print("Which one of your general's would you like to fire?")
                    checkName(general1Salary, GENERAL_1_NAME)
                    checkName(general2Salary, GENERAL_2_NAME)
                    checkName(general3Salary, GENERAL_3_NAME)
                    checkName(general4Salary, GENERAL_4_NAME)
                    checkName(general5Salary, GENERAL_5_NAME)
                    checkName(general6Salary, GENERAL_6_NAME)
                    print("(Enter the index of the general, e.g. if you want to fire the first general, you would enter '1')")
                    generalFireInput = int(input(">>> "))
                    if generalFireInput == 1:
                      fireGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, GENERAL_1_NAME)
                    elif generalFireInput == 2:
                      fireGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, GENERAL_2_NAME)
                    elif generalFireInput == 3:
                      fireGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, GENERAL_3_NAME)
                    elif generalFireInput == 4:
                      fireGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, GENERAL_4_NAME)
                    elif generalFireInput == 5:
                      fireGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, GENERAL_5_NAME)
                    elif generalFireInput == 6:
                      fireGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, GENERAL_6_NAME)
                    elif generalFireInput > 6:
                      print("Invalid input.")
                  elif generalChoice > 4:
                    print("Invalid input.")
    elif activity == 7:
      addDays()
      print("Your generals: ")
      checkName(general1Salary, GENERAL_1_NAME)
      checkName(general2Salary, GENERAL_2_NAME)
      checkName(general3Salary, GENERAL_3_NAME)
      checkName(general4Salary, GENERAL_4_NAME)
      checkName(general5Salary, GENERAL_5_NAME)
      checkName(general6Salary, GENERAL_6_NAME)
      print("(Enter the index of the general, e.g. if you want to train the first general, you would enter '1')")
      generalTrainInput = int(input(">>> "))
      if generalTrainInput == 1:
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 0, 2, GENERAL_1_STRENGHT, 5, "Field Marshal", 7500, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 2, 4, GENERAL_1_STRENGHT, 10, "Commander", 10000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 4, 6, GENERAL_1_STRENGHT, 15, "Defense Minister", 15000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 6, 8, GENERAL_1_STRENGHT, 20, "Colonel", 16000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 8, 9, GENERAL_1_STRENGHT, 25, "Lieutenant", 17000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 9, 10, GENERAL_1_STRENGHT, 30, "Lieutenant Major", 18000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 10, 12, GENERAL_1_STRENGHT, 45, "Supreme Commander", 25000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 12, 14, GENERAL_1_STRENGHT, 50, "Supreme Commander of the Armed Forces", 30000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 16, 18, GENERAL_1_STRENGHT, 50, "Supreme Warlord of the Armored Vanguard", 35000, GENERAL_1_NAME)
        trainGeneral(GENERAL_1_RANK, GENERAL_1_SALARY, 20, 25, GENERAL_1_STRENGHT, 50, "Destroumenous, The one feared by god", 50000, GENERAL_1_NAME)
      elif generalTrainInput == 2:
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 0, 2, GENERAL_2_STRENGHT, 5, "Field Marshal", 7500, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 2, 4, GENERAL_2_STRENGHT, 10, "Commander", 10000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 4, 6, GENERAL_2_STRENGHT, 15, "Defense Minister", 15000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 6, 8, GENERAL_2_STRENGHT, 20, "Colonel", 16000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 8, 9, GENERAL_2_STRENGHT, 25, "Lieutenant", 17000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 9, 10, GENERAL_2_STRENGHT, 30, "Lieutenant Major", 18000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 10, 12, GENERAL_2_STRENGHT, 45, "Supreme Commander", 25000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 12, 14, GENERAL_2_STRENGHT, 50, "Supreme Commander of the Armed Forces", 30000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 16, 18, GENERAL_2_STRENGHT, 50, "Supreme Warlord of the Armored Vanguard", 35000, GENERAL_2_NAME)
        trainGeneral(GENERAL_2_RANK, GENERAL_2_SALARY, 20, 25, GENERAL_2_STRENGHT, 50, "Destroumenous, The one feared by god", 50000, GENERAL_2_NAME)
      elif generalTrainInput == 3:
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 0, 2, GENERAL_3_STRENGHT, 5, "First Lieutenant", 7500, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 2, 4, GENERAL_3_STRENGHT, 10, "Commander", 10000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 4, 6, GENERAL_3_STRENGHT, 15, "Second Lieutenant", 15000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 6, 8, GENERAL_3_STRENGHT, 20, "Flight Lieutenant", 16000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 8, 9, GENERAL_3_STRENGHT, 25, "Colonel", 17000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 9, 10, GENERAL_3_STRENGHT, 30, "Lieutenant Colonel", 18000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 10, 12, GENERAL_3_STRENGHT, 45, "Air Marshal", 25000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 12, 14, GENERAL_3_STRENGHT, 50, "Supreme Commander of the Flying Forces", 30000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 16, 18, GENERAL_3_STRENGHT, 50, "Supreme Marshal of the Air Force", 35000, GENERAL_3_NAME)
        trainGeneral(GENERAL_3_RANK, GENERAL_3_SALARY, 20, 25, GENERAL_3_STRENGHT, 50, "Retronmonisouslremoin-III, The one who flew to the heavens.", 50000, GENERAL_3_NAME)
      elif generalTrainInput == 4:
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 0, 2, GENERAL_4_STRENGHT, 5, "Sub-Lieutenant", 7500, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 2, 4, GENERAL_4_STRENGHT, 10, "Lieutenant", 10000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 4, 6, GENERAL_4_STRENGHT, 15, "Lieutenant Commander", 15000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 6, 8, GENERAL_4_STRENGHT, 20, "Petty Officer", 16000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 8, 9, GENERAL_4_STRENGHT, 25, "Warrant Officer", 17000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 9, 10, GENERAL_4_STRENGHT, 30, "Chief Warrant Officer", 18000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 10, 12, GENERAL_4_STRENGHT, 45, "Admiral", 25000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 12, 14, GENERAL_4_STRENGHT, 50, "Supreme commander of the Sailing Forces", 30000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 16, 18, GENERAL_4_STRENGHT, 50, "The murderer of the Kraken", 35000, GENERAL_4_NAME)
        trainGeneral(GENERAL_4_RANK, GENERAL_4_SALARY, 20, 25, GENERAL_4_STRENGHT, 50, "Krakenmanstakipolsvaski-III, The one who swam to hell itself.", 50000, GENERAL_4_NAME)
      elif generalTrainInput == 5:
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 0, 2, GENERAL_5_STRENGHT, 5, "Sub-Lieutenant", 7500, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 2, 4, GENERAL_5_STRENGHT, 10, "Lieutenant", 10000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 4, 6, GENERAL_5_STRENGHT, 15, "Lieutenant Commander", 15000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 6, 8, GENERAL_5_STRENGHT, 20, "Petty Officer", 16000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 8, 9, GENERAL_5_STRENGHT, 25, "Warrant Officer", 17000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 9, 10, GENERAL_5_STRENGHT, 30, "Chief Warrant Officer", 18000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 10, 12, GENERAL_5_STRENGHT, 45, "Admiral", 25000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 12, 14, GENERAL_5_STRENGHT, 50, "Supreme commander of the Sailing Forces", 30000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 16, 18, GENERAL_5_STRENGHT, 50, "The murderer of the Kraken", 35000, GENERAL_5_NAME)
        trainGeneral(GENERAL_5_RANK, GENERAL_5_SALARY, 20, 25, GENERAL_5_STRENGHT, 50, "Krakenmanstakipolsvaski-III, The one who swam to hell itself.", 50000, GENERAL_5_NAME)
      elif generalTrainInput == 6:
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 0, 2, GENERAL_6_STRENGHT, 5, "Sub-Lieutenant", 7500, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 2, 4, GENERAL_6_STRENGHT, 10, "Lieutenant", 10000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 4, 6, GENERAL_6_STRENGHT, 15, "Lieutenant Commander", 15000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 6, 8, GENERAL_6_STRENGHT, 20, "Petty Officer", 16000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 8, 9, GENERAL_6_STRENGHT, 25, "Warrant Officer", 17000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 9, 10, GENERAL_6_STRENGHT, 30, "Chief Warrant Officer", 18000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 10, 12, GENERAL_6_STRENGHT, 45, "Admiral", 25000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 12, 14, GENERAL_6_STRENGHT, 50, "Supreme commander of the Sailing Forces", 30000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 16, 18, GENERAL_6_STRENGHT, 50, "The murderer of the Kraken", 35000, GENERAL_6_NAME)
        trainGeneral(GENERAL_6_RANK, GENERAL_6_SALARY, 20, 25, GENERAL_6_STRENGHT, 50, "Krakenmanstakipolsvaski-III, The one who swam to hell itself.", 50000, GENERAL_6_NAME)
      elif generalTrainInput > 6:
        print("Invalid range entered.")
    elif activity == 8:
      addDays()
      print("Here are the buildings you can build: ")
      print("VEHICLE FACTORY - $15,000 \nBARRACKS - $25,000 \nAIRBASE - $50,000 \nBANK - $100,000 \nCOMMAND CENTER - $150,000 \OIL REFINERY - $75,000")
      print("1 for VEHICLE FACTORY \n2 for BARRACKS \n3 for AIRBASE \n4 for BANK \n5 for COMMAND CENTER \n6 for OIL REFINERY")
      buildingInput = int(input(">>> "))
      if buildingInput == 1:
        print("How many VEHICLE FACTORIES do you want to build?")
        vFactoryInput = int(input(">>> "))
        if vFactoryInput <= 0:
          print(f"Can't build {vFactoryInput} vehicle factories.")
        else: 
          buildBuilding(vFactoryInput, "Vehicle Factory(ies)", VEHICLE_FACTORY, 15000)
          updateCapacity(vFactoryInput, 15)
      elif buildingInput == 2:
        print("How many BARRACKS do you want to build?")
        barracksInput = int(input(">>> "))
        if barracksInput <= 0:
          print(f"Can't build {barracksInput} vehicle factories.")
        else: 
          buildBuilding(barracksInput, "Barrack(s)", BARRACKS, 25000)
          updateCapacity(barracksInput, 25)
      elif buildingInput == 3:
        print("How many AIRBASE(S) do you want to build?")
        airbaseInput = int(input(">>> "))
        if airbaseInput <= 0:
          print(f"Can't build {airbaseInput} airbase(s).")
        else: 
          buildBuilding(airbaseInput, "Airbase(s)", AIRBASE, 50000)
          updateCapacity(airbaseInput, 10)
      elif buildingInput == 4:
        print("How many BANK(S) do you want to build?")
        bankInput = int(input(">>> "))
        if bankInput <= 0:
          print(f"Can't build {bankInput} bank(s).")
        else: 
          buildBuilding(bankInput, "bank(s)", BANK, 100000)
          updateMoney(150000)
      elif buildingInput == 5:
        with open(COMM_CENTER, "r+") as commCenter:
          prevCommCenters = int(commCenter.read())
          if prevCommCenters == 0:
              buildBuilding(1, "Command Center(s)", COMM_CENTER, 150000)
              updateStats(25)
          elif prevCommCenters == 1:
            print("Can't built another command center")
      elif buildingInput == 6:
        print("How many OIL REFINERIY(ES) do you want to build?")
        oilInput = int(input(">>> "))
        if oilInput <= 0:
          print(f"Can't build {oilInput} oil refineries(s).")
        else: 
          buildBuilding(oilInput, "oil refineries(s)", POWER_PLANT, 75000)
          updateOil(oilInput)
    elif activity == 9:
      with open(AIRBASE, "r+") as airbase:
        with open(BANK, "r+") as bank:
          with open(BARRACKS, "r+") as barracks:
            with open(COMM_CENTER, "r+") as commCenter:
              with open(POWER_PLANT, "r+") as powerPlant:
                with open(VEHICLE_FACTORY, "r+") as vehicleFact:
                  airbaseCount = int(airbase.read())
                  bankCount = int(bank.read())
                  barracksCount = int(barracks.read())
                  commCenterCount = int(commCenter.read())
                  oilRefineryCount = int(powerPlant.read())
                  vehicleFactCount = int(vehicleFact.read())
                  print("You have the following buildings: ")
                  print(f"Airbases: {airbaseCount} \nBank: {bankCount} \nBarracks: {barracksCount} \nCommand Center: {commCenterCount} \nOil refinery: {oilRefineryCount} \nVehicle Factories: {vehicleFactCount}")
                  print("You can do the following things: ")
                  print("1 to DESTROY BUILDINGS \n2 to VIEW BUILDING'S INCOME \n3 to UPGRADE BUILDINGS")
                  buildingActivity = int(input(">>> "))
                  if buildingActivity == 1:
                    print("1 to destroy AIRBASE \n2 to destroy BANK \n3 to destroy BARRACKS \n4 to destroy COMMAND CENTER \n5 to destroy OIL REFINERIES \n6 to destroy VEHICLE FACTORIES")  
                    destructionActivity = int(input(">>> "))
                    if destructionActivity == 1:
                      print("How many AIRBASES do you want to destroy?")
                      airbaseDestructionAmount = int(input(">>> "))
                      if airbaseDestructionAmount <= 0:
                        print(f"Can't destroy {airbaseDestructionAmount} AIRBASES.")
                      elif airbaseDestructionAmount > airbaseCount:
                        print(f"Can't destroy more AIRBASES than you have.")
                      else:
                        print(f"Destroyed {airbaseDestructionAmount} AIRBASES")
                        print(f"Added ${50000 * airbaseDestructionAmount} to your bank.")

for i in range(7):
  main()
