import streamlit

streamlit.title('":heart:"My parents New Healthy Diner')
streamlit.header('":pancake:"Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-boiled, free-range egg')
streamlit.text('Avocado toast')
streamlit.header('Build your own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

