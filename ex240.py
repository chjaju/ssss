#4.여기서 num은 14이고 14 * 2를 한 28이 최종값이다. 그 후 아래에 있는 함수에서 num(28) 값을 계속 return한다.
def 함수0(num) :
    return num * 2
#3.여기서 num은 12이고 또 함수0을 호출한다.
def 함수1(num) :
    return 함수0(num + 2)
#2.c에서 num이 2이므로 2+10을 한 12가 num이된다. 그리고 함수1을 호출한다.
def 함수2(num) :
    num = num + 10
    return 함수1(num)
#1.함수 2가 호출된다.
c = 함수2(2)
#5.최종적으로 28이 c값이된다.
print(c)
#정답=28