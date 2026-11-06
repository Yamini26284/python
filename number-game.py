# build  a number guessing game - computerpicks a random number, user keeps guessing until its correct !!

# output - guess : 50 --> too low!, guess : 75 --> too high!
# since, u dont know how mnay attempets would a user take, we need to use while loop, as it would only stop once the goal is achived.

import random

value = random.randint(1,50) # generatering random integers between 2 numbers

#base code

count = 0
while True : 
    hum = int(input("Guess your number between 1 to 50 : "))
    count += 1
    if hum == value:
        print(f"You got it right in {count} attempts!!")
        break
    elif  hum > value :
        print("your value is higher.") 
    else :
        print("your value is lower")

