# import pygame
import random
from collections import Counter


def spell_library():
    # key-value library that encompasses the spells, affinities, and score.
    # key-value library is used because, you might want to add, remove, or change affinities/score through upgrades or powerups.

    # key values of 4 affinities- fire, lightning, holy, and mystic with their score
    # affinity / score
    affinity_list = {"fire": 10,
                     "lightning": 10,
                     "holy": 10,
                     "mystic": 10,
                     "affinity_list": ["fire", "lightning", "holy", "mystic"]}
    # key values of spells- bolt, whip, ball, burst(for frenzy), placeholder, comet
    # spell / multiplier
    spell_list = {"bolt": 1,
                  "whip": 2,
                  "ball": 3,
                  "burst": 4,
                  "placeholder": 4,
                  "comet": 5}


def score_calculator(selected_hand):
    # calculates the score through formulas and returns result
    ## scoring will be determined as such:

    ### each affinity will have a base score of 10, and a base mult of 1. 
    ### playing 1 affinity will result with a bolt, 2 of the same will upgrade to whip, 3 will be ball, 4 for the placeholder, and 5 for the comet.
    ### if all 4 affinities are selected, frenzy burst ill be the result. 
    ### every spell has a multiplier, which is equal to the spell level. bolt will have 1x, whip will have 2x, ball will have 3x, and so on. 
    ### Placeholder and burst will both be 4x

    # formula types with their scores
    print("Calculating score...")
    affinity, power = Counter(selected_hand).most_common(1)[0]
    print(f"Your spell will have the {affinity} affinity and {power} multiplier")
    # calculator that takes formulas and the input of the character 
    return


def inventory():
    # uses random to select 7 affinities from an inventory of affinities containing 7 of each.
    affinity_inventory = ["fire", "fire", "fire", "fire", "fire", "fire", "fire", "lightning", "lightning", "lightning", "lightning", "lightning", "lightning", 
                       "lightning", "holy", "holy", "holy", "holy", "holy", "holy", "holy", "mystic", "mystic", "mystic", "mystic", "mystic", "mystic", "mystic", ]
    hand_counter = 0
    hand = []
    while hand_counter < 7:
        hand_counter += 1
        idx = random.randrange(len(affinity_inventory))
        hand.append(f"{affinity_inventory[idx]}")
        affinity_inventory.pop(idx)
    return hand


def game():
    player_hand = inventory()
    print(player_hand)
    selected_hand = []

    selection_process = True
    while selection_process == True:
        affinity_selection = True
        hand_confirmation = True
        while affinity_selection == True:
            try:
                selection = input("select up to 5 affinities by typing their index(1-7) seperated by spaces: ")
                inputs = selection.split()
                integer_selection = [int(item) for item in inputs]
                affinity_selection = False
            except ValueError:
                print("Invalid input, try again")

        for number in integer_selection:
            int_number = number - 1
            selected_affinity = player_hand[int_number]
            selected_hand.append(selected_affinity)
        
        
        while hand_confirmation == True:
            confirmation = input(f"Play {selected_hand}?(Y/N): ")
            if confirmation == "Y" or confirmation == "y":
                return score_calculator(selected_hand)
            elif confirmation == "N" or confirmation == "n":
                print("Canceled")
                selected_hand = []
                hand_confirmation = False
            else:
                print("Please provide a valid input.")


def main():
    running = True
    while running == True:
        quit_confirmation = True
        result = game()
        while quit_confirmation == True:
            quit = input("Do you want to quit? Y/N: ")
            if quit == "Y" or quit == "y":
                running = False
                quit_confirmation = False
            elif quit == "N" or quit == "n":
                print("Restarting.")
                quit_confirmation = False
            else:
                print("Please provide a valid input.")
    if running == False:
        print("Thank you for playing")
    

if __name__ == "__main__":
    main()