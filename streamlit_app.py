import streamlit
import pandas
streamlit.title ('My Mom\'s New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal') 
streamlit.text ('🥗 kale, Spanich & Rocket Smothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Eggs') 
streamlit.text ('🥑🍞 Avocado toast') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv ('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt') 
my_fruit_list = my_fruit_list.set_index('Fruit')

#Fruit multiselect 
fruits_selected =streamlit.multiselect ( "Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display The table on the page
streamlit.dataframe(fruits_to_show)


# New Section to display Fruitvicd api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input ( 'What fruit would you like information about','Kiwi')
streamlit.write( 'the User entered', fruit_choice) 

import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
