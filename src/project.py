# import pygame
import random
from collections import Counter

class Spell_Manager:
    def __init__(self):
        # affinity / score
        self.affinity_list = {"fire": 10,
                              "lightning": 10,
                              "holy": 10,
                              "mystic": 10,
                              "frenzy": 25,
                              "affinity_list": ["fire", "lightning", "holy", "mystic"]}
        
        # spell / multiplier
        self.spell_list = {"bolt": 1,
                           "whip": 2,
                           "ball": 3,
                           "burst": 3,
                           "reap": 4,
                           "comet": 5}
        
    def cast_spell(self, spell, affinity):
        if spell in self.spell_list:
            self.spell_list[spell] += .5
        if affinity in self.affinity_list:
            self.affinity_list[affinity] += 2
        
    def get_spell_libraries(self):
        spell_library_data = self.affinity_list, self.spell_list
        return spell_library_data


def score_calculator(selected_hand):
    affinity_list, spell_list = spell_manager.get_spell_libraries()

    spell_hierarchy = {"1": "bolt",
                       "2": "whip", 
                       "3": "ball", 
                       "4": "reap", 
                       "5": "comet"}

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
    affinity_power = affinity_list[f"{affinity}"] * (power)
    spell_score = round(affinity_power * spell)

    spell_manager.cast_spell(name, affinity)


    print(f"You cast {affinity} {name} for {spell_score} damage!")
    print(f"You become more proficient in casting {name}s and {affinity} affinities!\n")
    return spell_score


def inventory():
    hand = []
    affinity_list, spell_list = spell_manager.get_spell_libraries()
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


def floor_scaler(round_count, floor):
    if round_count < 5 and floor == 1:
        enemy_hp = 50 * round_count
    elif round_count == 5 and floor == 1:
        enemy_hp = 350
    elif round_count < 5 and floor > 1:
        enemy_hp = (100 * floor + (75*(round_count + floor)))
    elif round_count == 5 and floor > 1:
        enemy_hp = (125 * floor + (75*(round_count + floor)) + 150)
    return enemy_hp


def enemy_manager():
    name_list = ["Jimbo", "Libra", "Siouxsie", "Molina", "Dallon", "Snarf", "Ingward", "Eingyi", "Anastacia", "Andre", "Oswald", "Shiva", "Kaathe", "Azathoth"]
    race_list = ["Vampire", "Goblin", "Zombie", "Fae", "Elf", "Succubus", "Demon", "Angel", "Skeleton", "Kijetesantakalu", "Pikmin", "Comprehensibly Incomprehensible Ant"]
    modifier_list = ["Monarch", "Prophet", "Lich", "Scholar", "Paladin", "Warlock", "Cleric", "Statue", "that's slightly attractive", "Warrior"]
    name_idx = random.randrange(len(name_list))
    race_idx = random.randrange(len(race_list))
    modifier_idx = random.randrange(len(modifier_list))
    name = f"{name_list[name_idx]}"
    race = f"{race_list[race_idx]}"
    modifier = f"{modifier_list[modifier_idx]}"
    enemy_name_data = name, race, modifier
    return enemy_name_data


def round_manager():
    ongoing_game = True
    life = 5
    highscore = 0
    round_counter = 1
    floor_counter = 1
    while ongoing_game == True:
            name, race, modifier = enemy_manager()
            print(f"Floor {floor_counter}, Round {round_counter}!")
            play_round = True
            required_score = floor_scaler(round_counter, floor_counter)

            while play_round == True:
                confirmation = True
                
                if round_counter == 5 and floor_counter == 10:
                    required_score = 12082025
                    print (f"Floor Guardian Rick, Soldier of God HP: {required_score}!")
                elif round_counter == 5:
                    print(f"Floor Guardian {name}, the {race} {modifier} HP: {required_score}!")
                elif round_counter < 5:
                    print(f"Enemy HP: {required_score}!")

                player_damage = play_hand()
                required_score -= player_damage
                highscore += player_damage
                if required_score <= 0:

                    if round_counter < 5:
                        if round_counter == 5 and floor_counter == 10:
                            print("\n")
                            print("Rick collapses to the ground, grasping his greatsword. He doesn't say a word, but nods to you in approval and allows you to pass.")
                            print("You walk past him, your body aching from your journey, and approach a well decorated stone door.")
                            print("Your hand touches the dark, cold, door and pushes it forward... a warm, dim light floods the room, gradually getting brighter.")
                            Print("You walk into the light...\n")
                            Print("And so you disappear, with your fate unknown...")
                            play_round = False
                            ongoing_game = False
                            return highscore
                        print("You have defeated the enemy!\n") 
                        if life < 5:
                            life += 1
                        round_counter += 1
                    elif round_counter == 5:
                        print("You have defeated the Floor Guardian!\n")            
                        while confirmation == True:
                            continue_confirmation = input("Dive deeper into the dungeon?(Y/N): ")
                            if continue_confirmation == "n" or continue_confirmation == "N":
                                print("You pack your things and leave while you're still alive...\n")
                                play_round = False 
                                return highscore
                            elif continue_confirmation == "y" or continue_confirmation == "Y":
                                life = 5
                                round_counter = 1
                                floor_counter += 1
                                print("You drink a health potion and decide to dive deeper into the dungeon...\n")
                                confirmation = False
                                play_round = False
                            else:
                                print("Please provide a valid input.")

                    play_round = False
                else:
                    life -= 1
                    print(f"You were attacked! {life} health remaning!\n")
                    if life <= 0:
                        if round_counter == 5 and floor_counter == 10:
                            decision = True
                            print("You collapse and grasp your chest... your mind stops racing, and you accept your fate, like a prey animal that knows it's time to stop running...")
                            print("You await your execution from the final Floor Guardian- Rick, Soldier of God... but only a hand stretches out.")
                            while decision == True:
                                choice = input("Do you take his hand?(Y/N): ")
                                if choice == "y" or choice == "Y":
                                    print("\n")
                                    print("You reach out and take his hand. The pain of your wounds no longer haunt you, and you stand up.")
                                    name = input("Rick asks for your name: ")
                                    print("\n")
                                    print("You've fought well, and valiantly, honing your spells and affinities, all of your choices have led up to this point.")
                                    print(f"You are now- {name}, Spellshock of God")
                                    return highscore
                                elif choice == "n" or choice == "N":
                                    print("\n")
                                    print("You deny his offer, your strength fades and so does the dungeon around you.")
                                    print("As you accept your own decision, Rick sits next to you, and you lie against the cold stone floor with a companion...\n")
                                    print("And so you lie as a corpse, spelldrained and valiantly fought...")
                                    return highscore
                                else:
                                    print("Please provide a valid input.")
                        print("You collapse to the ground and become just another corpse to litter the dungeon...\n")
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
        print("Thank you for playing Spellshock!")

spell_manager = Spell_Manager()   

if __name__ == "__main__":
    main()