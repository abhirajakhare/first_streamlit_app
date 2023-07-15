import streamlit
import pandas as pd
streamlit.title ('My Parents New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal') 
streamlit.text ('🥗 kale, Spanich & Rocket Smothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Eggs') 
streamlit.text ('🥑🍞 Avocado toast') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv ('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt') 
#Fruit multiselect 
streamlit.multiselect ( "Pick Some Fruits:", list(my_fruit_list.index))
#Display The table on the page
streamlit.dataframe(my_fruit_list)

