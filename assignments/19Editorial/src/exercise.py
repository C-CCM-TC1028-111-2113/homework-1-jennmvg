def main():
    #escribe tu código abajo de esta línea
    import math
words= int(input("how many words did you write?"))
pages= math.ceil(words/475)
cost= (pages*60)*.90
print("Your publiching cost is:", cost)
    pass


if __name__ == '__main__':
    main()
