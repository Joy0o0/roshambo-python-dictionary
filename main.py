import random #random library | thư viện lựa chọn random

# get player's action | Nhập lựa chọn hành động
user_action = input("Enter a choice (rock, paper, scissors): ")

# list of computer/player possible action | Danh sách lựa chọn có thể sử dụng bởi cả hai
possible_actions = ["rock", "paper", "scissors"]

# action comparision (matching) | So sánh lựa chọn
actions_matching = {
    'rock_scissors': 'Win',
    'rock_paper': 'Lose',
    'paper_scissors': 'Lose',
    'paper_rock': 'Win',
    'scissors_rock': 'Lose',
    'scissors_paper': 'Win'
}

# computer picking their action | Máy tính chọn hành động
computer_action = random.choice(possible_actions)

# printing both player action | In ra lựa chọn cả 2
print(f"You chose {user_action}, computer chose {computer_action}.")

# checking actions | Kiểm tra lựa chọn/So sánh
if user_action == computer_action:
    # if both pick the same action | Nếu cả 2 cùng pick chung lựa chọn
    print(f"Both players selected {user_action}. It's a tie!")
else:
    # if both didn't pick a same action | Nếu cả 2 không cùng chung lựa chọn
    both_player_action = f'{user_action}_{computer_action}'
    print(actions_matching[both_player_action])

# Chú thích
# scissors: kéo , rock: đá, paper: bao
# tie: hòa


# by porudev 
# @porudev 
