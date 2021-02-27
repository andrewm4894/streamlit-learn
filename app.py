import streamlit as st
from apps.dev.dev import say_hello

# define apps
app_a = 'App A'
app_b = 'App B'
pages = {
    app_a: ('App A, Page A1', 'App A, Page A2'),
    app_b: ('App B, Page B1', 'App B, Page B2')
}

# inputs
app_selected = st.sidebar.selectbox('Select App', list(pages.keys()))
app_page = st.sidebar.selectbox('App Page', pages[app_selected])

# app specific inputs
if app_selected == app_a:
    st.sidebar.text_input('App A: text input')
elif app_selected == app_b:
    st.sidebar.number_input('App B: number')

# button to run app
app_run = st.sidebar.button('Run')

# render results
st.markdown("## Hello World")
st.write(say_hello('Hello from a python module i made.'))
if app_run:
    if app_selected == app_a:
        st.write('...no markdown for App A...')
        st.write(f'App is: {say_hello(app_selected)}')
        st.write(f'Page is: {app_page}')
    elif app_selected == app_b:
        st.write('...with markdown for App B...')
        st.write(f'## App is: {say_hello(app_selected)}')
        st.write(f'## Page is: {app_page}')

