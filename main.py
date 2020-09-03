#get name
name = input("What is your name?")

# just some basic encouragement 

print("That is a cool name, " + name)

# user input for how many pizzas we have

pizzas = int(input("How many pizzas do you have?"))

# user input for how many people sharing pizza

people = int(input("How many people are there?"))

# get's the amount of pizza slices, since your basic pizza has 8 pieces.

slices = pizzas * 8

# this performs our basic operation to get our amount of slices per person

slices_per_person = slices / people

print("The results are in. :)")

# for this I used an f-string this displays how many slices of pizza each person gets

print(f"There are {slices_per_person} piece/pieces of pizza for each of your {people} people.")



