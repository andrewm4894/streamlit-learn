from PIL import Image
import streamlit as st
from src.dev.dev import say_hello

app_dict = {
    'name': 'silly string stuff',
    'pages': ('uppercase it', 'concatinator')
}

logo = Image.open('./assets/app_a_litt_up.jpg')

@st.cache
def do_uppercase(some_string):
    return some_string.upper()


@st.cache
def do_concat(strings_to_concat, sep=' '):
    return f'{sep}'.join(strings_to_concat)


def create_inputs(app_page=None):
    if app_page == 'uppercase it':
        return [st.sidebar.text_input('text to uppercase', 'upper case me')]
    elif app_page == 'concatinator':
        return [st.sidebar.text_input('text a', 'hello'), st.sidebar.text_input('text b', 'world')]


def render_results(inputs=None, app_page=None):
    st.image(logo)
    st.markdown('<style>body{background-color: Yellow;}</style>', unsafe_allow_html=True)
    st.markdown('## Make it all yellow!!!')
    st.write(f'Page is: {say_hello(app_page)}')
    if app_page == 'uppercase it':
        st.write(f'Here it is in uppercase: {do_uppercase(inputs[0])}')
    elif app_page == 'concatinator':
        st.write(f'Here is the concatenated string: {do_concat(inputs)}')

