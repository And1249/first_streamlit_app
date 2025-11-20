import streamlit as st
import pandas as pd

st.title('My Parents New Healty Diner')

st.header('Menú de desayuno')
st.text('🥣 Omega 3 y avena con arándanos')
st.text('🥗 Batido de col rizada, espinacas y rúcula')
st.text('🐔 Huevo duro de gallinas camperas')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pongamos una lista de selección aquí para que puedan elegir la fruta que quieran incluir 
fruits_selected = st.multiselect("Elige algunas frutas:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Muestra la tabla en la página.
st.dataframe(fruits_to_show)


