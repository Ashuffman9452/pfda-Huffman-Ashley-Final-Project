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


def score_calculator(selected_hand):
    affinity_list, spell_list = spell_library()
    spell_hierarchy = {"1": "bolt",
                       "2": "whip", 
                       "3": "ball", 
                       "4": "reap", 
                       "5": "comet"}

    # TODO: fix bug where playing spells with extra affinities further enhances damage untintentionally (could possibly make into an upgrade)
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


def inventory():
    hand = []
    affinity_list, spell_list = spell_library()
    affinity_inventory = affinity_list["affinity_list"] * 7
    inventory_data = generate_hand(hand, affinity_inventory), affinity_inventory
    return inventory_data


def generate_hand(hand, affinity_inventory):
    while len(hand) < 7:
        idx = random.randrange(len(affinity_inventory))
        hand.append(f"{affinity_inventory[idx]}")
        affinity_inventory.pop(idx)
        generated_hand = hand
    return generated_hand


def floor_scaler():

    return


def enemy_manager(round):
    if round == 1:
        enemy_hp = 100
    elif round == 2:
        enemy_hp = 200
    elif round == 3:
        enemy_hp = 350
    else:
        enemy_hp = 200 + (75*round)*1.2
    return enemy_hp


def round_manager():
    ongoing_game = True
    life = 4
    highscore = 0
    round_counter = 1
    while ongoing_game == True:
        print(f"Round {round_counter}!")
        play_round = True
        required_score = enemy_manager(round_counter)
        while play_round == True:
            confirmation = True
            print(f"Enemy HP: {required_score}!")
            player_damage = play_hand()
            required_score -= player_damage
            highscore += player_damage
            if required_score <= 0:
                print("You have defeated the enemy!")
                while confirmation == True:
                    continue_confirmation = input("Dive deeper into the dungeon?(Y/N): ")
                    if continue_confirmation == "n" or continue_confirmation == "N":
                        print("You pack your things and leave while you're still alive...")
                        play_round = False 
                        return highscore
                    elif continue_confirmation == "y" or continue_confirmation == "Y":
                        life = 4
                        round_counter += 1
                        print("You drink a health potion and decide to dive deeper into the dungeon...")
                        confirmation = False
                        play_round = False
                    else:
                        print("Please provide a valid input.")
            else:
                life -= 1
                print(f"You were attacked! {life} health remaning!")
                if life <= 0:
                    print("You collapse to the ground and become just another corpse to litter the dungeon...")
                    return highscore

 
def play_hand():
    generated_player_hand_data, affinity_inventory = inventory()
    player_hand = generated_player_hand_data
    selected_hand = []
    redraw_counter = 3
    selection_process = True
    while selection_process == True:
        hand_confirmation = True
        check_index_error = True
        while check_index_error == True:
            affinity_selection = True
            while affinity_selection == True:    
                try:
                    print(player_hand)
                    if redraw_counter > 0:
                        selection = input(f"Select up to 5 affinities by typing their index(1-7), or select up to {redraw_counter} starting with 'r' to redraw, seperated by spaces: ")
                    else:
                        selection = input(f"You have no more redraws, select up to 5 affinities by typing their index(1-7) seperated by spaces: ")
                    inputs = selection.split()
                    if len(inputs) > 5:
                        print("You can only select up to 5 affinities!")
                    elif inputs[0] == "r":
                        inputs.pop(0)
                        if len(inputs) > redraw_counter:
                            print(f"You cannot redraw more than {redraw_counter} affinities!")
                        else:
                            integer_selection = [int(item) for item in inputs]
                            sorted_integer_selection = sorted(integer_selection, reverse=True)
                            for number in sorted_integer_selection:
                                int_number = number - 1
                                player_hand.pop(int_number)
                                redraw_counter -= 1    
                            generate_hand(player_hand, affinity_inventory)
                    else:
                        integer_selection = [int(item) for item in inputs]
                        affinity_selection = False
                except ValueError:
                    print("Invalid input, try again.")
                except IndexError:
                    print("Invalid input, try again.")
            try:
                for number in integer_selection:
                    int_number = number - 1
                    selected_affinity = player_hand[int_number]
                    selected_hand.append(selected_affinity)
                check_index_error = False
            except IndexError:
                print("Invalid input, try again.")
                selected_hand = []

               
        while hand_confirmation == True:
            confirmation = input(f"Play {selected_hand}?(Y/N): ")
            if confirmation == "Y" or confirmation == "y":
                redraw_counter -= len(selected_hand)
                return score_calculator(selected_hand)
            elif confirmation == "N" or confirmation == "n":
                print("Canceled")
                selected_hand = []
                hand_confirmation = False
            else:
                print("Please provide a valid input.")


def game():
    playing = True
    while playing == True:
        result = round_manager()
        return result


def main():
    running = True
    while running == True:
        quit_confirmation = True
        result = game()
        print(f"You delt {result} total damage this run!")
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