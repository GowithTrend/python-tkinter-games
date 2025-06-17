import random

def start_game():
    print("🌲 Welcome to the Jungle Adventure!")
    print("You're standing at the edge of a mysterious forest.")
    print("Do you want to ENTER the forest or RUN away?")
    choice1 = input("Type 'enter' or 'run': ").strip().lower()
    if choice1 == "enter":
        forest_path()
    elif choice1 == "run":
        print("\n😅 You chose safety, but missed the adventure!")
    else:
        print("\n❗ Invalid choice. Game ended. Try again!")

def forest_path():
    print("\nYou walk into the forest and see a wide river.")
    print("Do you want to SWIM across or BUILD a raft?")
    choice2 = input("Type 'swim' or 'build': ").strip().lower()
    if choice2 == "swim":
        print("\nOh no! A crocodile got you. 🐊 Game over.")
    elif choice2 == "build":
        treasure_island()
    else:
        print("\n❗ Invalid choice. Lost in the jungle with no way out.")

def treasure_island():
    print("\nSmart move! You built a raft and crossed safely.")
    print("Ahead, you find a treasure chest and a cave entrance.")
    print("Do you open the CHEST or ENTER the CAVE?")
    choice3 = input("Type 'chest' or 'cave': ").strip().lower()
    if choice3 == "chest":
        print("\n🎉 You found gold and jewels! You Win!")
    elif choice3 == "cave":
        snake_challenge()
    else:
        print("\n❗ Invalid choice. Treasure fades away into the jungle.")

def snake_challenge():
    print("\nInside the cave, you encounter a sleeping snake.")
    print("Do you SNEAK past it or RUN away silently?")
    choice4 = input("Type 'sneak' or 'run': ").strip().lower()
    if choice4 == "sneak":
        print("\n👏 Amazing! The snake didn't wake up. You escape with a chest! You Win!")
    elif choice4 == "run":
        print("\nThe snake woke up and slithered after you. You got bitten. Game over.")
    else:
        print("\n❗ Invalid choice. Cave seals shut, you're trapped forever!")

def play_again():
    print("\nDo you want to play again? (yes/no)")
    replay = input().strip().lower()
    return replay == "yes"

while True:
    start_game()
    if not play_again():
        print("\nThanks for playing! 🧠 See you next time.")
        break
