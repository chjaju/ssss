#초기값을 1로 설정한다.
result = 1
#i의 값이 증가 될때마다 result값이 result * i 로 새로 나오는 반복문을 i가 10이 될때까지 반복한다
for i in range(1, 11) :
   result = result * i
#i가 10이 될때까지 반복해서 나온 result값을 출력한다.
print(result)
#정답=3628800