
import deck


def deal_cards(d):
    player_one_cards = []
    player_two_cards = []

    for x in range(4):
       player_one_cards.append(d.draw_a_card())
       player_two_cards.append(d.draw_a_card())


def compare_cards():
    pass

    
def main():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    deal_cards(deck_of_cards)



main()