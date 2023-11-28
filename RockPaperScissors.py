import random

def main():
    print('Guidelines for ROCK, PAPER, SCISSORS:')
    print('Rock vs Paper -> Paper wins')
    print('Rock vs Scissors -> Rock wins')
    print('Paper vs Scissors -> Scissor wins\n')

    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        choice = int(input("Enter your choice :"))

        while choice > 3 or choice < 1:
            choice = int(input("Enter a valid choice please ☺ "))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        print(f"User choice is: {choice_name}\n")

        print("Now its the Computers Turn! ")
        comp_choice = random.randint(1, 3)

        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print(f"Computer choice is : {comp_choice_name}\n")
        print(f"{choice_name} Vs {comp_choice_name}")
        print('.' * 100)

        if ((choice == 1 and comp_choice == 2) or
           (choice == 2 and comp_choice == 1)):
            result = 'Paper'
            winner = 'Paper wins'
        elif ((choice == 1 and comp_choice == 3) or
             (choice == 3 and comp_choice == 1)):
            result = 'Rock'
            winner = f'You win, with {choice_name}!'
        elif ((choice == 2 and comp_choice == 3) or
             (choice == 3 and comp_choice == 2)):
            result = 'Scissors'
            winner = f'You win, with {choice_name}!'

        if comp_choice_name == result:
            print(f"\nThe computer wins, with {comp_choice_name}!\n")
        else:
            print(f"\n{winner}\n")

        print("Do you want to play again? (Y/N): ")
        ans = input()
        if ans.lower() == 'n':
            break

    print("\nThanks for playing")

# Run the game
main()
