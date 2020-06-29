#coding=utf-8

from random import random
from random import randint
from datetime import datetime
from datetime import timedelta




def main():
    print "Welcome to the number guessing game:\n I have my number..."
    my_num = randint(1,10)
    guess_num = 0
    while True:
        guess = input("What's your guess [1-10]?")
        guess_num = guess_num + 1
        if guess == my_num:
            print "You got it! Thanks for playing! Your guess time is {}".format(guess_num)
            break
        elif guess < my_num:
            print "That's too low. Try again!"
        elif guess > my_num:
            print "That's too high. Try again!"





    #num = 0
    #start_time = datetime.now()
    #period = timedelta(minutes = 5)
    #while datetime.now()-start_time<period:
    #    if random() in [0,1]:
    #        break
    #    num = num + 1

    #print num



if __name__ == "__main__":
    main()
