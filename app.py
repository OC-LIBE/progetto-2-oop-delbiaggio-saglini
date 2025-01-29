import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player
from modules.game import Game
from modules.hand import Hand


st.set_page_config(layout="wide",)

card_width=10
    

start_button = st.button("Start")
if start_button:
    game1 = Game()
    game1.game_start()
    hand1 = Hand()


    columns = st.columns(7)

    for i in range(1,7):
        with columns[i]:
            carta = hand1.mano[i]
            st.image(carta, use_column_width=True)

    



        



    







