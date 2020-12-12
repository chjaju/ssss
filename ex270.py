class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend
#리스트를 만든다.
종목 = []
#stock클래스의 객채를 각각 만들어준다.
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

#리스트에다 append명령어를 이용하여 객채들을 넣어준다.
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

#for문을 이용하면 종목이라는 리스트안의 개체가 나온다. i는 삼성,현대차,LG전자를 바인딩 한다.
for i in 종목:
    print(i.code, i.per)  
#종목코드와 per을 출력하기 위해 i.code, i.per을 프린트 한다.
#정답
#005930 15.79
#005380 8.7
#066570 317.34