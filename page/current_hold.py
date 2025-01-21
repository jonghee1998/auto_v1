import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie
from lib.API.set_account import *
from lib.API.kr_trading import *
from lib.stock.graph import * 

import FinanceDataReader as fdr

############################################ Session State ############################################
st.session_state.load = True
if "stock" not in st.session_state:
    st.session_state.stock = None

def current_hold_page():
    # 주식계좌 연동
    key = "PS1TI6RNRaKlaBsGw8PW84VY5owerGLNefZT"
    secret = "6UKV61FqcRKWiZ0tdgJSstPr3VyCB6TAfJElnQZG76NRDUykXWiQ1OPrbPvD4Smkq+72KVzZ+sRiN1OS3VIqe4bg/wS+th9SHGBjgAlpCccAtdfKW2hGMz7OGl7+/ieiJhJTE9p1uTWPgkjlEBCNcMKFUPEXA31cE2v9MzJawgtMF15De/Y="
    acc_no = "50123857-01"
    broker = create_kr_object(key, secret, acc_no)
    
    # 보유자산 조회
    prvs_rcdl_excc_amt, tot, dnca = get_balance(broker)
    formatted_tot = f"{(tot):,} ₩"  # 소수점 없이 천 단위 쉼표 추가
    formatted_dnca = f"{(dnca):,} ₩"
    
    # 이익률 계산
    profit_loss = tot - prvs_rcdl_excc_amt # 평가손익
    cumulative_return = ((tot / prvs_rcdl_excc_amt) - 1) * 100 # 수익률
    
    # 보유 주식 조회
    pdno, prdt_name, hldg_qty, pchs_amt, evlu_amt = get_holding_stocks(broker)
    
    ############################################ 페이지 구성 ############################################
    
    ### 페이지 제목
    st.markdown("# **보유주식 정보 확인**") 
    st.divider()
    
    ### 페이지 부제목
    st.markdown("##### **보유 자산**") 

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(
            pd.DataFrame({"총평가금액": [formatted_tot]}),
            hide_index=True,
            width=500,
        )
    
    with col2:
        st.dataframe(
            pd.DataFrame({"예수금": [formatted_dnca]}),
            hide_index=True,
            width=500,
        )
    
    with st.container():
        st.dataframe(
            pd.DataFrame({
                "평가손익": [f"{profit_loss:,.0f} 원"],  # 천 단위 쉼표와 '원' 추가
                "수익률": [f"{cumulative_return:.2f} %"]  # 소수점 2자리와 '%' 추가
            }),
            hide_index=True,
            use_container_width=True
        )
    
    ### 페이지 부제목
    st.markdown("##### **보유 주식 현황**") 
    col1, col2 = st.columns(2)
    with col1:
        fig = display_holding_chart(prdt_name, hldg_qty)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        selected_stock = st.selectbox("보유 주식 선택", prdt_name)
        
        prdt_name = ['-' if name == '없음' else name for name in prdt_name]

        # 데이터프레임 생성
        df = pd.DataFrame({
            "종목 코드": pdno,
            "종목명": prdt_name,
            "보유 수량": hldg_qty,
            "매수 금액": pchs_amt,
            "평가 금액": evlu_amt
        })
        
        selected_info = df[df["종목명"] == selected_stock]
        st.dataframe(selected_info.reset_index(drop=True),
                    hide_index=True,
                    use_container_width=True)
                
    ### 페이지 부제목
    st.markdown("##### **환율 Trend (최근 1년)**")
    with st.container():
        exchange_rate = fdr.DataReader('USD/KRW').iloc[-1][0]
        st.write(f'현재 환율: {round(exchange_rate,1)} 원')
        
        fig = display_currency_chart()
        st.plotly_chart(fig, use_container_width=True) 
    
    
    
