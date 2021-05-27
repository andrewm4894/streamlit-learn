# streamlit-learn

![litt_up](./assets/app_a_litt_up.jpg)  
*im sorry, i hate it too but i'm leaving it in*

## Overview 

This is a silly dumb streamlit app to try and show an example of a few things:

- Some notion of a multipage app where each app can have itself different "screens" or "pages".
- A `src` type folder where you might write custom python modules you want to have available to all your "apps" or "screens" within the app.
- Ability to easily deploy it to https://streamlit.io/sharing for example this app should be up and available [here](https://share.streamlit.io/andrewm4894/streamlit-learn/main/app.py).
- Show different logos etc on different pages.
- Have dynamic inputs that can vary in types and number of inputs depending on each page.
- Some functions to do stuff with the inputs.

Blog post: https://andrewm4894.com/2021/05/27/streamlit-multi-page-app-minimal-example/
App running on Streamlit sharing: https://share.streamlit.io/andrewm4894/streamlit-learn/main/app.py

### Apps

These are meant to be very dumb and pointless app's :) 

#### "silly string stuff"

Has two pages:
1. "uppercase it" - just takes some input and makes it uppercase.
2. "concatinator" - take two string inputs and concatenate them.

#### "crazy numbers"

Has two pages:
1. "make it yuge" - take a number and multiplies it by some random big number.
2. "sum them" - takes two numbers and sums them.

### Structure

Here are each of the main folders/files and what they do.

- `/.streamlit` - This is where some streamlit specific config files like `config.toml` live, more info in streamlit docs [here](https://docs.streamlit.io/en/stable/streamlit_configuration.html).
- `/apps` - This is where we have an `app_<name>.py` file for each app within our overall streamlit app. For example, `/apps/app_silly_strings.py` contains as much of the logic and code that is specific to the "silly string stuff" app.
- `/assets` - The place where your images and other similar types of files live that you want to use across your apps.
- `/src` - For python code and functions you want to have available on any page of your app you can make a custom module in here. For example the `funny_numbers` module has the functions used by the "crazy numbers" app.
- `app.py` - This is the main streamlit app we launch via `streamlit run app.py` which will import and render the other apps as needed.
- `Pipfile` - Pipenv is used in this example instead of a requirements.txt or any other approaches to define the python environment the app should run in.

### todo

Some maybe todo's.

- Use classes more to better abstract out each app. Some nice ideas in [here](https://github.com/YanAlmeida/streamlit-multipage-framework).
- Add example of testing in some sense. Maybe read [here](https://blog.streamlit.io/testing-streamlit-apps-using-seleniumbase/) for more info.
- Add a github workflow for automated testing.
- Build out the example to do something bigger that would depend on sharing state across pages or apps. For example, some data preprocessing that you want to only do once and then have the resulting data be available to all pages. 
- Add some interactive charts. Lots of nice examples in streamlit gallery of how to do this. 