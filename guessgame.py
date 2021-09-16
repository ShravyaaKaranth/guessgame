from random import randrange
n = randrange(1000)
while True:
    i = int(input("Guess A Number :\t"))
    if n==i:
        print("You Win!!")
        break
    print('Smaller' if n<i else 'greater')