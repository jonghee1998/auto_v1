import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie

############################################ Session State ############################################
st.session_state.load = True
if 'stock' not in st.session_state:
    st.session_state.stock = None

def display_simulation_page():
    st.header('주식예측 및 자동매매 시스템')
    st.write('1. 데이터 수집 및 전처리를 통한 상/하락장 파악')
    st.write('2. 특정 주식 시장 파악 및 해당 주식 예측')
    st.write('3. 주식예측 결과에 대한 EDA 및 시각화')
    st.write('4. 예측 결과를 통한 자동매매 시스템 구축')
    st.write('5. 자동매매 시스템을 통한 수익률 분석')

    with st.empty():        
        tab = sac.tabs([
            sac.TabsItem(label = '현보유 확인'),
            sac.TabsItem(label = '상/하락장 확인'),
            sac.TabsItem(label = '관심종목 확인'),
            sac.TabsItem(label = '예측종목 선택'),
            
        ], size='sm', use_container_width=True)

    ##############################################################################################################################
    #################################################   현보유 확인   ###############################################################
    ##############################################################################################################################
        if tab == '현보유 확인':
            st.write('업로드 확인')


