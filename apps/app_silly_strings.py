from PIL import Image
import streamlit as st
from src.my_string_funcs.core import do_concat, do_uppercase

app_dict = {
    'name': 'silly string stuff',
    'pages': ('uppercase it', 'concatinator')
}

logo = Image.open('./assets/app_a_litt_up.jpg')


def create_inputs(app_page=None):
    if app_page == 'uppercase it':
        return [st.sidebar.text_input('text to uppercase', value='upper case me')]
    elif app_page == 'concatinator':
        return [st.sidebar.text_input('text a', value='hello'), st.sidebar.text_input('text b', value='world')]


def render_results(inputs=None, app_page=None):
    st.image(logo)
    st.write(f'## {app_page}')
    if app_page == 'uppercase it':
        st.write(f'Here it is in uppercase: {do_uppercase(inputs[0])}')
    elif app_page == 'concatinator':
        st.write(f'Here is the concatenated string: {do_concat(inputs)}')

