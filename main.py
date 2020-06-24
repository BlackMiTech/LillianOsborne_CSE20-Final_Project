# -*- coding:utf-8 -*-
# --- Version:0.0.6--- #
'''
Title: Kingdom & Unions War.
Author:Jimmy Wang
Date: June 19th,2020
'''

start = True

import time
import random

Enemy_bot = ["Jason" , "Jimmy", "Aaron", "Charlie", "Annie"]

union = ["[Berserker]","[Forest Archer]","[Knight of light]","[Solitary swordsman]","[Fighting master]","[Bullet expert]"]
Kingdoms = ["[Fight Nec]","[Dark Archer]","[Skeleton Knight]","[Bloodthirsty swordsman]","[Chief Assassin]","[The king of traps]"]

# Define weapon
AK47 = 0
Hemostatic = 0
Balisong = 0
Hemostatic_num = 0

# Randomly select 3 elements in the list to generate a list
My_teams = random.sample(union,3)
Enemy = random.sample(Enemy_bot, 1) #randomly choose 1 name from the list
enemy_teams = random.sample(Kingdoms,3)
attribute_01 = {}
attribute_02 = {}

def attribute_user():                 #random the attribute
    user_Blood = random.randint(100, 180)
    user_aggressivity = random.randint(30, 50)
    return user_Blood,user_aggressivity

def attribute_computer():             #define(_ , _)2 value [A tuple]
    enemy_Blood = random.randint(100, 180)
    enemy_aggressivity = random.randint(30, 50)
    return enemy_Blood,enemy_aggressivity

def chooseteam():                      #Add key and tuple to dictionary
    for i in range(3):
        attribute_01[My_teams[i]] = attribute_user()
        attribute_02[enemy_teams[i]] = attribute_computer()

    print("----------------- Characters_Info -----------------")
    print("Your Character：")

    for i in range(3):
        print(" {} Remaining Blood:{} Aggressivity:{}".format(My_teams[i],attribute_01[My_teams[i]][0],attribute_01[My_teams[i]][1]))
    print("--------------------------------------------")
    print("Enemy Character：")
    for i in range(3):
        print(" {} Remaining Blood:{} Aggressivity:{}".format(enemy_teams[i],attribute_02[enemy_teams[i]][0],attribute_02[enemy_teams[i]][1]))
    print("--------------------------------------------")

def Order_My_teams_new():
    print("""-------Please adjust your order--------""")
    global My_teams  # Global becomes a global variable
    My_teams_order = {}     # Create a new list
    for i in range(3):      # Add a new order to the list
        order_01 = int(input("Which number would you like to put {} in?（Please enter 1,2 or 3)".format(My_teams[i])))
        My_teams_order[order_01] = My_teams[i]             ##{2: "[Berserker]", 1: "[Fighting master]", 3: "[Forest Archer]"}#
    My_teams = []           #Clear original list
    for i in range(1,4):
        My_teams.append(My_teams_order[i])      # Reorder the list
    print("The order of our character is{}".format(My_teams))
    print("The order of enemy is{}".format(enemy_teams))

# Check number if it is int
def checkNumberInt(value):
    if value.isnumeric():
        return int(value)
    else:
        print("You did not enter the correct numbers!")
        newNum = input("Please enter a number again:")
        return checkNumberInt(newNum)

def game_start():                 #2 wins
    for i in range(3): # Total 3 games
        scores = 0
        user_Blood = attribute_01[My_teams[i]][0]
        enemy_Blood = attribute_02[enemy_teams[i]][0]
        user_aggressivity = attribute_01[My_teams[i]][1]
        enemy_aggressivity = attribute_02[enemy_teams[i]][1]
        if AK47 == 1 and Balisong == 0:
            user_aggressivity = user_aggressivity + 13
            user_Blood = user_Blood - 10
            enemy_Blood = enemy_Blood + 2
            print("You now have equipment your AK-47, your aggressivity has proved to", user_aggressivity,"\n also your enemy blood has proved to", enemy_Blood)
        elif Balisong == 1 and AK47 == 0:
            user_aggressivity = user_aggressivity + 20
            user_Blood = user_Blood - 15
            enemy_aggressivity = enemy_aggressivity + 2
            print("You now have equipment your Balisong, your aggressivity has proved to", user_aggressivity,".\n Also your enemy blood has proved to", enemy_Blood)
        elif Balisong == 1 and AK47 == 1:
            user_aggressivity = user_aggressivity + 60
            user_Blood = user_Blood - 40
            enemy_aggressivity = enemy_aggressivity + 5
            print("You now have equipment your Balisong and AK-47, your aggressivity has proved to", user_aggressivity,
                  "\n also your enemy blood has proved to", enemy_Blood)
        print("===================================The {} Game============================================".format(i+1))
        print("==Our_characters======Enemy_characters==")
        print(" {}  VS  {} ".format(My_teams[i],enemy_teams[i]))
        print("Blood:{}                Blood:{}".format(attribute_01[My_teams[i]][0],attribute_02[enemy_teams[i]][0]))
        print("Aggressivity:{}         Aggressivity:{}".format(attribute_01[My_teams[i]][1],attribute_02[enemy_teams[i]][1]))
        input("----------------------------Press_Enter_To_Continue----------------------------")
        while user_Blood > 0 and enemy_Blood > 0:
            user_Blood = user_Blood - enemy_aggressivity
            enemy_Blood = enemy_Blood - user_aggressivity
            print("You start to attack，[Enemy] remaining blood volume is:{}".format (enemy_Blood))
            print("The enemy start to attacked you，Your team Blood remaining:{}".format (user_Blood))
            time.sleep(1)

        if user_Blood > 0 and enemy_Blood <= 0:
            scores = scores + 1
            print("Victory!You have defeated your enemy!")

        elif user_Blood <= 0 and enemy_Blood > 0:
            if Hemostatic_num > 0:
                print("""
                Do you want to use your Hemostatic agent? It will give you 35 volumes of blood.
                Press 1 to use
                Or
                You can enter 2 without blood medicine
                """)
                use_hemostatic = checkNumberInt(input(" >"))
                if use_hemostatic == int("1"):
                    user_Blood = user_Blood + 35 # add 35 blood
                    enemy_aggressivity = enemy_aggressivity + 10 # For balancing, the enemy aggressivity will add 10
                if use_hemostatic == int("2"):
                    scores = scores - 1
                    print("Sorry，The enemy has defeated you!")

            else:
                scores = scores - 1
                print("Sorry，The enemy has defeated you!")
                gold = gold - randomgold_lose
        else:
            print("Oh, you and the enemy have died together!")
        print("-----------------------")

    if scores > 0:
        print("{} wins in three games, you won!!!".format(scores+1))
        gold = gold + randomgold_win
    elif scores < 0:
        print("{} wins in three games, you lost!!!".format(scores+1))
        gold = gold - randomgold_lose
    else:
        gold = gold + randomgold
        print("It was tie!")

# ---Ends---#
def endProgram():
    pause = input("Enter exit to exit or press ENTER to restart. >")
    if pause == str("exit"):
        exit()
    else:
        print("-------------------------------------------")
    return

name = input("Please input your name:")
randomgold = random.randint(5, 500)
randomgold_win = random.randint(200, 500)
randomgold_lose = random.randint(50, 200)

# --- ONLY FOR TEST---#
if name == str("test"):
    gold = 1000000000000000 # test
    AK47 = 1
    Hemostatic = 1
    Balisong = 1
    Hemostatic_num = 99999999
    age = -1
else:
    age = input("{},please input your age: ".format(name))
    user_info = {"name": name, "age": int(age)}  # User Information
    # Give different initial gold coins according to user's age
    if 10 < user_info['age'] < 18:
        gold = 1000 + randomgold
    elif 18 <= user_info['age'] <= 30:
        gold = 1500 + randomgold
    else:
        gold = 500 + randomgold
    user_info['gold'] = gold


# --- Program Start --- #
while start:
    start = False
    print("Welcome to Kingdom & Unions War.")
    print("Hello,", name, " welcome to play this game.\n")
    print("Your initial gold coins are:", gold)
    print("\n")
    time.sleep(1)
    print("-------------------------------------------")
    print("Game Description")
    print("The system will automatically select three characters for you and fight against the evil enemies.")
    print("-------------------------------------------")
    print("Tips: go to the stores buy some weapons!")
    print("""
    1. Enter in the Game.
    2. Settings
    3. Stores
    4. Coming Soon...
    """)
    mode = checkNumberInt(input("> "))
    # --- Game Start --- #
    if mode == int("1"):
        chooseteam()
        Order_My_teams_new()
        game_start()
        start = True
        endProgram()
    elif mode == int("2"):
        print("""
        1. Account information
        2. Change your profile
        3. Stock
        """)
        mode_01 = checkNumberInt(input("> "))
        if mode_01 == int("1"):
            print("--------------------------")
            print("Hello,", name)
            print("Your current balance is:", gold)
            print("""
            Enter "1" to recharge your account.
            Or 
            Enter anything to back into Menu
            """)
            charge = checkNumberInt(input("> "))
            if charge == str("1"):
                print("-------------------------------------")
                print("This function has not been added yet.")
                print("-------------------------------------")
                start = True
                endProgram()
            elif charge == int("568052318"): # test for the balance
                gold = gold + 100000000
                print("Charge successfully, your remain balance is:", gold)
                start = True
                endProgram()
            else:
                start = True
                endProgram()
        elif mode_01 == int("2"):
            print("--------------------------")
            print("Hello,", name)
            print("""
            1. Change your name
            2. Coming soon...
            """)
            change_profile = checkNumberInt(input("> "))
            if change_profile == int(1):
                if name == str("test"):
                    print("You can not change test name!")
                    start = True
                    endProgram()
                else:
                    name = input("Please input your new name >")
                    start = True
                    endProgram()
            else:
                start = True
                endProgram()
        elif mode_01 == int("3"):
            print("--------------------------")
            print("Hello,", name)
            print("You now have:")
            if AK47 == 1:
                print("AK-47 Full-automatic Rifle")
            if Balisong == 1:
                print("Balisong(Butterfly knife)")
            if Hemostatic == 1:
                print("Hemostatic agent x", Hemostatic_num)
            start = True
            endProgram()
    elif mode == int("3"):
        print("--------------------------")
        print("Hello,", name, "welcome to the BLACK Store.")
        print("Balance:", gold)
        print("""
        1. Balisong(Butterfly Knife) 400$ (Butterfly Knife)
        2. AK-47 Full-automatic Rifle 3000$
        3. Hemostatic agent x1 58$
        """)
        store_buy = checkNumberInt(input("> "))
        if store_buy == int("1"):
            if Balisong == 0: # Check if weapon is valid
                gold = gold - 400
                if gold <= 0:
                    print("Your account balance is not enough to buy this!")
                    gold = gold + 400 # If balance is not enough, then add the gold back
                else:
                    print("Successfully,Your remaining balance is:", gold)
                    Balisong = 1
                    start = True
                    endProgram()
            else:
                print("You already have Balisong(Butterfly Knife)!")
                start = True
                endProgram()
        if store_buy == int("2"):
            if AK47 == 0:   # if ak is not in stock, then buy it
                gold = gold - 3000
                if gold <= 0:
                    print("Your account balance is not enough to buy this!")
                    gold = gold + 3000
                    start = True
                    endProgram()
                else:
                    print("Successfully,Your remaining balance is:", gold)
                    AK47 = 1
                    start = True
                    endProgram()
            else:
                print("You already have AK-47 Full-automatic Rifle!")
                start = True
                endProgram()
        if store_buy == int("3"):
            print("How Much You Want To Buy?")
            Hemostatic_buy_num = checkNumberInt(input(" >"))
            gold = gold - 58 * Hemostatic_buy_num
            if gold <= 0:
                print("Your account balance is not enough to buy this!")
                gold = gold + 58 * Hemostatic_buy_num  # If balance is not enough, then add the gold back
                start = True
                endProgram()
            else:
                print("Successfully,Your remaining balance is:", gold)
                print("You now have", Hemostatic_num,"Hemostatic Agent")
                Hemostatic = 1
                Hemostatic_num = Hemostatic_num + Hemostatic_buy_num
                start = True
                endProgram()
    else:
        print("Please choose a valid number")
        start = True
        endProgram()