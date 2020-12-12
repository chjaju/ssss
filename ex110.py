#if문이 참이므로 아래있는 else : print("4")는 필요없고 if False:  print("1") print("2")  else: print("3")으로 간후 참이므로 false문으로 가지않고 
#else로 가서 3이 출력된다.
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
#if문이 끝났으므로 5가 또 출력된다.
print("5")
#정답=3,5