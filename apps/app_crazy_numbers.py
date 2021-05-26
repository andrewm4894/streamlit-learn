from PIL import Image
import streamlit as st
from src.dev.dev import say_hello

app_dict = {
    'name': 'crazy numbers',
    'pages': ('make it yuge', 'sum them')
}

logo = Image.open('./assets/app_b_litt_smiling.jpg')


def create_inputs(app_page=None):
    if app_page == 'make it yuge':
        return [st.sidebar.number_input('make me yuge', 42)]
    elif app_page == 'sum them':
        return [st.sidebar.number_input('number 1', 2), st.sidebar.number_input('number 2', 2)]


def render_results(inputs=None, app_page=None):
    st.image(logo)
    st.markdown('<style>body{background-color: Red;}</style>', unsafe_allow_html=True)
    st.markdown('## Make it all red!!!')
    st.write(f'Page is: {say_hello(app_page)}')
    if app_page == 'make it yuge':
        st.write(f'Its yuge: {inputs[0]*100000}')
    elif app_page == 'sum them':
        st.write(f'summed up: {sum(inputs)}')