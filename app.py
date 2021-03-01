from PIL import Image
import streamlit as st
from apps.dev.dev import say_hello

logo = Image.open('./assets/litt_up.jpg')

# define apps
app_a = 'App A - Yellow'
app_b = 'App B - Red'
pages = {
    app_a: ('App A, Page A1', 'App A, Page A2'),
    app_b: ('App B, Page B1', 'App B, Page B2')
}

# inputs
st.sidebar.markdown('## Navigation')
app_selected = st.sidebar.selectbox('Select App', list(pages.keys()))
app_page = st.sidebar.selectbox('App Page', pages[app_selected])

# app specific inputs
st.sidebar.markdown('## Inputs')
if app_selected == app_a:
    input_text = st.sidebar.text_input('App A: text input')
elif app_selected == app_b:
    input_number = st.sidebar.number_input('App B: number')

# button to run app
app_run = st.sidebar.button('Run')

@st.cache
def do_work(app_selected):
    print('im doing work')
    if app_selected == app_a:
        return input_text.upper()
    elif app_selected == app_b:
        return input_number * 100
    return 'Error!'


# render results
st.image(logo)
st.markdown("## Hello World")
st.write(say_hello('Hello from a python module i made.'))
if app_run or app_page:
    if app_selected == app_a:
        st.markdown('<style>body{background-color: Yellow;}</style>', unsafe_allow_html=True)
        st.markdown('## Make it all yellow!!!')
        st.write(f'App is: {say_hello(app_selected)}')
        st.write(f'Page is: {app_page}')
        st.write(do_work(app_selected))
    elif app_selected == app_b:
        st.markdown('<style>body{background-color: Red;}</style>', unsafe_allow_html=True)
        st.markdown('## Make it all red!!!')
        st.write(f'App is: {say_hello(app_selected)}')
        st.write(f'Page is: {app_page}')
        st.write(do_work(app_selected))

