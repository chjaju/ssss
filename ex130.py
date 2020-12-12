#아래코드는 비트코인 가격정보를 딕셔너리로 가져온다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#최고가를 high 최저가를 low로 정의한다. float는 소수점이 있을 수 있으므로 한것이다. 그리고 시가도 정의한다.
high= float(btc['max_price'])
low= float(btc['min_price'])
변동폭 =high - low
시가 = float(btc['opening_price'])

#시가+변동폭이 최고가보다 크면 "상승장"을 작으면 "하락장"을 출력하도록 if문을 이용하여 만든다.
if (시가+변동폭) > high:
    print("상승장")
else:
    print("하락장")