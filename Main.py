#CLASSES IMPORTED
import pokemon
import attack
import primary
import random

#THE 3 PRIMARY TYPES
Grass = primary.Primary("Grass")
Fire = primary.Primary("Fire")
Water = primary.Primary("Water")

#ATTACKS ASSOCIATED WITH TYPE PAIR
Ven_Attack = attack.Attack("Frenzy Plant", "Venoshock", "Grass", "Poison")
Inf_Attack = attack.Attack("Flare Blitz", "Close Combat", "Fire", "Fighting")
Smp_Attack = attack.Attack("Muddy Water", "Mud Bomb", "Water", "Ground")

#POKEMON ASSOCIATED WITH TYPE PAIR
Venusaur = pokemon.Pokemon("Venusaur", Grass, "Poison")
Infernape = pokemon.Pokemon("Infernape", Fire, "Fighting")
Swampert = pokemon.Pokemon("Venusaur", Water, "Ground")

#PARTY EACH PLAYER BEGINS WITH
user_pokemon_party = [Venusaur, Infernape, Swampert]
cpu_pokemon_party = [Venusaur, Infernape, Swampert]

#1 Introduction to the game; there are 3 Pokemon in your party to choose from:
def game_intro():
    print("Welcome to Pokemon Battle Simulator!")
    print("To begin, select your starting Pokemon.")      
    print(str(user_pokemon_party))
    response = ''
    while response not in (user_pokemon_party):
        response = input('Please enter your starter:')
    return response

game_intro()

#2 The player chooses the starter Pokemon:
starter_pokemon = game_intro(input)

#3 The CPU (Opponent) chooses 1 of 3 Pokemon at random:
cpu_starter = random.choice(cpu_pokemon_party)

### FIRST USER ATTACK ###
def first_user_sequence():
    user_pokemon_party.remove(starter_pokemon)
    if starter_pokemon == Venusaur:
        return "Venusaur used" + Ven_Attack.attack1
    elif starter_pokemon == Infernape:
        return "Infernape used" + Inf_Attack.attack1
    elif starter_pokemon == Swampert:
        return "Venusaur used" + Smp_Attack.attack1
    else:
        return "Oops, something happened."

### FIRST CPU ATTACK ###
def first_cpu_sequence():
    cpu_pokemon_party.remove(cpu_starter)
    if cpu_starter == Venusaur:
        return "The opponent chose Venusaur! The opponent's Venusaur used" + Ven_Attack("Grass")
    elif cpu_starter == Infernape:
        return "The opponent chose Infernape! The opponent's Infernape used" + Inf_Attack("Fire")
    elif cpu_starter == Swampert:
        return "The opponent chose Swampert! The opponent's Swampert used" + Smp_Attack("Water")
    else:
        return "Oops, something happened."
    
#4 First 2 Pokemon Battle, which results in a winner
first_user_sequence()
if starter_pokemon < cpu_starter:
    first_cpu_sequence()
first_round_winner = primary(self.round_winner)  #### STUCK HERE ####
print(first_round_winner)

### IF USER POKEMON LOSES, PROMPTED TO CHOOSE FROM REMAINING POKEMON ###
def new_pokemon_prompt():
    print("Who do you choose next? " + str(user_pokemon_party))
    response = ''
    while response not in user_pokemon_party:
        response = input('Please enter your next pokemon:')
    return response

### ATTACK FOR NEW USER POKEMON ###
def remaining_user_sequence():
    next_pokemon = new_pokemon_prompt(input)
    user_pokemon_party.remove(next_pokemon)
    if next_pokemon == Venusaur:
        return "Venusaur used" + Ven_Attack.attack1
    elif next_pokemon == Infernape:
        return "Infernape used" + Inf_Attack.attack1
    elif next_pokemon == Swampert:
        return "Venusaur used" + Smp_Attack.attack1
    else:
        return "Oops, something happened."

### ATTACK FOR NEW CPU POKEMON, A POKEMON CHOSEN AT RANDOM UNIQUE FROM ONE ALREADY CHOSEN ###
def remaining_cpu_sequence():
    cpu_next = random.choice(cpu_pokemon_party)
    cpu_pokemon_party.remove(cpu_next)
    if cpu_next == Venusaur:
        return "The opponent chose Venusaur! The opponent's Venusaur used" + Ven_Attack.attack1
    elif cpu_next == Infernape:
        return "The opponent chose Infernape! The opponent's Infernape used" + Inf_Attack.attack1
    elif cpu_next == Swampert:
        return "The opponent chose Swampert! The opponent's Swampert used" + Smp_Attack.attack1
    else:
        return "Oops, something happened."

#Easier Way? 'For' loop or 'While' loop?

#5 Depending on the number of Pokemon remaining in each party, the game continues, removing elements from list until a player has no more Pokemon.
if len(user_pokemon_party) == 0:
    print("It appears you are all of of Pokemon. You have lost the game.")
    pass   
elif len(cpu_pokemon_party) == 0:
    print("You have defeated all of the opponent's Pokemon. Congratulations!")
    pass
elif len(user_pokemon_party) < 1:
    new_pokemon_prompt()
    remaining_user_sequence()
elif len(cpu_pokemon_party) < 1:
    remaining_cpu_sequence()
elif len(user_pokemon_party) < 2:
    new_pokemon_prompt()
    remaining_user_sequence()
elif len(cpu_pokemon_party) < 2:
    remaining_cpu_sequence()
else:
    print("Oops, something went wrong.")

### FUNCTION FOR HOW THE GAME WRAPS UP AFTER THE USER WINS OR LOSES ###
def end_game():
    print("Would you like to play again?")
    response = ''
    while response not in {"yes", "no"}:
        response = input("Please enter yes or no: ")
    return response == "yes"

#6 User is asked to play again or exit the game.
if end_game() == "yes":
    game_intro()
else:
    exit()
