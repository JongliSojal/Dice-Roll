#made by Jongli Sojal

from random import randint

print "Welcome to Dice Roll 1.0"
print

def pc_roll(x):
    if x==1:
        print " ___________\n" \
              "|           |\n" \
              "|     _     |\n" \
              "|    |_|    |\n" \
              "|           |\n" \
              "|___________|\n"
        
    if x==2:
        print " ___________\n" \
              "|   _       |\n" \
              "|  |_|      |\n" \
              "|       _   |\n" \
              "|      |_|  |\n" \
              "|___________|\n"

    if x==3:
        print " ___________\n" \
              "|  _        |\n" \
              "| |_| _     |\n" \
              "|    |_| _  |\n" \
              "|       |_| |\n" \
              "|___________|\n"

    if x==4:
        print " ___________\n" \
              "|  _     _  |\n" \
              "| |_|   |_| |\n" \
              "|  _     _  |\n" \
              "| |_|   |_| |\n" \
              "|___________|\n"
        
    if x==5:
        print " ___________\n" \
              "|  _     _  |\n" \
              "| |_| _ |_| |\n" \
              "|  _ |_| _  |\n" \
              "| |_|   |_| |\n" \
              "|___________|\n"

    if x==6:
        print " ___________\n" \
              "|  _  _  _  |\n" \
              "| |_||_||_| |\n" \
              "|  _  _  _  |\n" \
              "| |_||_||_| |\n" \
              "|___________|\n"


def your_roll(n):
    if n==1:
        print " ___________\n" \
              "|           |\n" \
              "|     _     |\n" \
              "|    |_|    |\n" \
              "|           |\n" \
              "|___________|\n"
        
    if n==2:
        print " ___________\n" \
              "|   _       |\n" \
              "|  |_|      |\n" \
              "|       _   |\n" \
              "|      |_|  |\n" \
              "|___________|\n"

    if n==3:
        print " ___________\n" \
              "|  _        |\n" \
              "| |_| _     |\n" \
              "|    |_| _  |\n" \
              "|       |_| |\n" \
              "|___________|\n"
        
    if n==4:
        print " ___________\n" \
              "|  _     _  |\n" \
              "| |_|   |_| |\n" \
              "|  _     _  |\n" \
              "| |_|   |_| |\n" \
              "|___________|\n"

    if n==5:
        print " ___________\n" \
              "|  _     _  |\n" \
              "| |_| _ |_| |\n" \
              "|  _ |_| _  |\n" \
              "| |_|   |_| |\n" \
              "|___________|\n"
 
    if n==6:
        print " ___________\n" \
              "|  _  _  _  |\n" \
              "| |_||_||_| |\n" \
              "|  _  _  _  |\n" \
              "| |_||_||_| |\n" \
              "|___________|\n"


victory = 0
defeat = 0

while True:
    n = input("Enter 0 to quit.\nEnter Roll Value[1-6]: ")
    print
    if n==0:
        print "Win: ", victory
        print "Lose: ", defeat
        print "Thanks for playing!"
        break
    else:
        print "Required Roll"
        x = randint(1, 6)
        pc_roll(x)
        print "Your Roll"
        your_roll(n)

        if (x == n):
            victory = victory + 1
            print "Victory!"
            print "Win: ", victory
            print "Lose: ", defeat
            
        else:
            defeat = defeat + 1
            print "Defeat!"
            print "Win: ", victory
            print "Lose: ", defeat
            
        print
