import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hands = [rock, paper, scissors]
person_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if person_hand < 0 or person_hand >= 3:
    print("You chose the wrong number. You lose.")
else:  
    print(hands[person_hand])
    computer_hand_num = random.randint(0, 2)
    print("Computer choose: ")
    print(hands[computer_hand_num])
    
    #rock
    if person_hand == 0:
        if computer_hand_num == 0:
            print("It is a tie.")
        elif computer_hand_num == 1:
            print("Computer wins")
        else:
            print("You win")
    
    #paper
    elif person_hand == 1:
        if computer_hand_num == 0:
            print("You win.")
        elif computer_hand_num == 1:
            print("It is a tie.")
        else:
            print("Computer wins.")
    
    #scissors
    elif person_hand == 2:
        if computer_hand_num == 0:
            print("Computer wins.")
        elif computer_hand_num == 1:
            print("You win.")
        else:
            print("It is a tie.")
    
    else:
        print("You chose the wrong number!")
        print("Computer wins.")
