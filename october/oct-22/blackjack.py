import random

player1 = []
dealer = []
running = True
deck = ['A','K','Q','J','2','3','4','5','6','7','8','9','10'] *4
deck_values = {
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10
}

house = []
player1 = []

def add_card(player_cards):
    player_cards.append(deck.pop(random.randint(0,len(deck))))
    return player_cards
        
def check_winner(house, player):
    print(f'House score: {house}.')
    print(f'Player score: {player}.')
    total_dealer = 0
    total_player = 0
    for num in house:
        total_dealer += deck_values[num]
    for num in player:
        total_player += deck_values[num]
    if total_dealer < 17:
        house = add_card(house)
        check_winner(house, player)
    else:
        if total_player > 21:
            return print("YOU BUST! Dealer wins")
        elif total_player < 22 and total_dealer > 21:
            return print("DEALER BUST! Player wins!")
        elif total_player > total_dealer:
            return print("Player wins!")
        elif total_dealer > total_player:
            return print("Dealer wins!")
        elif total_player == total_dealer:
            return print("PUSH. You get your money back:) ")

def deal_hand():
    random_num = deck.pop(random.randint(0,len(deck)))
    random_num2 = deck.pop(random.randint(0,len(deck)))
    return [random_num, random_num2]

def values(house, player):
    total_dealer = 0
    total_player = 0
    for num in house:
        total_dealer += deck_values[num]
    for num in player:
        total_player += deck_values[num]
    print(f'Players cards are {player}.')
    print(f'House cards are {house[0]} and Unknown.')
    print(f'Total for the player: {total_player}.', f'Total for the dealer: {total_dealer}.')
    add1_card = input('Would you like to add a card? (y)es (n)o \n Enter here: ')
    if add1_card == 'y':
        if total_player > 21:
            return check_winner(house, player)
        player = add_card(player)
        values(house, player)
    else:
        
        return check_winner(house, player)

def see_cards():
    house = deal_hand()
    player1 = deal_hand()
    print(f'Players cards are {player1[0]} and {player1[1]}.')
    print(f'House cards are {house[0]} and Unknown.')
    return values(house, player1)

see_cards()

# STEPS OF THE GAME:

# 1. Deal the cards
# 2. Check for blackjack for player or house
# 3. See player cards, see one of house's cards
# 4. Player gets to choose if they want another card
# 5. Player gets cards until they don't want more
# 6. If house is less than 16, add cards until over 16 or over 21
# 7. If house is over 21, player wins (if he didn't bust) 
#    If house is less than player, player wins
#    If house is greater than player, house wins