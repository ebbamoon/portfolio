import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages.home import show_home
from pages.install import show_install
from pages.user_guide import show_user_guide
from pages.api import show_api
from pages.examples import show_examples
from pages.community import show_community

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["install", "user_guide", "api", "examples", "community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": show_home,
    "Install": show_install,
    "User Guide": show_user_guide,
    "API": show_api,
    "Examples": show_examples,
    "Community": show_community,
}
go_to = functions.get(page)
if go_to:
    go_to()