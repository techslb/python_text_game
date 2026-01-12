def print_main_menu():
    print("The Red Divide")
    print("Select an option below:\n")
    print("1: New Game")
    print("2: Exit")

def get_input():
    return int(input())

def main():
    print_main_menu()
    choice = get_input()

    if choice == 1:
        print("Starting New Game")
    elif choice == 2:
        print("Exiting the program") # change this to something more user friendly
    else:
        print("Invalid selection. Please try again.")

#def print_modifiable_stats_list(selection): #Figure this out later
    #for name, desc in modifiable_stats_list:
        #print(name)
        #print(desc)