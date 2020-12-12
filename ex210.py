#message1이라는 함수를 정의한다. "A"를 프린트한다.
def message1():
    print("A")
#message2라는 함수를 정의한다. "B"를 프린트한다.
def message2():
    print("B")
#message3이라는 함수를 정의하는데 FOR문을 3번 돌리는데 i가 0일때 message2()를 호출하고 "C"를 프린트한다. 이것을 i가 1,2일때도 똑같이 한다.
#for문이 3번 돌면 message1()을 호출한다.
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
#message3()을 출력한다.
message3()
#정답
#B
#C
#B
#C
#B
#C
#A