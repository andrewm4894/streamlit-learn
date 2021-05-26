import streamlit as st
import apps.app_silly_strings as app_silly_strings
import apps.app_crazy_numbers as app_crazy_numbers

# define app pages
app_pages = {
    app_silly_strings.app_dict['name']: app_silly_strings.app_dict['pages'],
    app_crazy_numbers.app_dict['name']: app_crazy_numbers.app_dict['pages'],
}

# generic inputs
st.sidebar.markdown('## Navigation')
app_selected = st.sidebar.selectbox('Select App', list(app_pages.keys()))
app_page = st.sidebar.selectbox('App Page', app_pages[app_selected])

# app specific inputs
st.sidebar.markdown('## Inputs')
if app_selected == app_silly_strings.app_dict['name']:
    inputs = app_silly_strings.create_inputs(app_page)
elif app_selected == app_crazy_numbers.app_dict['name']:
    inputs = app_crazy_numbers.create_inputs(app_page)

# button to run app
app_run = st.sidebar.button('Run')

# render results
if app_run or app_page:
    if app_selected == app_silly_strings.app_dict['name']:
        app_silly_strings.render_results(inputs, app_page)
    elif app_selected == app_crazy_numbers.app_dict['name']:
        app_crazy_numbers.render_results(inputs, app_page)

