import numpy as np
import itertools
import random
import pandas as pd

deck = dict(
    coeur = 8,
    carreau = 8,
    pic = 8,
    trefle = 8
)

all_2_s= pd.Series([2,2,2,2])

n_shuffle = 100_000

games_with_a_color_evenly_distributed = 0
for _ in range(n_shuffle):
    deck_shuffled = [[card_type]*quantity for card_type,quantity in deck.items()]
    deck_shuffled= list(itertools.chain.from_iterable(deck_shuffled))
    random.shuffle(deck_shuffled)
    
    hands = [deck_shuffled[i:i+8] for i in range(0,32,8)]

    card_count_all_hands = list()
    for hand in hands:
        card_count = dict()
        for card_type in deck.keys():
            card_count[card_type] = hand.count(card_type)
        card_count_all_hands.append(card_count)

    card_df = pd.DataFrame(card_count_all_hands).T
    card_df["two_card_for_everyone?"] = card_df.apply(lambda x: x.equals(all_2_s),1)
    
    game_has_a_color_evenly_distributed = bool(card_df["two_card_for_everyone?"].sum())
    games_with_a_color_evenly_distributed += game_has_a_color_evenly_distributed
    percent_game_with_a_color_even_dist = (games_with_a_color_evenly_distributed/n_shuffle)*100
print("% of having at least one color evenly distriubed: {}".format(percent_game_with_a_color_even_dist))
