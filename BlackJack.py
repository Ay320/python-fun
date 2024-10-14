import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def random_card():
    return random.choice(cards)

def count_cards(cards):
    total = 0
    for card in cards:
        total += card
    return total

def final_print():
    print("______________________________________")
    print(f"your final hand is: {user_cards} , final score: {count_cards(user_cards)}")
    print(f"computer final hand is: {computer_cards} , final score: {count_cards(computer_cards)}")

def replace_11(cards):  # replace 1st instance of 11
    for card_index in range(len(cards)):
        if cards[card_index] == 11:
            cards[card_index] = 1
            break

should_continue = True
while should_continue:
    answer = input("Do you want to play? (y/n) : ")
    if answer == "n":
        break

    user_cards = []
    computer_cards = []
    user_cards.append(random_card())
    computer_cards.append(random_card())
    user_cards.append(random_card())
    
    if count_cards(user_cards) > 21 and 11 in user_cards:
        replace_11(user_cards)

    print(f"your cards: {user_cards} , current score: {count_cards(user_cards)}")
    print(f"computer first card: {computer_cards[0]}")

    if count_cards(user_cards) == 21:
        final_print()
        print("You win with a blackJack")
        continue

    while count_cards(user_cards) <= 21:
        hit = input("Do you want another card? (y/n) : ")
        if hit == "y":
            user_cards.append(random_card())
            if count_cards(user_cards) > 21:
                replace_11(user_cards)
            print(f"your cards: {user_cards} , current score: {count_cards(user_cards)}")
            print(f"computer first card: {computer_cards[0]}")
        if hit == "n":
            break

    if count_cards(user_cards) >21:
        final_print()
        print("You went over, You lose !")
        continue
    # add dealer second card (reveal)
    computer_cards.append(random_card())
    if count_cards(computer_cards) > 21:
        replace_11(computer_cards)

    while count_cards(computer_cards) < 17:
        computer_cards.append(random_card())
        if count_cards(computer_cards) > 21:
            replace_11(computer_cards)

    if count_cards(computer_cards) > 21:
        final_print()
        print("Computer went over, You win !")
        continue

    if count_cards(user_cards) > count_cards(computer_cards):
        final_print()
        print("You win !")
    elif count_cards(user_cards) < count_cards(computer_cards):
        final_print()
        print("You lose !")
    else:
        final_print()
        print("its a draw !")










