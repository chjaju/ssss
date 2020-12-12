#ohlc리스트를 정의한다.
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
#수익을 계속 더해주기 위해 for문밖에 total_profit = 0 을 적어준다.
total_profit= 0
#day_price가 ohlc리스트의 1번부터 3번을 바인딩 하기위해 for day_price in ohlc[1:]를 이용한다.
#0번째는 ["open", "high", "low", "close"]이므로 필요없어서 건너뛰는 것이다.
for day_price in ohlc[1:]:
    #수익은 day_price[0] - dayprice[3]이다.
    profit = day_price[0] - day_price[3]
    #수익을 total_profit에 계속 더해준다.
    total_profit += profit
#총 수익금인 total_profit을 프린트한다.
print(total_profit)
#정답=0