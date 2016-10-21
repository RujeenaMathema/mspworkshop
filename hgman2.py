import time
import random
name = input ("Enter Your Name:")
print("---------Welcome--------")
print("Hello," + name, "Time to Play!")

#wait for 1 second
time.sleep(1)

print("Start guessing....")
time.sleep(0.5)

#for random words
kelimeler = ["ability","about","above","absolute","accessible","accommodation",
             "accounting","beautiful","bookstore","calculator","clever","engaged",
             "engineer","enough","handsome","refrigerator","opposite","socks",
             "interested","strawberry","backgammon","anniversary","confused",
             "dangerous","entertainment","exhausted","impossible","overweight",
             "temperature","vacation","scissors","accommodation","appointment",
             "decrease","development","earthquake","environment","brand",
             "environment","necessary","luggage","responsible","ambassador",
             "circumstance","congratulate","frequent",]


#here we set the secret
#word = "helloworld"

word= randon.choice(kelimeler) # variable name in bracket

#create a variable with an empty value
guesses = " "

#determine number of turns
turns = 10

#check if the turns are more than zero
while(turns>0):
    
    #make a counter that starts with zero
    failed = 0

    #for every character in secret_word
    for char in word: #in returns a value 'true' or 'false'
        #see if the character is in the player's guess
        #for empty dashes____
        if char in guesses:
            print (char)
        else:
            #if not found, print dash
            print("_")

            failed +=1
    if failed == 0:
        print("------------You Won!------------")
        break

    guess = input("guess a character:")

    #set the players guess to guesses
    guesses +=guess

    #if the guess is not found in the secret word
    if guess not in word:
        #turns counter  decreases with 1
        turns -=1

        print("Wrong!")
        #how many turns are left
        print("You have,", + turns, "more guesses")

        #if the turns are equal to zero
        if turns ==0:
            print("-----------You Lose!------------")

        

        
