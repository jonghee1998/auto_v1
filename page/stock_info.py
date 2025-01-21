import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie

from lib.stock.graph import * 
from lib.API.set_account import *
from lib.API.kr_trading import *

from lib.stock.interested_stock import create_stock_dict
############################################ Session State ############################################
st.session_state.load = True
if "stock" not in st.session_state:
    st.session_state.stock = None

# Add a heading
key = "PS1TI6RNRaKlaBsGw8PW84VY5owerGLNefZT"
secret = "6UKV61FqcRKWiZ0tdgJSstPr3VyCB6TAfJElnQZG76NRDUykXWiQ1OPrbPvD4Smkq+72KVzZ+sRiN1OS3VIqe4bg/wS+th9SHGBjgAlpCccAtdfKW2hGMz7OGl7+/ieiJhJTE9p1uTWPgkjlEBCNcMKFUPEXA31cE2v9MzJawgtMF15De/Y="
acc_no = "50123857-01"

broker = create_kr_object(key, secret, acc_no)

################################################################################################################################
def stock_information_page():
    ### 사이드바 작업
    st.sidebar.markdown("## **User Input Features**")
    stock_dict = create_stock_dict()
    if st.session_state.stock is None:
        st.session_state.stock = list(stock_dict.keys())[0]  # 첫 번째 값을 기본값으로 설정
    else:
        st.session_state.stock = st.sidebar.selectbox(
            "Choose a stock",
            options=list(stock_dict.keys()),
            index=list(stock_dict.keys()).index(st.session_state.stock)
        )
    stock = st.session_state.stock
    ticker = stock_dict[stock]["ticker"]
    open, high, row, close = get_current_price(broker, ticker)

    
    ### 선택된 주식에 대한 정보 표시
    st.markdown("## **Basic Information**")
    
    col1, col2 = st.columns(2)
    col1.dataframe(
        pd.DataFrame({"Issuer Name": [stock_dict[stock]["name"]]}),
        hide_index=True,
        width=500)
            
    col2.dataframe(
        pd.DataFrame({"Sector": [stock_dict[stock]["sector"]]}),
        hide_index=True,
        width=500)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.dataframe(
        pd.DataFrame({"Open": [open]}),
        hide_index=True,
        width=500)
    
    col2.dataframe(
        pd.DataFrame({"High": [high]}),
        hide_index=True,
        width=500)
    
    col3.dataframe(
        pd.DataFrame({"Low": [row]}),
        hide_index=True,
        width=500)
    
    col4.dataframe(
        pd.DataFrame({"Close": [close]}),
        hide_index=True,
        width=500)
            

    with st.container():
        df = display_daily_stock_chart(broker, ticker)
        fig = display_candle_chart(df)
        st.plotly_chart(fig, use_container_width=True) 
        
    


    # with st.empty():        
    #     tab = sac.tabs([
    #         sac.TabsItem(label = '현보유 확인'),
    #         sac.TabsItem(label = '상/하락장 확인'),
    #         sac.TabsItem(label = '관심종목 확인'),
    #         sac.TabsItem(label = '예측종목 선택'),
            
    #     ], size='sm', use_container_width=True)

    # ##############################################################################################################################
    # #################################################   현보유 확인   ###############################################################
    # ##############################################################################################################################
    #     if tab == '현보유 확인':
    #         st.write('업로드 확인')

