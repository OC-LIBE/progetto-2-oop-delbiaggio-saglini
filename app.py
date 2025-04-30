import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player
from modules.game import Game
from modules.hand import Hand


st.set_page_config(layout="wide",)

card_width=10
upper_column1,upper_column2,upper_column3,upper_column4,upper_column5 = st.columns([0.5,1,1.5,1.4,1],vertical_alignment="center")   

if "Game started" not in st.session_state:
    st.session_state["Game started"] = False
    st.session_state["Game1"] = ()
    st.session_state["Carta selezionata"] = False
    
with upper_column1:
    if st.button("Start",use_container_width=True):
        st.session_state["Game1"] = Game()
        st.session_state["Game1"].game_start()
        st.session_state["Game started"] = True
        st.session_state["Punteggio"] = 0
    if st.button("Restart",use_container_width=True):
        st.session_state["Game started"] = False

if st.session_state["Game started"] == True:
    
    
    columns = st.columns(8)
    for i in range(len(st.session_state["Game1"].player1.hand.carte)):
        with columns[i]:
            st.session_state["Immagine carta"] = st.session_state["Game1"].player1.hand.carte[i]
            st.session_state["Immagine carta"]  = st.image(st.session_state["Immagine carta"].image, use_container_width=True)
            if st.button("Seleziona carta "+ str(i)):
             if len(st.session_state["Game1"].player1.selected_cards) < 5:
                    if st.session_state["Game1"].player1.hand.carte[i] not in  st.session_state["Game1"].player1.selected_cards:
                        st.session_state["Game1"].player1.select_card(st.session_state["Game1"].player1.hand.carte[i])
                        st.rerun()
            if st.session_state["Game1"].player1.hand.carte[i] in st.session_state["Game1"].player1.selected_cards:
                st.write("Carta selezionata")
    with upper_column2:
        subcol1,subcol2 = st.columns([0.5,0.5],vertical_alignment="center")
        with subcol1:
            if st.session_state["Game1"].scarti > 0:
                if st.button("Scarta",use_container_width=True):
                    st.session_state["Game1"].player1.remove_card(st.session_state["Game1"].deck)
                    print(st.session_state["Game1"].player1.hand)
                    st.session_state["Game1"].scarti = st.session_state["Game1"].scarti - 1
                    st.rerun()
        with subcol2:
            if st.session_state["Game1"].mani_da_giocare > 0:
                if st.button("Gioca mano",use_container_width=True):
                    st.session_state["Game1"].logic1.riconoscimento_mani(st.session_state["Game1"].player1.selected_cards)
                    st.session_state["Game1"].player1.remove_card(st.session_state["Game1"].deck)
                    st.session_state["Punteggio"] += st.session_state["Game1"].logic1.punteggio
                    st.session_state["Game1"].mani_da_giocare = st.session_state["Game1"].mani_da_giocare - 1
                    st.rerun()
     
    with upper_column3:
        st.header("Punteggio: " +  str(st.session_state["Punteggio"]))
        st.header("Mani rimanenti: " + str(st.session_state["Game1"].mani_da_giocare))
        st.header("scarti rimanenti: " + str(st.session_state["Game1"].scarti))
        
    with upper_column4:
        st.header("Punteggio da raggiungere: " + str(st.session_state["Game1"].logic1.punteggio_da_raggiungere))

