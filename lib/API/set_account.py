'''
주식계좌 연결: 한국투자증권 open api 활용 (KoreaInvestment)

정보
1. 한국투자증권의 오픈API의 함수를 사용하려면 API KEY와 API SECRET을 사용하여 토큰을 발급해야합니다. (토큰의 유효기간은 1일)
2. 유효기간이 지났다면 새로 토큰을 발급 받아야 정상적으로 오픈 API를 사용할 수 있습니다.

3. KoreaInvestment 클래스의 객체를 생성하면 생성자에서 토큰을 자동으로 발급하고'token.dat'라는 이름의 파일로 저장합니다. 
'''

import mojito

key = "PS1TI6RNRaKlaBsGw8PW84VY5owerGLNefZT"
secret = "6UKV61FqcRKWiZ0tdgJSstPr3VyCB6TAfJElnQZG76NRDUykXWiQ1OPrbPvD4Smkq+72KVzZ+sRiN1OS3VIqe4bg/wS+th9SHGBjgAlpCccAtdfKW2hGMz7OGl7+/ieiJhJTE9p1uTWPgkjlEBCNcMKFUPEXA31cE2v9MzJawgtMF15De/Y="
acc_no = "50123857-01"

######################################### 증권사 국내주식 객체 생성 ######################################### 
def create_kr_object(key, secret, acc_no):
    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        mock=True # 모의투자 시, 실제 투자시 삭제
    )
    return broker


######################################### 증권사 해외주식 객체 생성 #########################################
def create_na_object(key, secret, acc_no):
    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        exchange='나스닥',
        mock=True # 모의투자 시, 실제 투자시 삭제
    )
    return broker
