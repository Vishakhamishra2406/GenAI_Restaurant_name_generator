import streamlit as st
import langchain_helper
st.title("RESTAURANT NAME GENERATOR")

cuisine=st.sidebar.selectbox("Pick a Cuisine", ("American", "Chinese", "Mexican", "Italian", "Indian"))

if cuisine:
    response=langchain_helper.generate_name(cuisine)

    st.header(response['restaurant_name'])
    menu_items=response['menu_items'].split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)