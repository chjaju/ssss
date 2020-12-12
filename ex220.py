#print_max함수를 정의한다.
def print_max(a, b, c) :
    #만약 a가 b,c보다 크다면 a를 프린트하라.
    if a>b and a>c :
        print(a)
    #그렇지않고 b가 a,c보다 크면 b를 프린트하라.
    elif b>c and b>a :
        print(b)
    #위의모두가 아니면 c가 가장 크다.
    else :
        print(c)
#예를 들어 print_max(15,14,21)을 출력해보자
print_max(15,14,21)
#출력해보면 21이 나온다.      