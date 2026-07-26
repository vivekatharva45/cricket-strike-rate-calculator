print("Welcome")
def main():
    Name = input("What is the name of the batsman? ")
    Runs = Batsman_runs(input("How many runs did the batsman score? "))
    Balls = Balls_faced(input("How many balls were faced by the batsman? "))

    rate = Runs/Balls * 100

    print(f"The strike rate is {rate:.2f}")


def Batsman_runs(B):
    return int(B)






def Balls_faced(G):
    return int(G)

main()
