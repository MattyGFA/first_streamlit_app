import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please selecta fruit to get information.")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.error()

# Snowflake Connector
streamlit.header("The fruit load list contains:")
# Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
         return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

# Don't run anything past here....
streamlit.stop()

# Snowflake add fruit
add_my_fruit = streamlit.text_input('What fruit would you like add?')
streamlit.write('Adding: ', add_my_fruit)
