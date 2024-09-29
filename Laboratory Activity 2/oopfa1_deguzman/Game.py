from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
from random import randint
import time

x = int(input("1 : Player VS Player || 2 : Player VS Computer\n  :  "))

while x != 0:
    
    if x == 1: # Multiplayer
        player1 = input('Enter name P1 : ')
        X = input('1 : Swordsman | 2 : Archer | 3 : Magician\n   :   ')
        if X == 1: # Swordsman
            p1 = Swordsman(player1)
            callback = p1.getHp()
        elif X == 2: # Archer
            p1 = Archer(player1)
            callback = p1.getHp()
        else: # Magician
            p1 = Archer(player1)
            callback = p1.getHp()
            
        player2 = input('Enter name P2 : ')
        Y = input('1 : Swordsman | 2 : Archer | 3 : Magician\n   :   ')
        if Y == 1: # Swordsman
            p2 = Swordsman(player2)
            callback2 = p2.getHp()
        elif Y == 2: # Archer
            p2 = Archer(player2)
            callback2 = p2.getHp()
        else: # Magician
            p2 = Magician(player2)
            callback2 = p2.getHp()
        
        gameMulti = 1
        p1wins = 0
        p2wins = 0
        stageNo = 0
        while gameMulti != 0:
            print(f"##### STAGE {stageNo} #####")
            
            while p1.getHp() > 0 and p2.getHp() > 0:
                print(f"\n{p1.getUsername()} HP: {p1.getHp()}")
                print(f"{p2.getUsername()} HP: {p2.getHp()}")
                
                if randint(0, 1) == 1:
                    if isinstance(p1, Swordsman):
                        p1.slashAttack(p2)
                    elif isinstance(p1, Archer):
                        p1.rangedAttack(p2)
                    elif isinstance(p1, Magician):
                        p1.magicAttack(p2)
                        p1.heal()
                else:
                    print(f"{p1.getUsername()} missed!")
                if p2.getHp() <= 0:
                    break
                    
                print("Player 2's Turn!")
                if randint(0, 1) == 1:
                    if isinstance(p2, Swordsman):
                        p2.slashAttack(p1)
                    elif isinstance(p2, Archer):
                        p2.rangedAttack(p1)
                    elif isinstance(p2, Magician):
                        p2.magicAttack(p1)
                        p2.heal()
                else:
                    print(f"{p2.getUsername()} missed!")
                time.sleep(0.3)
                
            if p1.getHp() <= 0:
                print(f"\n{p2.getUsername()} WON")
                p2wins += 1
                p1.setHp(callback)
                p2.setHp(callback2)
            if p2.getHp() <= 0:
                print(f"\n{p1.getUsername()} WON")
                p1wins += 1
                p1.setHp(callback)
                p2.setHp(callback2)
            
            gameMulti = int(input('\npress 0 to END! | anything else to continue...'))
            stageNo += 1
            
        print(f"P1 wins {p1wins} | P1 wins {p2wins} ")
        break
    
    elif x == 2: # Single Player
        
        p1 = Novice(input('\nPlease a name for this New Game: '))
        
        comp1 = Archer("Fiandell the Quick")
        comp2 = Swordsman("Ronald the Valiant")
        comp3 = Boss("Monster")

        # STAGE 1
        print("##### STAGE 1 #####")
        
        while p1.getHp() > 0 and comp1.getHp() > 0:
            print(f"\n{p1.getUsername()} HP: {p1.getHp()}")
            print(f"{comp1.getUsername()} HP: {comp1.getHp()}")
            p1.basicAttack(comp1)
            if comp1.getHp() > 0:
                if randint(0, 1) == 1:
                    comp1.rangedAttack(p1)
                else:
                    print(f"{comp1.getUsername()} missed!")
            #time.sleep(0.3)
            
        if p1.getHp() <= 0:
            print('\nGAME OVER! Exiting Game...')
            break
        if comp1.getHp() <= 0:
            print('\nYOU WIN! all stats increased...')
            p1.setHp(125)
            p1.setDamage(7)
        
        # STAGE 2
        print("\n##### STAGE 2 #####\n Loading, Please Wait...")
        time.sleep(3)
        
        while p1.getHp() > 0 and comp2.getHp() > 0:
            print(f"\n{p1.getUsername()} HP: {p1.getHp()}")
            print(f"{comp2.getUsername()} HP: {comp2.getHp()}")
            p1.basicAttack(comp2)
            if comp2.getHp() > 0:
                if randint(0, 1) == 1:
                    comp2.slashAttack(p1)
                else:
                    print(f"{comp2.getUsername()} missed!")
            time.sleep(0.3)
            
        if p1.getHp() <= 0:
            print('\nGAME OVER! Exiting Game...')
            break
        if comp2.getHp() <= 0:
            print('\nYOU WIN! You can now change your role against the final boss.')
    
            y = input('1 : Swordsman | 2 : Archer | 3 : Magician\n   :   ')
            if y == 1: # Swordsman
                Swordsman = Swordsman(f"{p1.getUsername()}")
                p1 = Swordsman
            elif y == 2: # Archer
                Archer = Archer(f"{p1.getUsername()}")
                p1 = Archer
            else: # Magician
                Magician = Magician(f"{p1.getUsername()}")
                p1 = Magician
                
        # BOSS FIGHT
        print("\n##### FINALE #####\n Loading, Please Wait...")
        time.sleep(3)
        
        while p1.getHp() > 0 and comp3.getHp() > 0:
            print(f"\n{p1.getUsername()} HP: {p1.getHp()}")
            print(f"{comp3.getUsername()} HP: {comp3.getHp()}")
            p1.basicAttack(comp3)
            if p1 == Swordsman:
                p1.slashAttack(comp3)
            if p1 == Archer:
                p1.rangedAttack(comp3)
            if p1 == Magician:
                p1.magicAttack(comp3)
                p1.heal()
            if comp3.getHp() > 0:
                if randint(0, 5) == 5:
                    comp3.basicAttack(p1)
                    comp3.slashAttack(p1)
                    comp3.magicAttack(p1)
                    comp3.rangedAttack(p1)
                    comp3.heal()
                else:
                    print(f"{comp3.getUsername()} missed!")
            time.sleep(0.3)
            
        if p1.getHp() <= 0:
            print('\nGAME OVER! Exiting Game...')
            break
        if comp3.getHp() <= 0:
            print('\nYOU WIN! The Game will now exit...')
            break
        
    else:
        print('invalid input!')
        x = int(input("1 : Player VS Player || 2 : Player VS Computer\n  :  "))