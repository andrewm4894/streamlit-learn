import streamlit as st


@st.cache
def do_uppercase(some_string):
    return some_string.upper()


@st.cache
def do_concat(strings_to_concat, sep=' '):
    return f'{sep}'.join(strings_to_concat)