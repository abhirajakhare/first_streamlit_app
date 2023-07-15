import streamlit
import pandas as pd
streamlit.title ('My Mom\'s New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal') 
streamlit.text ('🥗 kale, Spanich & Rocket Smothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Eggs') 
streamlit.text ('🥑🍞 Avocado toast') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv ('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt') 
my_fruit_list = my_fruit_list.set_index('Fruit')

#Fruit multiselect 
fruits_selected =streamlit.multiselect ( "Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display The table on the page
streamlit.dataframe(fruits_to_show)



# New Section to display Fruitvicd api response 
steamlit.header("Fruityvice Fruit Advice!")

import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
