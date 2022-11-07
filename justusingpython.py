import random
#The Dice Game

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(r"""\

___________.__             ________  .__                 ________                       
\__    ___/|  |__   ____   \______ \ |__| ____  ____    /  _____/_____    _____   ____  
  |    |   |  |  \_/ __ \   |    |  \|  |/ ___\/ __ \  /   \  ___\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/   |    `   \  \  \__\  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  > /_______  /__|\___  >___  >  \______  (____  /__|_|  /\___  >
                \/     \/          \/        \/    \/          \/     \/      \/     \/ 


                """)

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


p1 = input('Enter name for Player 1 > ')
print(" ")
print(" ")

p2 = input('Enter name for Player 2 > ')
print(" ")
print(" ")

print("Welcome, " + p1 + " and " + p2 + "!")
print(" ")
print("Let's start!")
print(" ")
print(" ")

print(p1 + ", enter a letter!")
print(" ")
p1letter = input('Enter your letter here > ')
print(" ")
print(" ")

print(p2 + ", enter a letter!")
print(" ")
p2letter = input('Enter your letter here > ')
print(" ")
print(" ")

p1score = random.randint(1,6)

p2score = random.randint(1,6)

if p1score==p2score:
  print("DRAW")
elif p1score>p2score:
 print(p1 + " wins")
elif p1score<p2score:
  print(p2 + " wins")

p1total = p1score
p2total = p2score

print(" ")
print(" ")
print(" ")
print(p1 + "'s score = " , p1total)
print(" ")
print(p2 + "'s score = " , p2total)












