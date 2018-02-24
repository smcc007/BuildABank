from Account import Account as acc

def mainProg():
    acc1 = acc()
    print acc1
    acc1.balance = 25
    print acc1


if __name__ == "__main__":
    mainProg()
