import mojito
import pprint


# resp = broker.fetch_balance()

# 현재가 조회 (장 종료시 종가)
def get_current_price(broker, ticker):
    resp = broker.fetch_price(ticker) # 이중 딕셔너리 타입으로 리턴, 이후 두개의 키값을 통해 값들 반환
    open = resp['output']['stck_oprc']  # 시가
    high =  resp['output']['stck_hgpr'] # 고가
    row = resp['output']['stck_lwpr']   # 저가
    close = resp['output']['stck_prpr'] # 종가
    
    return open, high, row, close

# 종목코드 조회
def get_stock_code(broker):
    symbols = broker.fetch_symbols()
    
    return symbols

# 잔고 조회
def get_balance(broker):
    resp = broker.fetch_balance()
    for comp in resp['output2']:
        prvs_rcdl_excc_amt = comp['prvs_rcdl_excc_amt']  # 초기 투자 금액
        tot = comp['tot_evlu_amt'] # 총평가금액         # 총 자산의 현재 평가 가치
        dnca = comp['dnca_tot_amt'] # 예수금            # 잔여 시드머니
    return float(prvs_rcdl_excc_amt), float(tot), float(dnca)
 
# 보유 종목 조회
def get_holding_stocks(broker):

    resp = broker.fetch_balance()
    pdno, prdt_name, hldg_qty, pchs_amt, evlu_amt = [], [], [], [], []
    
    # output1이 비어있지 않은 경우 데이터를 처리
    if resp['output1']:
        for comp in resp['output1']:
            pdno.append(comp.get('pdno', '-'))          # 종목 코드
            prdt_name.append(comp.get('prdt_name', '-'))  # 종목명
            hldg_qty.append(comp.get('hldg_qty', '0'))   # 보유 수량
            pchs_amt.append(comp.get('pchs_amt', '0'))  # 매수 금액
            evlu_amt.append(comp.get('evlu_amt', '0'))  # 평가 금액
    else:
        # output1이 비어있는 경우 기본값 추가
        pdno.append('-')
        prdt_name.append('없음')
        hldg_qty.append(0)
        pchs_amt.append(0)
        evlu_amt.append(0)

    return pdno, prdt_name, hldg_qty, pchs_amt, evlu_amt

#########################################################################################################################
'''
매수 기본정보 
1. 시장가 매매: 시장의 가격에 맞춰 알아서 주문을 넣는 방식입니다. 따라서 가격을 입력할 필요는 없고 수량만 입력하면 됩니다.
2. 지정 매매: 해당 호가에 주문을 넣은 순서대로 주문수량이 누적되며 해당 가격에서 주문 순서에 맞춰 체결됩니다. 지정가 주문을 할 때 가격과 수량을 입력해야합니다.

주식을 매도할 때 부르는 가격을 매도 호가라고 하고, 매수할 때 부르는 가격을 매수 호가라고 합니다.

호가에는 가격 단위가 존재하며 이 규칙에 맞게 호가를 제출해야 정상적으로 거래가 진행됩니다. 
예를 들어, 삼성전자의 현재가가 60,000원이라면 100 단위의 호가만 유효합니다. 
즉, 60,100, 60,200원은 정상적인 호가이지만 60,050원은 호가의 가격단위에 맞지 않아서 정상적으로 주문이 진행되지 않습니다.
'''
# 시장가 매수
def buy_stock_market(broker, ticker, quantity):
    resp = broker.create_market_buy_order(
        symbol=ticker,
        quantity=quantity
    )
    # msg = resp['msg1']
    # rt_cd = resp['rt_cd']
    # msg_cd = resp['msg_cd]
    # output = resp['output']
    
    return resp # 수정 예정

# 지정가 매수
def buy_stock_limit(broker, ticker, price, quantity):
    resp = broker.create_limit_buy_order(
        symbol=ticker,
        price=price,
        quantity=quantity
    )
    return resp 

# 시장가 매도
def sell_stock_market(broker, ticker, quantity):
    resp = broker.create_market_sell_order(
        symbol=ticker,
        quantity=quantity
    )
    return resp

# 지정가 매도
def sell_stock_limit(broker, ticker, price, quantity):
    resp = broker.create_limit_sell_order(
        symbol=ticker,
        price=price,
        quantity=quantity
    )
    return resp
    

# 전체 수량 주문 취소
'''
org_no, order_no 는 주문 메서드의 리턴인 resp 중 output에서 구함
'''
def cancel_order_all(broker, org_no, order_no, quantity):
    resp = broker.cancel_order(
        org_no=org_no,
        order_no=order_no,
        quantity=quantity,  # 잔량전부 취소시 원주문 수량과 일치해야함
        total=True   # 잔량전부를 의미
    )
    return resp


# 일부 수량 주문 취소
def cancel_order_partial(broker, org_no, order_no, quantity):
    resp = broker.cancel_order(
        org_no=org_no,
        order_no=order_no,
        quantity=quantity,  # 취소수량
        total=False   # 잔량전부 x 의미
    )
    return resp


# 주문 정정
'''
org_no, order_no 는 주문 메서드의 리턴인 resp 중 output에서 구함
'''
def change_order_all(broker, org_no, order_no, price, quantity):
    resp = broker.modify_order(
        org_no=org_no,
        order_no=order_no,
        order_type="00",
        price=price,
        quantity=quantity,
        total=True
    )
    return resp

def change_order_partial(broker, org_no, order_no, price, quantity):
    resp = broker.modify_order(
        org_no=org_no,
        order_no=order_no,
        order_type="00",
        price=price,
        quantity=quantity,
        total=False
    )
    return resp
    
    