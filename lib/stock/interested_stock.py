def create_stock_dict():
    # 주식 심볼과 세부 정보 매핑 (market_cap 제거, ticker 추가)
    stock_dict = {
        "Samsung Electronics": {
            "name": "삼성전자",
            "sector": "Technology",
            "ticker": "005930",
            "country": "Korea",
        },
        "AAPL": {
            "name": "Apple Inc.",
            "sector": "Technology",
            "ticker": "AAPL",
            "country": "USA",
        },
        "GOOGL": {
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "ticker": "GOOGL",
            "country": "USA",
        },
        "AMZN": {
            "name": "Amazon.com Inc.",
            "sector": "Consumer Discretionary",
            "ticker": "AMZN",
            "country": "USA",
        },
        "MSFT": {
            "name": "Microsoft Corp.",
            "sector": "Technology",
            "ticker": "MSFT",
            "country": "USA",
        },
        "TSLA": {
            "name": "Tesla Inc.",
            "sector": "Automotive",
            "ticker": "TSLA",
            "country": "USA",
        },
        "FB": {
            "name": "Facebook Inc.",
            "sector": "Technology",
            "ticker": "FB",
            "country": "USA",
        },
    }
    return stock_dict
