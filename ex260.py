class OMG :
    def print() :
        print( "oh my god" )


mystock = OMG()
mystock.print()   
#오류나는 이유  def print()에는 인자값이 없는데 mystock.print()를 호출하면  OMG.print(mystock)로 되기때문에 인자가 없는데 인자가 넘어오기때문에 오류가 뜨는것이다.
