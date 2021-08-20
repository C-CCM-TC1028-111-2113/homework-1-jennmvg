def main():
    #escribe tu código abajo de esta línea
    import math
number = int(input("Enter your number: "))

even = 0

while(number > 0):
  if number % 2 == 0:
    even += 1
  number = number // 10

print(f"Number of Even Numbers:", even)
    pass


if __name__ == '__main__':
    main()
