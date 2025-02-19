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
    st.session_state["Game1"] = ()
    st.session_state["Carta selezionata"] = False
if start_button:
    st.session_state["Game1"] = Game()
    st.session_state["Game1"].game_start()
    st.session_state["Game started"] = True

if st.session_state["Game started"] == True:
    
    columns = st.columns(8)
    for i in range(len(st.session_state["Game1"].player1.hand.carte)):
        with columns[i]:
            st.session_state["Immagine carta"] = st.session_state["Game1"].player1.hand.carte[i]
            st.session_state["Immagine carta"]  = st.image(st.session_state["Immagine carta"].image, use_container_width=True)
            if len(st.session_state["Game1"].player1.selected_cards) < 5:
                if st.button("Seleziona carta "+ str(i)):
                    st.session_state["Game1"].player1.select_card(st.session_state["Game1"].player1.hand.carte[i])
    # for card in st.session_state["Game1"].player1.selected_cards:
    #     with columns[i]:
    #         st.write("Carta selezionata")
    if st.button("Scarta"):
        st.session_state["Game1"].player1.remove_card(st.session_state["Game1"].deck)
        print(st.session_state["Game1"].player1.hand)
        st.rerun()
    


            
            

    



        



    







