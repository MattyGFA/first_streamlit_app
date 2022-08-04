import streamlit

streamlit.title('Mats Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥖🥓🥚🍄🍞 Sausage, Bacon, Eggs(Done your way), Beans, Mushrooms, Fried Bread')
streamlit.text('🥖🥓🥚🍅 B.E.S.T')
streamlit.text('(X)🍞 .. on Toast')
streamlit.text('🥞 Pancakes')

streamlit.header('Healthy Options')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothy')
streamlit.text('🥚 Hard-Bolied Free-Range Egg')
streamlit.text('🥑🍞 Adovado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Display the table on the page.
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())





