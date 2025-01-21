import streamlit as st
import streamlit_antd_components as sac

from lib.utils.load import load_config, load_image

from page.home_page import home_page
from page.current_hold import current_hold_page
from page.stock_info import stock_information_page
from page.simulation_page import display_simulation_page

import plotly.express as px
import yfinance as yf
import pandas as pd
import time

############################################ Session State ############################################
st.session_state.load = True

# Page config
st.set_page_config(      
    page_title="Stock Prediction & Auto-Trading System",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""<style>span[data-baseweb="tag"] {background-color: #ffffff; color=gray; !important;}</style>""", unsafe_allow_html=True)
congif, readme = load_config("config.toml", "config_readme.toml")

# st.markdown(
#     """
#     <style>
#         [data-testid="stSidebar"][data-testid="stImage"] {
#             text_align: center;
#             display: block;
#             margin-left: auto;
#             margin-right: auto;
#             width: 10px !important;
#         }
#         [data-testid="stSidebar"][data-testid="stImage"] img {
#             width: 10% !important;
#             max_width: 10px !important;
#         }
#     """, unsafe_allow_html=True
# )

# # 사이드바 이미지 추가
# st.sidebar.image(load_image("logo.png"), width=30)
# st.sidebar.markdown('---')
# st.sidebar.markdown('')

########################
st.sidebar.header('Menu')
with st.sidebar.container():
    selected_menu = sac.menu([
        sac.MenuItem(f'{readme["sections"]["home_page"]}'),
        sac.MenuItem(type='divider'),
        sac.MenuItem(f'🏛️ {readme["sections"]["current_hold"]}'),
        sac.MenuItem(type='divider'),
        sac.MenuItem(f'🔍 {readme["sections"]["stock_info"]}'),
        sac.MenuItem(type='divider'),
        sac.MenuItem(f'📈 {readme["sections"]["stock_prediction"]}'),
        sac.MenuItem(type='divider')
    ], variant='filled', format_func='upper', size='md'
    )
if selected_menu == f'{readme["sections"]["home_page"]}':
    home_page()
elif selected_menu == f'🏛️ {readme["sections"]["current_hold"]}':
    current_hold_page()
elif selected_menu == f'🔍 {readme["sections"]["stock_info"]}':  
    stock_information_page()
elif selected_menu == f'📈 {readme["sections"]["stock_prediction"]}':  
    display_simulation_page()




