n = int(input("단어의 개수를 입력하시오\n"))
group_n = n #그룹단어 개수
i = 0


words = map(str, input("단어를 입력하시오\n").split()) #단어를 words에 넣고
words = list(words) #words를 리스트로 만듬
print(words)
for a in range(len(words)): # words의 원소 개수만큼 반복
  for b in range(len(words[a])-1): # words의 a번째 원소의 문자 길이 수만큼 반복
    if words[a][b] == words[a][b+1] :
      continue
    elif words[a][b] in words[a][b+1:]:
        group_n = group_n-1
        break
print(group_n)
