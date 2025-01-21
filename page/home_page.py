import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie

############################################ Session State ############################################
st.session_state.load = True
if "stock" not in st.session_state:
    st.session_state.stock = None


def home_page():
    
    st.markdown(
    """
    # 📈 **예측 모델 기반 자동매매 프로그램**
    
    ### **보유 기능 정리**

    **정해진 로직 기반으로 보유 주식 및 관심 주식회사들의 동향을 바탕으로 자동매매를 진행하기 위해 만들어진 대시보드입니다.**
    
    ## 🏗️ **상세 기능**

    - **한국투자증권 API** - 한국투자증권 API를 활용해 주식 계좌를 연동하여 실시간 보유 내역 확인 및 자동매매 가능함 (현재 Demo: 모의계좌)
    - **Data Pipeline** - 야후 파이낸스, 미국 경제지표 등등 다양한 지표를 크롤링이나 오픈 API를 활용해 데이터풀 생성함
    - **Prediction Model** - 모델은 현재 구상 중이며, LSTM, Multioutput Regressor 등으로 예측 진행 중
    - **Auto Trade Mechanism** - 생성된 예측 모델의 결과를 바탕으로, 자동매매 로직에 의거하여 매매 진행
    """
    )   