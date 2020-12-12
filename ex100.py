#date와 close_price를 리스트로 정의한다
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
#close_table을 딕셔너리로 만들기 위해 dict함수를 이용하고 그안에 두개의 리스트를 zip하면 0번은 0번끼리 1번은 1번끼리 만들어진다.
close_table = dict(zip(date, close_price))
#close_table을 print한다.
print(close_table)
#정답={'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}