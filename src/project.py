# import pygame
import random


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


def score_calculator():
    # calculates the score through formulas and returns result
    ## scoring will be determined as such:

    ### each affinity will have a base score of 10, and a base mult of 1. 
    ### playing 1 affinity will result with a bolt, 2 of the same will upgrade to whip, 3 will be ball, 4 for the placeholder, and 5 for the comet.
    ### if all 4 affinities are selected, frenzy burst ill be the result. 
    ### every spell has a multiplier, which is equal to the spell level. bolt will have 1x, whip will have 2x, ball will have 3x, and so on. 
    ### Placeholder and burst will both be 4x

    # formula types with their scores

    # calculator that takes formulas and the input of the character 
    return


def inventory():
    # uses random to select 7 affinities from an inventory of affinities containing 7 of each.
    affinity_inventory = ["fire", "fire", "fire", "fire", "fire", "fire", "fire", "lightning", "lightning", "lightning", "lightning", "lightning", "lightning", 
                       "lightning", "holy", "holy", "holy", "holy", "holy", "holy", "holy", "mystic", "mystic", "mystic", "mystic", "mystic", "mystic", "mystic", ]
    hand_counter = 0
    hand = []
    while hand_counter < 7:
        idx = random.randrange(len(affinity_inventory))
        hand.append(affinity_inventory[idx])
        affinity_inventory.pop(idx)
        hand_counter += 1
    return hand


def game():
        player_hand = inventory()
        print(player_hand)

def main():
    running = True
    while running == True:
         
        quit = input("Do you want to quit? Y/N: ")
        if quit == "Y" or "y":
            running = False
        else:
           running = True 
    if running == False:
        print("Thank you for playing")
    


if __name__ == "__main__":
    main()