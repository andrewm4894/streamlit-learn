from PIL import Image
import streamlit as st
import numpy as np
from src.funny_numbers.core import multiply_by, sum_it

app_dict = {
    'name': 'crazy numbers',
    'pages': ('make it yuge', 'sum them')
}

logo = Image.open('./assets/app_b_litt_smiling.jpg')


def create_inputs(app_page=None):
    if app_page == 'make it yuge':
        return [st.sidebar.number_input('make me yuge', value=42)]
    elif app_page == 'sum them':
        return [st.sidebar.number_input('number 1', value=2), st.sidebar.number_input('number 2', value=2)]


def render_results(inputs=None, app_page=None):
    st.image(logo)
    st.write(f'## {app_page}')
    if app_page == 'make it yuge':
        multiplier = int((np.random.rand()*100)*(np.random.rand()*100))
        st.write(f'Its yuge: {multiply_by(inputs[0], multiplier)}')
        st.write(f'(p.s i multiplied it by {multiplier})')
    elif app_page == 'sum them':
        st.write(f'summed up: {sum_it(inputs)}')