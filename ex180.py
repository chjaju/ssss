low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

#volatility 리스트를 만든다.
volatility = []
#리스트에서 각각의 값에 접근하기 위해 for i in range()를 이용한다.
for i in range(5) :
#변동폭을 high_prices[i] - low_prices[i]으로 정의하면 i의 값에 따라 계산된다.
   diff = high_prices[i] - low_prices[i]
   #계산된 변동폭을 volatility 리스트에 추가하기 위해 .append()을 이용한다.
   volatility.append(diff)
    
#volatility리스트에 저장되었는지 확인하기 위해 프린트 해본다.
print(volatility)
#저장된 변동폭 [50, 100, 30, 80, 0]