def main():
    #escribe tu código abajo de esta línea
    import math
last= float(input("what was yout last month´s balance?"))
incomes=float(input("how many incomes did you had?"))
outcomes= float(input("how many outcomes did you had?"))
checks= int(input("how many checks did you made?"))
total= (last*.925)+incomes-outcomes-(checks*13)
print("your final account balance is:", total)
    pass

if __name__ == '__main__':
    main()
