#per리스트를 정의한다.
per = ["10.31", "", "8.00"]

for i in per:
    #실행 코드이다.
    try:
        print(float(i))
    #예외가 발생하면 0으로 프린트하는 코드이다.
    except:
        print(0)
    #예외 발생안하면 clean data 를 프린트하는 코드이다.
    else:
        print("clean data")
    #예외에 상관없이 수행되는 코드이다.
    finally:
        print("변환 완료")
#정답
#10.31
#clean data
#변환 완료
#0
#변환 완료
#8.0
#clean data
#변환 완료