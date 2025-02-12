import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player
from modules.game import Game
from modules.hand import Hand


st.set_page_config(layout="wide",)

card_width=10
    

start_button = st.button("Start")
if "Game started" not in st.session_state:
    st.session_state["Game started"] = False
if start_button:
    game1 = Game()
    game1.game_start()
    st.session_state["Game started"] = True


    columns = st.columns(7)

    for i in range(0,7):
        with columns[i]:
            st.session_state["Immagine carta"] = game1.player1.hand.carte[i]
            st.session_state["Immagine carta"]  = st.image(st.session_state["Immagine carta"].image, use_container_width=True)
            if st.button("Seleziona carta "+ str(i)):
                game1.player1.select_card()
                st.write("carta selezionata ")
            
            

    



        



    







