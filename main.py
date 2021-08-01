import streamlit as st
import numpy as np 
import pandas as pd 
import yagmail


yag = yagmail.SMTP('radomator', 'Leboat2021.')

st.title('Wisel Stats Analysis')
st.text('')

st.sidebar.text('')
st.sidebar.title('Analisis')
st.sidebar.markdown('')
analysis_type   = st.sidebar.selectbox('Tipo de analisis',['Basico','Enfrentamientos','Rachas','Jugadores','Historico','Plantillas','Otros'],0)
num_players = st.selectbox('Numero de jugadores',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],0)

if num_players == 7:
    st.title('Jugador 1')
    player1  = st.text_input("Name",key='1')
    email1   = st.text_input('Email',key='1')
    st.title('Jugador 2')
    player2  = st.text_input("Name",key='2')
    email2   = st.text_input('Email',key='2')
    st.title('Jugador 3')
    player3  = st.text_input("Name",key='3')
    email3   = st.text_input('Email',key='3')
    st.title('Jugador 4')
    player4  = st.text_input("Name",key='4')
    email4   = st.text_input('Email',key='4')
    st.title('Jugador 5')
    player5  = st.text_input("Name",key='5')
    email5   = st.text_input('Email',key='5')
    st.title('Jugador 6')
    player6  = st.text_input("Name",key='6')
    email6   = st.text_input('Email',key='6')
    st.title('Jugador 7')
    player7  = st.text_input("Name",key='7')
    email7   = st.text_input('Email',key='7')


    player_names  = [player1,player2,player3,player4,player5,player6,player7]
    player_emails = [email1,email2,email3,email4,email5,email6,email7]

    button_value = st.button('Generate')
  
    if button_value:
        df = pd.DataFrame({
            'playerNames' : player_names,
            'playerEmails': player_emails,
        })

        df = df.sample(frac=1).reset_index(drop=True)

        df

    # SEND EMAILS

    button_send = st.button('Send')

    if button_send:
        yag.send('angel.isinie@gmail.com','sorteo','heyyyyyy')

