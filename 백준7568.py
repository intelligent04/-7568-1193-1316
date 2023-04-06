i = 0
n = int(input("사람수를 입력하시오"))
for i in range(n): # 사람수만큼 반복
    info = map(int, input("몸무게와 키를 입력하시오\n").split()) #키와 몸무게를 info에 넣음
    info = list(info) #info를 리스트로 만듬
    print(info)