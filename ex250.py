#numpy모듈을 import한다.
import numpy
#그냥 range는 실수단위로 증가가 안되는 반면 numpy.arange는 실수 단위로도 증가시키게 만들 수 있다. 0부터 5까지 0.1씩 증가한다.
for i in numpy.arange(0, 5, 0.1):
   print(i)
#프린트한다.