# 2장 연습문제
kor = 80
eng = 75
mat= 55
avg = (kor + eng + mat) / 3
print("홍길동의 과목 평균은 %d 입니다." % avg )


#3번
a = "881120-1068234"
print(a[:6])
print(a[7:])

#4번
pin = "881120-1068234"
print(pin[7])

#5번
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


#6번
li = [1,3,5,4,2]
li.sort()
li.reverse()
print(li)

#7번
a = ['Life','is', 'too', 'short']
for b in a:
    print(b)  # 이건 내가 한거 한줄로 안되네..ㅋㅋ

a = ['Life','is', 'too', 'short']
print(a)
result = " ".join(a)  # " " 각 리스트 마다 공백을 주고 연결한다.


#8번 튜플은 비밀 사물함이다. 그러니 튜플안에 다른 튜플을 넣어진행한것
a = (1,2,3)
a = a + (4,)
print(a)


#10번
a = {'a' : 90, 'b' : 80, 'c' : 70}
result = a.pop('b')
print(a)
print(result)

#11번
a = [1,1,1,2,2,2,3,4,4,5,5]
aSet = set(a)
b = list(aSet)
print(b)


#12번
a = b = [1,2,3]
a[1] = 4
print(b)