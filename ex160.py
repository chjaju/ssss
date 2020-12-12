#리스트를 정의한다.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#for문을 사용하고 split(".")을 이용하여 문자열을 .을 기점으로 분리하고 확장자가 h이거나 c이면 파일 이름을 출력하게 한다.
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)
#정답= intra.h
#    intra.c
#    define.h