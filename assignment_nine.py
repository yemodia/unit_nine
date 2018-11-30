# Yerim-Oumar Dia
# November 30, 2018
# Introduction to Computer Science
# This program is a model of a card compare game.
# Each player starts with a list of 5 random cards
# The program then compares the cards from each player based on the rank and the suit of the card.
# The player with the greatest card then wins that round
# The goal is to win at least 3 rounds out of 5 to win the game.
import deck


def deal_cards(d):
    """
    This function distributes the list of card to each player
    :param d: This parameter calls the draw_a_card function
    :return: This function returns the list full list of  cards for each player
    """
    player_one_cards = []
    player_two_cards = []

    for x in range(5):
        player_one_cards.append(d.draw_a_card())
        player_two_cards.append(d.draw_a_card())

    return player_one_cards, player_two_cards


def compare_cards(card_one, card_two):
    """
    This function compares the two cards in the list
    :param card_one: The  card being compared  for player one
    :param card_two: The card being compared for player two
    :return: This function returns the greater card
    """
    compare = card_one.compared_to(card_two)
    return compare


def main():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    card_list_one, card_list_two = deal_cards(deck_of_cards)
    player_one_points = 0
    player_two_points = 0
    for x in range(5):
        print("Player one has", card_list_one[x])
        print("Player two has", card_list_two[x])
        winning_card = compare_cards(card_list_one[x], card_list_two[x])
        print("The winning card is:", winning_card)
        print(" ")
        if winning_card in card_list_one:
            player_one_points = player_one_points + 1

        if winning_card in card_list_two:
            player_two_points = player_two_points + 1

    if player_one_points > player_two_points:
        print("Player One Wins the Game!!")
    else:
        print("Player Two Wins the Game !!")


main()
