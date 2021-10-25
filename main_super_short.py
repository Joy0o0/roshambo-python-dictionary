import random
user_action = input("Enter a choice (rock, paper, scissors): ")
actions_matching = {
    'rock_scissors': 'Win',
    'rock_paper': 'Lose',
    'paper_scissors': 'Lose',
    'paper_rock': 'Win',
    'scissors_rock': 'Lose',
    'scissors_paper': 'Win'
}
computer_action = random.choice(["rock", "paper", "scissors"])
print(f"Tie") if user_action == computer_action else print(f'{actions_matching[f"{user_action}_{computer_action}"]}')
