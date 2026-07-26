print("Welcome")
def main():
    Name = input("What is the name of the batsman? ")
    Runs = Batsman_runs(input("How many runs did the batsman score? "))
    Balls = Balls_faced(input("How many balls were faced by the batsman? "))

    rate = Runs/Balls * 100

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

main()


