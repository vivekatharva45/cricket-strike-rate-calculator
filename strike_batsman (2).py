print("Welcome to Atharva's Cricket Stat Toolkit" )
print("3 Features available:")
print("1.Batting Strike Rate")
print("2.Bowling economy")
print("3.Batting average")

X = input("Please type the number to choose the option:")

def strike():
    Name = input("What is the name of the batsman? ")
    Runs = Batsman_runs(input("How many runs did the batsman score? "))
    Balls = Balls_faced(input("How many balls were faced by the batsman? "))

    rate = Runs/Balls * 100


    XX = fours(input("How many fours did the batsman hit?" ))
    XXX = sixes(input("How many sixes did the batsman hit?" ))

    Totalboundruns = int(XX)*4 + int(XXX)* 6

    boundarypercent = float(Totalboundruns/Runs*100)

    print(f"{Name}'s boundary percentage was {boundarypercent:.2f}%")
    print(f"{Name}'s strike rate was {rate:.2f}")

    if rate <=130:
     print("This was a slow innings.")


    if 130<rate<=150:
       print("This was a decent innings.")

    if 150<rate<=180:
     print("This was a good innings.")

    if 180<rate:
       print("This was an outstanding innings!")


def Batsman_runs(B):
    return int(B)


def Balls_faced(G):
    return int(G)

def fours(f):
   return(int(f))

def sixes(s):
   return (int(s))


def economy():
   Names = input("Please specify the name of the bowler? ")
   Conc = Runsconceded(input("How many runs did the bowler concede? "))
   Over = overbowled(input("How many overs did the bowler bowl? "))


   eco = Conc/Over

   print(f"{Names}'s economy is {eco:.2f}")

   if eco<6:
      print("The bowler was extremely economical.")

   if 6<=eco<9:
      print("The bowler was good.")

   if eco>9:
      print("The bowler was expensive.")


def Runsconceded(a):
   return int(a)

def overbowled(O):
   return float(O)


def average():
   Namess = input("Specify the name of the batsman: ")
   Runs_scored=scoredruns(input("How many runs did the batsman score?: "))
   Timesout=innings(input("How many times did the batsman get out?: "))

   avg = Runs_scored/Timesout

   print(f"{Namess}'s average is {avg:.2f}")

def scoredruns(x):
      return int(x)

def innings(i):
      return int(i)

if X=="1":
   strike()


elif X =="2":
   economy()


elif X == "3":
   average()

else:
   print("invalid")







