import streamlit as st  
import plotly.graph_objects as go
from lib.API.kr_trading import *
import FinanceDataReader as fdr
from datetime import datetime, timedelta
import pandas as pd


#  Streamlit 페이지
def display_holding_chart(prdt_name, hldg_qty):
    # 데이터 확인
    if not prdt_name or not hldg_qty or sum(hldg_qty) == 0:
        # 보유 주식이 없는 경우 기본값 설정
        prdt_name = ['없음']
        hldg_qty = [1]  # Plotly 차트에서 0값을 처리하기 위한 기본값
        colors = ['gray']
    else:
        # 보유 주식이 있는 경우
        colors = None  # 기본 색상 사용

    # Plotly 도넛 차트 생성
    fig = go.Figure(data=[go.Pie(
        labels=prdt_name,
        values=hldg_qty,
        hole=0.5,  # 도넛 모양
        textinfo='label+percent',
        insidetextorientation='radial',
        marker=dict(colors=colors)  # 색상 처리
    )])
    
    # 도넛 차트 레이아웃 설정
    fig.update_layout(
        # showlegend=True,
        # title_x=0.5
    )

    return fig


def display_currency_chart():
    
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)

    # USD/KRW 환율 정보 가져오기 (1년 치 데이터)
    exchange_rate = fdr.DataReader('USD/KRW', start=start_date, end=end_date)

    # Plotly 라인 차트 생성
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=exchange_rate.index,
        y=exchange_rate['Close'],
        mode='lines',
        name='USD/KRW 환율',
        line=dict(width=2)
    ))

    # 차트 레이아웃 설정
    fig.update_layout(
        title="USD/KRW 환율 변동 (Close)",
        xaxis_title="날짜",
        yaxis_title="환율",
        template="plotly_white"
    )
    
    return fig

def display_daily_stock_chart(broker, ticker):
    resp = broker.fetch_ohlcv(
        symbol=ticker,
        timeframe='D',
        adj_price=True
    )
    df = pd.DataFrame(resp['output2'])
    df['date'] = pd.to_datetime(df['stck_bsop_date'], format="%Y%m%d")
    df = df[['date', 'stck_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_clpr']]
    df.columns = ['date', 'Open', 'High', 'Low', 'Close']
    df = df.sort_values(by='date')
    return df

def display_candle_chart(df):
    # 이동평균 계산
    df["MA_10"] = df["Close"].rolling(window=10).mean()  # 10일 이동평균
    df["MA_20"] = df["Close"].rolling(window=20).mean()  # 20일 이동평균
    df["MA_50"] = df["Close"].rolling(window=50).mean()  # 50일 이동평균

    # Plotly 캔들차트 생성
    fig = go.Figure()

    # 캔들차트 추가
    fig.add_trace(go.Candlestick(
        x=df["date"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Candlestick"
    ))

    # MA 라인 추가
    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["MA_10"],
        mode="lines",
        name="MA 10",
        line=dict(width=1, color="blue")
    ))

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["MA_20"],
        mode="lines",
        name="MA 20",
        line=dict(width=1, color="green")
    ))

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["MA_50"],
        mode="lines",
        name="MA 50",
        line=dict(width=1, color="red")
    ))

    # 레이아웃 설정
    fig.update_layout(
        title="Candlestick Chart",
        xaxis_title="date",
        yaxis_title="Price",
        template="plotly_white",
        xaxis_rangeslider_visible=False  # 하단 슬라이더 비활성화
    )
    
    return fig



























