import random
text_file=open("Endings.txt", "w")
print("Disclamer: This is a demo asuch all gameplay is subject to change")
print("")
print("")
print("Long ago in the anccent land of Bepreocia, there lived a grand king")
print("who ruled over a kingdom that had stood for hundreds of years.")
print("The king grew old while ruling his kingdom and was eventaly bed ridden")
print("the eldest son of the king stepped forth and took the crown in place")
print("of the king. The prince soon learnt of the troubles of ruling such a")
print("large kingdom and he turned to his farther for help, but the king had")
print("become too ill to have visiters. The prince started to reaserch differnt")
print("methods of healing and stumbled upon a legend, of the imortal goblet.")
print("The prince knew this could save his farther and called for you, his greatest")
print("knight, to retrive the goblet and save the kingdom.")
armour=1
attack=2
co=0
print("Please sir knight tell me your name?")
name=input("")
print("Arise", name, "and tell me will you accept the challenge.")
print("1. Yes")
print("2. No")
print("3. Swear at him")
accept=input("")
if accept=="1":
    print("Oh great knight thank you. Please retreve the goblet with posthaste!")
    print("Take these 50 gold to help you")
    gold=50
    hp=10
    good=0
    greed=0
    useless=0
elif accept=="2":
    print("A pity I was told you were the best, but it seems that pride bilds you")
    quit()
else:
    print("How dare you speak to your king in that way, guards!")
    quit()
print("Your travels begin and soon after leaving the walls of the city you arive")
print("at a forest. You proced forward and find an old woman laying in a clearing.")
print("You note that you can hear her crying. Will you help her?")
print("1. Yes")
print("2. No")
print("3. Shoot her with an arrow")
help_1=input("")
if help_1=="1":
    print("The woman hold a knife to your throat and reveals they are a man in disguise")
    print("the man slits your throat and you perish.")
    quit()
elif help_1=="2":
    print("You continue onwards on your quest. To avoid the woman was a great idea")
    print("after all you remeber hearing that canibles in disguses live in these woods.")
else:
    arrow=(random.randint(0, 1))
    if arrow==(1):
        print("You pull out your bow but before you can shoot an arrow hits you in your")
        print("neck killing you instantly.")
        quit()
    else:
        print("You fire an arrow but miss. The woman turns around revieling them to be")
        print("a man in disguise. Fearing for the worst you ride off to continue your quest.")
print("After traveling on a road for a few minutes you arive at a split in the road.")
while_1=0
while while_1==0:
    print("You can travel down the first road or the second or you can head back.")
    print("1. First road")
    print("2. Second road")
    print("3. Headback")
    road_1=input("")
    if road_1=="1":
        print("You take the first road and come to a an empty town. You walk around searching for any")
        print("sign of life but there is non")
        print("do you wish to spend the night here")
        print("1. Yes")
        print("2. No")
        camp_1=input("")
        if camp_1=="1":
            print("You go into one of the abandomed houses and sleep in the bed, leaving your stead outside.")
            print("During the night you here voices do you investigate?")
            print("1. Yes")
            print("2. No")
            check_1=input("")
            if check_1=="1":
                print("You go out of the house and find a group of people chanting in a circle one them spots you and")
                print("starts to screach at you, alerting the others. The all turn to face you and as you draw your sword")
                print("a ball of fire hits you and boils you in your armour.")
                quit()
            else:
                print("You continue to rest in peace and wake up well rested the next morning, and headback to the split in the road.")
                bridge_1=1
        else:
            print("You return to the split in the road.")
            print("You can travel down the first road or the second road or you can head back.")
            print("1. *Locked*")
            print("2. Second road")
            print("3. Headback")
            road_2=input("")
            if road_2=="2":
                print("You come across the remains of a bridge.")
                print("Do you wish to travel swim through the river")
                print("1. Yes")
                print("2. No")
                print("3. Call for help")
                river_1=input("")
                if river_1=="1":
                    swim_1=(random.randint(0, 1))
                    if swim_1==(1):
                        print("You jump into the river but your armour weighs you down and eventaly you drown")
                        quit()
                    else:
                        print("You swim across the river with relative ease and ride your horse onwards")
                        bridge_1=1
                        while_1=1
                elif river_1=="2":
                    print("You head home knowing there is no way to cross safely. You report the probblem to")
                    print("the prince but he his so upset that you have failed that he has you exicuted.")
                    quit()
                else:
                    print("You call for help but no one responds and knowing that little time remains to save the king,")
                    print("you swim across the river not careing about your armour weighing you down.")
                    swim_2=(random.randint(0,1))
                    if swim_2==(1):
                        print("You jump into the river but your armour weighs you down and eventaly you drown")
                        quit()
                    else:
                        print("You swim across the river with relative ease and ride your horse onwards")
                        bridge_1=1
                        while_1=1
            elif road_2=="1":
                print("Error")
                print("Loading backup file...")
                print("File conclusion:")
                print("Termanation")
                quit()
            else:
                print("You return home and the king dies, the prince seaks you out and has you exicuted.")
                quit()
    elif road_1=="2":
        print("You travel down the road and find a bridge with an angry mob on the other side.")
        print("You ride acrros the bridge and are greeted with the yells of the mob.")
        print("You ride past them not wanting to get into a fight.")
        bridge_1=1
        while_1=1
    else:
        print("You return home and the king dies, the prince seaks you out and has you exicuted.")
        quit()
if bridge_1==(0):
    print("You return to the split in the road and go down the second road.")
    print("You come across the remains of a bridge.")
    print("Do you wish to travel swim through the river")
    print("1. Yes")
    print("2. No")
    print("3. Call for help")
    river_1=input("")
    if river_1=="1":
        swim_1=(random.randint(0, 1))
        if swim_1==(1):
            print("You jump into the river but your armour weighs you down and eventaly you drown.")
            quit()
        else:
            print("You swim across the river with relative ease and ride your horse onwards.")
    elif river_1=="2":
        print("You head home knowing there is no way to cross safely. You report the probblem to")
        print("the prince but he his so upset that you have failed that he has you exicuted.")
        quit()
    else:
        print("You call for help but no one responds and knowing that little time remains to save the king,")
        print("you swim across the river not careing about your armour weighing you down.")
        swim_2=(random.randint(0,1))
        if swim_2==(1):
            print("You jump into the river but your armour weighs you down and eventaly you drown.")
            quit()
        else:
            print("You swim across the river with relative ease and ride your horse onwards.")
else:
    useless=useless+1
print("You ride into a town and see a store.")
while_2=0
buy_1=0
buy_2=0
buy_3=0
while while_2==0:
    print("Do you wish to enter the store.")
    print("1. Enter store")
    print("2. Ride onwards")
    town_1=input("")
    if town_1=="1":
        print("You enter the store and see a sword, a shield, and set of armour for sale.")
        print("The sword costs 10 gold. The shield costs 15 gold. The armour costs 25 gold.")
        print("Your balance is", gold)
        print("What do you wish to buy.")
        print("1. Sword")
        print("2. Shield")
        print("3. Armour")
        print("4. Sword and Shield")
        print("5. Sword and Armour")
        print("6. Shield and Armour")
        print("7. All")
        print("8. Leave store")
        store_1=input("")
        if store_1=="1":
            if buy_1==0:
                if gold>10:
                    print("You buy the sword and leave the store.")
                    attack+2
                    gold=gold-10
                    buy_1=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is sold out of that, so you leave the store.")
        elif store_1=="2":
            if buy_2==0:
                if gold>15:
                    print("You buy the shield and leave the store.")
                    armour+1
                    gold=gold-15
                    buy_2=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is sold out of that, so you leave the store.")
        elif store_1=="3":
            if buy_3==0:
                if gold>25:
                    print("You buy the armour and leave the store.")
                    armour+2
                    gold=gold-25
                    buy_3=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is out of that, so you leave the store.")
        elif store_1=="4":
            if buy_1==0 and buy_2==0:
                if gold>25:
                    print("You buy the sword and shield, and leave the store.")
                    attack+2
                    armour+1
                    gold=gold-25
                    buy_1=1
                    buy_2=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is sold out of that, so you leave the store.")
        elif store_1=="5":
            if buy_1==0 and buy_3==0:
                if gold>35:
                    print("You buy the sword and armour, and leave the store.")
                    attack+2
                    armour+2
                    gold=gold-35
                    buy_1=1
                    buy_3=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is sold out of that, so you leave the store.")
        elif store_1=="6":
            if buy_2==0 and buy_3==0:
                if gold>40:
                    print("You buy the shield and armour, and leave the store.")
                    armour+3
                    gold=gold-40
                    buy_2=1
                    buy_3=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is out of that, so you leave the store.")
        elif store_1=="7":
            if buy_1==0 and buy_2==0 and buy_3==0:
                if gold>=50:
                    print("You buy the sword, shield and armour, and leave the store.")
                    attack+1
                    armour+3
                    gold=gold-50
                    buy_1=1
                    buy_2=1
                    buy_3=1
                else:
                    print("You don't have enough gold and leave the store.")
            else:
                print("The store is out of that, so you leave the store.")
        else:
            print("You leave the store empty handded.")
    else:
        while_2=1
        print("You leave the town and continue your quest.")
encounter_1=(random.randint(0,1))
if encounter_1==(1):
    print("You travel down a road and find a caravan crashed into a fence.")
    print("You find the owner but he's being robbed.")
    print("Do you help him.")
    print("1. Yes")
    print("2. No")
    help_2=input("")
    if help_2=="1":
        robberattack_1=2
        robberarmour_1=2
        good=good+1
        print("You draw your sword and attack the robber.")
        if attack>robberarmour_1:
            print("Your sword scares the robber and he runs away but he drops 20 gold as he flees.")
            print("Do you take the gold.")
            print("1. Yes")
            print("2. No")
            take_1=input("")
            if take_1=="1":
                print("You take the gold.")
                gold=gold+20
                greed=greed+1
            else:
                print("You leave the gold for others to take.")
                print("The caravan owner gives you 10 gold for your troubles")
                gold=gold+10
                co=1
        else:
            print("The robber spots your attack and runs away.")
            print("The caravan owner gives you 5 gold for your troubles")
            gold=gold+5
            co=1
    else:
        print("The robber spots you and runs away.")
        print("The caravan owner thanks you for helping him")
        co=1
else:
    useless=useless+1
print("You are riding near a cliff and the sun starts setting.")
print("You spot a cave that could be used as a camp.")
print("Do you wish to spend the night there.")
print("1. Yes")
print("2. No")
print("3. Headback to the town")
camp_2=input("")
if camp_2=="1":
    print("You start a fire just as the sun disapears over the horizen and fall asleep.")
    print("You awake still in the night. The fire is just embers now but you can feel that")
    print("you're not alone. You light a quick fire and make a torch only to find a small")
    print("gap in the wall of the cave.")
    print("Do you investigate.")
    print("1. Yes")
    print("2. No")
    check_2=input("")
    if check_2=="1":
        print("You squeaze through the gap and find a large cavern within.")
        print("You walk onwards and are ambushed by a group of gobllins.")
        ambush_1=(random.randint(0,1))
        battlearmour_1=armour
        armour=armour-ambush_1
        gobllin1armour=1
        gobllin2armour=1
        gobllin3armour=1
        while gobllin1armour>0 or gobllin2armour>0 or gobllin3armour>0:
            if hp<=0:
                print("You have died in battle.")
                quit()
            else:
                print("Hp:", hp)
                print("gobllin_1 hp:", gobllin1armour, "gobllin_2 hp:", gobllin2armour, "gobllin_3 hp:", gobllin3armour)
                print("fight:")
                print("1. Attack")
                print("2. Run")
                battle_1=input("")
                if battle_1=="1":
                    if gobllin1armour<=0:
                        hit_1=(random.randint(1,3))
                        if hit_1==(1):
                            print("You hit the second gobllin and deal", attack, "damage.")
                            gobllin2armour=gobllin2armour-attack
                        elif hit_1==(2):
                            print("You hit the third gobllin and deal", attack, "damage.")
                            gobllin3armour=gobllin3armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    elif gobllin2armour<=0:
                        hit_1=(random.randint(1,3))
                        if hit_1==(1):
                            print("You hit the first gobllin and deal", attack, "damage.")
                            gobllin1armour=gobllin1armour-attack
                        elif hit_1==(2):
                            print("You hit the third gobllin and deal", attack, "damage.")
                            gobllin3armour=gobllin3armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    elif gobllin3armour<=0:
                        hit_1=(random.randint(1,3))
                        if hit_1==(1):
                            print("You hit the first gobllin and deal", attack, "damage.")
                            gobllin1armour=gobllin1armour-attack
                        elif hit_1==(2):
                            print("You hit the second gobllin and deal", attack, "damage.")
                            gobllin2armour=gobllin2armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    elif gobllin1armour<=0 and gobllin2armour<=0:
                        hit_1=(random.randint(1,2))
                        if hit_1==(1):
                            print("You hit the third gobllin and deal", attack, "damage.")
                            gobllin3armour=gobllin3armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    elif gobllin1armour<=0 and gobllin3armour<=0:
                        hit_1=(random.randint(1,2))
                        if hit_1==(1):
                            print("You hit the second gobllin and deal", attack, "damage.")
                            gobllin2armour=gobllin2armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    elif gobllin2armour<=0 and gobllin3armour<=0:
                        hit_1=(random.randint(1,2))
                        if hit_1==(1):
                            print("You hit the first gobllin and deal", attack, "damage.")
                            gobllin1armour=gobllin1armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                    else:
                        hit_1=(random.randint(1,4))
                        if hit_1==(1):
                            print("You hit the first gobllin and deal", attack, "damage.")
                            gobllin1armour=gobllin1armour-attack
                        elif hit_1==(2):
                            print("You hit the second gobllin and deal", attack, "damage.")
                            gobllin2armour=gobllin2armour-attack
                        elif hit_1==(3):
                            print("You hit the third gobllin and deal", attack, "damage.")
                            gobllin3armour=gobllin3armour-attack
                        else:
                            print("You miss your attack and get hit by one of the gobllins.")
                            hp=hp-1
                else:
                    print("You try to run but you're shot down by one of the gobllins.")
                    quit()
    else:
        print("You go back to sleep and rest happily.")
        if gold>=5:
            print("You awake in the morning to find five gold missing from your bag.")
            gold=gold-5
        else:
            print("You awake in the morning and continue your jernouny.")
elif camp_2=="2":
    print("You continue on but eventally you loose direction and fall into a revine")
    print("and die from the fall.")
    quit()
else:
    print("You start to make your way back to the town but night falls quickly.")
    if co==1:
        print("Luckly you find a campsite with the caravan owner who ofers to let you stay")
        print("you sleep happly that night.")
    else:
        print("Luckly you find an old caravan with a dead man next to it.")
        print("You climb into the caravan and sleep, thinking of the deadman outside.")
print("The sun rises and you continue onwards.")
print("You find a grand forest shrouded in fog. The forest is so wide that it forces")
print("you to travel through. After a while of traveling you become lost.")
left=0
forward=0
right=0
while left<(random.randint(1, 10)) or forward<(random.randint(1, 10)) or right<(random.randint(1, 10)):
    print("Which direction will you go")
    print("1. Left")
    print("2. Forward")
    print("3. Right")
    walk=input("")
    if walk=="1":
        print("You walk left")
        left=left+1
    elif walk=="2":
        print("You walk forward")
        forward=forward+1
    else:
        print("You walk right")
        right=right+1
print("You find your way to a large clearing with no fog.")
print("In the center you see a naga and nagi playing music.")
print("They spot you and attack.")
nagahp=10
nagaarmour=1
nagihp=10
nagiarmour=1
fight_1=0
while nagahp>0 or nagihp>0:
    if hp<=0:
        print("You have died in battle.")
        quit()
    else:
        print("Hp:", hp)
        print("Naga_1 hp:", nagahp, "Naga_2 hp:", nagihp)
        print("What will you do")
        print("1. Attack")
        print("2. Run")
        battle_2=input("")
        if battle_2=="1":
            if nagahp<=0:
                hit_2=(random.randint(1,2))
                if hit_2==(1):
                    fight_1=attack-nagiarmour
                    print("You hit the second naga and deal", fight_1, "damage")
                    nagihp=nagihp-fight_1
                else:
                    enemy_1=(random.randint(1,10))
                    if enemy_1==(1):
                        print("You miss your attack and get hit")
                        hp=hp-1
                    else:
                        print("You miss your attack and doddge the enemy's attack")
            elif nagihp<=0:
                hit_2=(random.randint(1,2))
                if hit_2==(1):
                    fight_1=attack-nagaarmour
                    print("You hit the first naga and deal", fight_1, "damage")
                    nagahp=nagahp-fight_1
                else:
                    enemy_1=(random.randint(1,10))
                    if enemy_1==(1):
                        print("You miss your attack and get hit")
                        hp=hp-1
                    else:
                        print("You miss your attack and doddge the enemy's attack")
            else:
                hit_2=(random.randint(1,3))
                if hit_2==(1):
                    fight_1=attack-nagiarmour
                    print("You hit the second naga and deal", fight_1, "damage")
                    nagihp=nagihp-fight_1
                elif hit_2==(2):
                    fight_1=attack-nagaarmour
                    print("You hit the first naga and deal", fight_1, "damage")
                    nagahp=nagahp-fight_1
                else:
                    enemy_1=(random.randint(1,10))
                    if enemy_1==(1):
                        print("You miss your attack and get hit")
                        hp=hp-1
                    else:
                        print("You miss your attack and doddge the enemy's attack")
        else:
            print("You try to run but are shot down by one of the naga")
            quit()
print("You beat the nagas. As you walk over there lifeless bodys you find a bag with 100 gold and a map with a marked location")
gold=gold+100
while_3=0
nagameat=(random.randint(5, 20))
hunger=0
while while_3==0:
    print("Do you wish to travel to the marked location")
    print("1. Yes")
    print("2. No")
    travel_1=input("")
    if travel_1=="1":
        print("You travel anwards towards the mark on the map.")
        while_3=1
    else:
        if hunger==(random.randint(3,10)):
            print("You die from hunger.")
            quit()
        else:
            if nagameat==0:
                print("You sleep for the night but the lack of food makes you weaker.")
                hunger=hunger+1
            else:
                print("You stay at the clearing and camp for the night. You eat some of the nagas' corpes")
                nagameat=nagameat-1
                print("You find the map with the mark")
encounter_2=(random.randint(1,2))
if encounter_2==(1):
    print("You come across a traveling merchent.")
    print("Merchant: Hello tarveler would you like to brouse my wares?")
    print("You see a Sword, a Shield, a pair of Greaves, and a pair of Gauntlets.")
    while_4=0
    buy_4=0
    buy_5=0
    buy_6=0
    while while_4==0:
        print("Would you like to buy from the shop")
        print("1. Yes")
        print("2. No")
        merchant_1=input("")
        if merchant_1=="1":
            print("Merchant: What would you like to buy?")
            print("Gold:", gold)
            print("1. Sword")
            print("2. Shield")
            print("3. Greaves")
            print("4. Sword and Shield")
            print("5. Sword and Greaves")
            print("6. Shield and Greaves")
            print("7. All")
            print("8. Stop browsing")
            store_2=input("")
            if store_2=="1":
                if buy_4==0:
                    if gold>10:
                        print("You buy the sword and stop browsing.")
                        attack+2
                        gold=gold-10
                        buy_4=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is sold out of that, so you stop browsing.")
            elif store_2=="2":
                if buy_5==0:
                    if gold>15:
                        print("You buy the shield and stop browsing.")
                        armour+1
                        gold=gold-15
                        buy_5=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is sold out of that, so you stop browsing.")
            elif store_2=="3":
                if buy_6==0:
                    if gold>25:
                        print("You buy the armour and stop browsing.")
                        armour+2
                        gold=gold-25
                        buy_6=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is out of that, so you stop browsing.")
            elif store_2=="4":
                if buy_4==0 and buy_5==0:
                    if gold>25:
                        print("You buy the sword and shield, and stop browsing.")
                        attack+2
                        armour+1
                        gold=gold-25
                        buy_4=1
                        buy_5=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is sold out of that, so you stop browsing.")
            elif store_2=="5":
                if buy_4==0 and buy_6==0:
                    if gold>35:
                        print("You buy the sword and greaves, and stop browsing.")
                        attack+2
                        armour+2
                        gold=gold-35
                        buy_4=1
                        buy_6=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is sold out of that, so you stop browsing.")
            elif store_2=="6":
                if buy_5==0 and buy_6==0:
                    if gold>40:
                        print("You buy the shield and greaves, and stop browsing.")
                        armour+3
                        gold=gold-40
                        buy_5=1
                        buy_6=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is out of that, so you stop browsing.")
            elif store_2=="7":
                if buy_4==0 and buy_5==0 and buy_6==0:
                    if gold>=50:
                        print("You buy the sword, shield and greaves, and stop browsing.")
                        attack+1
                        armour+3
                        gold=gold-50
                        buy_4=1
                        buy_5=1
                        buy_6=1
                    else:
                        print("You don't have enough gold and stop browsing.")
                else:
                    print("The Merchant is out of that, so you stop browsing.")
            else:
                print("You stop browsing.")
        else:
            print("You leave the Merchant and continue your quest.")
            while_4=1
else:
    useless=useless+1
print("You follow the map and find a grand fortress")
print("Will you enter?")
print("1. Yes")
print("2. Return Home")
fort=input("")
if fort=="2":
    print("You return home and the king dies. The prince seeks you out and has you exicuted for treason.")
    print("You got the Coward ending")
    
    text_file.write("Coward Ending/n")
    text_file.close()
    
    quit()
else:
    useless=useless+1
print("You enter the fortress and find an old king sitting on a throne with a goblet.")
print("The king is sourounded by the skeletons of fallen knights.")
print("What do you do?")
print("1. Fight")
print("2. Steal Goblet")
print("3. Leave")
fort_2=input("")
if fort_2=="2":
    print("You return home and the king dies. The prince seeks you out and has you exicuted for treason.")
    print("You got the Coward ending")
    
    text_file.write("Coward Ending/n")
    text_file.close()
    
    quit()
elif fort_2=="1":
    print("You draw you sword and attack the king. Your sword easily goes through him but no blood is drawn.")
    print("The king ignores that you attacked him and hands you the Goblet.")
else:
    print("You take the Goblet from the king with no resistance. The king looks at you sadley.")
print("What do you do?")
print("1. Drink from the Goblet")
print("2. Deliver the goblet to the prince")
demo_end=input("")
if demo_end=="1":
    print("You drink from the goblet and stay with the king waiting for the next person to be guided.")
    print("You got the Guardian Ending")
    
    text_file.write("Guardian Ending/n")
    text_file.close()
    
    quit()
else:
    print("You return home and deliver the goblet, saving the kingdom. You were remembered as a hero forever.")
    print("You got the Hero Ending")
    
    text_file.write("Hero Ending/n")
    text_file.close()
    
    quit()
