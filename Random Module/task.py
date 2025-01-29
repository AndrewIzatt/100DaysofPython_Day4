import random
coin_flip = 'Y'
while coin_flip == 'Y':
    random_num = random.randint(1, 10)
    print(random_num)
    if 0 == random_num % 2:
        print("Heads")
    else:
        print("Tails")
    coin_flip = input("Would you like to flip again? Y or N\n")