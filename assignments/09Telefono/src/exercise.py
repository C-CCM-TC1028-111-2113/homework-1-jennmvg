def main():
    #escribe tu código abajo de esta línea
    import math
print("how many messagges do you use per month?")
messages= int(input())
print("how many megas do you use per month?")
megas= float(input())
print("how many minutes do you use per month?")
minutes= int(input())
price= (messages+megas+minutes)*0.80
print("Your monthly cost is:", price)
    #Leer los datos
    pass


if __name__ == '__main__':
    main()
