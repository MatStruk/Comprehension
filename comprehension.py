import random
# Program randomize number then plays guessing game with user, telling him/her hints till he guess it
guesses_taken = 0   # counts guesses

print('Hello! What is your name?')  # prints text
myName = input()    # ask user for input

number = random.randint(1, 20)  # randomize number in range 1,20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints text

while guesses_taken < 6:    # takes up to 6 player's inputs
    print('Take a guess.')  # prints text
    guess = input()     # take intput
    guess = int(guess)  # convert input to integer

    guesses_taken += 1  # increase variable

    if guess < number:  # hints if number is lower
        print('Your guess is too low.')     # prints text

    if guess > number:  # hints if number is higher
        print('Your guess is too high.')    # prints text

    if guess == number: # if guess is even, leaves while loop
        break

if guess == number:     # if player won, then code below is executed
    guesses_taken = str(guesses_taken)  # converts integer into string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')      # prints text

if guess != number:     # if player lost, then code below is executed
    number = str(number)    # convert variable into string
    print('Nope. The number I was thinking of was ' + number)   # prints text
