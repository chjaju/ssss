class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()
#자식 클래스의 객체가 생성될때 생성자가 호출이되고 먼저 자식생성을 프린트한다. 그후 super().__init__() 구문을 이용했으므로 부모클래스의 생성자를 호출하기 때문데 부모생성이 프린트된다.
#정답 
#자식생성
#부모생성