def main():
    #escribe tu código abajo de esta línea
    import math
    print(´Dame el numero de palabras´)
    words= int(input())
    pages= math.ceil(words/475)
    cost= (pages*60)*.90
    print(`El costo de la publicación es:´, cost)
    pass

if __name__ == '__main__':
    main()
