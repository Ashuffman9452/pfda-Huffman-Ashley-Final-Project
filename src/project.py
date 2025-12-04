# import pygame
import random
from collections import Counter


def spell_library():
    # affinity / score
    affinity_list = {"fire": 10,
                     "lightning": 10,
                     "holy": 10,
                     "mystic": 10,
                     "frenzy": 10,
                     "affinity_list": ["fire", "lightning", "holy", "mystic"]}

    # spell / multiplier
    spell_list = {"bolt": 1,
                  "whip": 2,
                  "ball": 3,
                  "burst": 3,
                  "reap": 4,
                  "comet": 5}
    returned_library = (affinity_list, spell_list)
    return returned_library


def score_calculator(selected_hand, returned_library):
    affinity_list, spell_list = returned_library
    spell_hierarchy = {"1": "bolt",
                       "2": "whip", 
                       "3": "ball", 
                       "4": "reap", 
                       "5": "comet"}

    # TODO: fix bug where playing spells with extra affinities further enhances damage untintentionally (could possibly make into an upgrade)
    print("Calculating score...")
    affinity, power = Counter(selected_hand).most_common(1)[0]
    frenzy_keys = ["fire", "lightning", "mystic", "holy"]
    if all(key in selected_hand for key in frenzy_keys):
        spell = spell_list["burst"]
        affinity = "frenzy"
        name = "burst"
    else:
        for value in spell_hierarchy:
            power_str = str(power)
            if power_str == value: 
                name = spell_hierarchy[f"{power_str}"]
                spell = spell_list[f"{name}"]
                break
    affinity_power = affinity_list[f"{affinity}"] * power
    spell_score = affinity_power * spell
    print(f"You cast {affinity} {name} for {spell_score} damage!")
    return spell_score


def inventory(returned_library):
    affinity_list, spell_list = returned_library
    affinity_inventory = affinity_list["affinity_list"] * 7
    hand_counter = 0
    hand = []
    while hand_counter < 7:
        hand_counter += 1
        idx = random.randrange(len(affinity_inventory))
        hand.append(f"{affinity_inventory[idx]}")
        affinity_inventory.pop(idx)
    hand_data = hand, hand_counter
    return hand_data


def game():
    # TODO: Decide wether or not to break game() into other custom functions
    returned_library = spell_library()
    player_hand, hand_counter = inventory(returned_library)
    selected_hand = []
    redraw_counter = 3

    selection_process = True
    # TODO: Add a way to discard and redraw affinities
    while selection_process == True:
        affinity_selection = True
        hand_confirmation = True
        while affinity_selection == True:
            try:
                print(player_hand)
                selection = input(f"select up to 5 affinities by typing their index(1-7), or select up to {redraw_counter} starting with 'r' to redraw, seperated by spaces: ")
                inputs = selection.split()
                if len(inputs) > 5:
                    print("You can only select up to 5 affinities!")
                elif inputs[0] == "r":
                    inputs.pop(0)
                    print(inputs)
                    if len(inputs) > redraw_counter:
                        print(f"You cannot redra more than {redraw_counter} affinities!")
                    else:
                        integer_selection = [int(item) for item in inputs]
                        for number in integer_selection:
                            int_number = number - 1
                            player_hand.pop(int_number)
                            hand_counter -= 1
                            redraw_counter -= 1
                        

                else:
                    integer_selection = [int(item) for item in inputs]
                    affinity_selection = False
            except ValueError:
                print("Invalid input, try again.")
            except IndexError:
                print("Invalid input, try again.")

        for number in integer_selection:
            int_number = number - 1
            selected_affinity = player_hand[int_number]
            selected_hand.append(selected_affinity)
               
        while hand_confirmation == True:
            confirmation = input(f"Play {selected_hand}?(Y/N): ")
            if confirmation == "Y" or confirmation == "y":
                return score_calculator(selected_hand, returned_library)
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
        print("Thank you for playing!")
    

if __name__ == "__main__":
    main()