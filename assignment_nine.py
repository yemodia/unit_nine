
import deck


def deal_cards(d):
    player_one_cards = []
    player_two_cards = []

    for x in range(5):
        player_one_cards.append(d.draw_a_card())
        player_two_cards.append(d.draw_a_card())

    return player_one_cards, player_two_cards


def compare_cards(card_one, card_two):
    compare = card_one.compared_to(card_two)
    return compare


def main():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    card_list_one, card_list_two = deal_cards(deck_of_cards)
    player_one_points = 0
    player_two_points = 0
    for x in range (5):
        print("Player one has", card_list_one[x])
        print("Player two has", card_list_two[x])
        print("The winning card is:", compare_cards(card_list_one[x], card_list_two[x]))
        print(" ")

main()