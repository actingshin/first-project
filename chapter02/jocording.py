# int 정수 float 실수형
# 나누기 /  몫 // 나머지 %
from re import I


a = 3
b = 4
print(a/b)

# str 문자열 자료형   \' 면 문자열'이다.
# \n 엔터 역할
# """ 3개 쓰면 그대로 들어감
print("""여기서
이렇게 
써도 된다""")

# 문자열 * 100 이면 100개의 문자가 나옴

# 인덱싱[0~] 숫자의 하나 보여줌  //
# 슬라이싱 ->  v[이상 : 미만 : 간격]

v = "printdk"

print(v[::-1])


# %d 정수 %s 문자열

number = 10
day = "three"
e = "I ate %d apples. so I was sick for %s days. %s days" % (number, day, day)

print(e)


#변수를 줄수있음

a = "dkfjdkfj {name}" .format(name = "신수용")
print(a)


# 소수점 표시하는 %f 에서 / %(사이에)10f 이면 앞에 공백 10칸 생기고
# %(사이에)-5f 이면 뒤로 에 공백 10칸 생김

a = "%10s" % "hi"
print(a)

a = "%-10sjyp" % " hi"
print(a)

# 소수점 표현  %0.4f 면 소수점 4번째 자리 표시
a = "%0.4f" %4.33214

print(a)


#count 숫자 세기

a = "hobby"

print(a.count('b'))

# find 가장 먼자 나오는 인덱스를 몇번째 인덱스 인지 알려준다 / 단, 없는수면 -1 나옴


a = "abcdefghijk"
print(a.find('j'))

# join 문자열 삽입 / upper 소문자를 대문자로 바꾸기 / lower 대문자를 소문자로 바꾸기 / strip 간격없애기

#replace (a,b)   a를 b로 바꾼다.
b = " Life is too short"
print(b.replace("Life", " Your leg"))


#split 뛰어쓰기 위주로 리스트로 나눈다. / ()이거는 띄어쓰기 인데 이거말고도 : 등 문자열로 자를수 있다.

a = "신수용 이정재 이병헌 삼겹살"
print(a.split())

a = "신수용미친이정재미친이병헌미친삼겹살"
print(a.split("미친"))

#리스트에대해
a = a.split("미친")
print(a[1])

#리스트 안에 리스트 만들어서 꺼내기

a = [1,2,3,4,5,[6,7,8]]
print(a[5][2])


# 리스트 끼리 더하면 하나의 리스트로 표현가능

# 리스트 값 수정 및 교체 가능  / []교체하면 빈거라 삭제 = del a[리스트 인덱스]
a = [1,2,3,4,5]
a[3] = 7
print(a)


# 리스트에 추가 append
a = [1,2,3]
a.append(6)
print(a)

# 리스트 정열 sort 를 하면 문자는 가나다 숫자는 123 순으로 정렬이 된다

a = [2,1,3,5]
a.sort()
print(a)


# reverse 하면 거꾸로 나옴

# insert 하면 특정 부분 인덱스에 넣을수있음
a = [1,2,3,4,5]
a.insert(0,4)
print(a)

# remove는 제거를 해주는데 맨 앞에 값만 이거는 인덱스 번호가 아니라 그냥 값이 빠짐

# POP은 리스트 요소 꺼내기
a = [1,2,3,4,5]
print(a.pop())
print(a[0])

#count는 리스트 안에 수를 세어준다

# extend는 확장해준다.


# 57분까지 완료 했습니다. 점프 투 파이썬 조코딩!! 

#--- 5/19 2장

# 튜플 = 자물쇠있는 리스트 값을 변화시킬수 없다.
# 슬라이싱, 더하기, 곱하기는 가능
a = (1,2,3,4)
print(a)

# 딕셔너리 키로 벨류를 부를수 있는것 'ㅁ' : 123    ㅁ이 키 123이 벨류


a = {
    "이름" : "홍길동",
    "성별" : "여자"
}

print(a)

# 리스트 추가 위에 추가하고싶으면 키와 밸류 쓰면 추가

a["크기"] = "거인"
print(a)

# 삭제하고 싶으면 del [키] 넣으면 삭제

#키가 중복되면 안됌


#키 따로 벨류 따로 뽑기
print(a.keys())
print(a.items())  #각 쌍의 키와 벨류를 튜플로 만들기

#get 없는 키를 넣으면 none이라고 나옴

print(a.get(4,"그딴게 어딨엄"))
 
print(1 in a) #a가 1에 있냐


#집합은 중복을 허용하지 않는다 / 집합은 순서가 없다.

s1 = set([1,2,3])
print(type(s1))
s1 = {1,2,3}
print(type(s1))

#1시간 13분

s1 = set("hello")
print(s1)
# 집합은 순서가 없고 각 문자로 중복없이 가져감


#교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))  #  교집합을 새롭게

print(s1|s2)  # 합집합 기호
print(s1.union(s2))

print(s1 - s2) # 차집합
print(s1.difference(s1))

#집합 원소 추가하기
s1 = set([1,2,3,4,5,6])
s1.add(7)
print(s1)

s1.update([7,8,9]) # 한번에 많은거 추가가능

s1.remove(1)  # 집합에서 1이라는 원소 지우기


# 불(리언)은 참 또는 거짓

a = True  # T를 대문자로 써줘야한다.
print(type(a))  # 타입은 불형

# 있는거 진실 없는거(값) 거짓

a =  "안녕"
if a:
    print(a)   # 안녕이 있어서 진실로 받고 출력함


a = [1,2,3,4]
while a:
    a.pop()
    print(a)
    b = "이거 봐라"
    if a:
        print(b)


# 자료형 객체 
a = [1,2,3]
b = a   # b는 a의 주소를 받은개념
a[1] = 4   # b도 1번에 4로 변함
print(a)
print(b)

#그냥 값만 복사하고싶으면
a = [1,2,3]
b =  a[:]
a[1] = 4
print(id(a))
print(id(b))  # 리스트에 값을 준것이기 때문에 주소도 다르고 값도 다르게 나온다 슬라이싱
print(a)
print(b)


a = 3
b = 5
a,b = b,a  # 값을 바꾸는 공식
print(a)
print(b)


#파이썬 구조를 직관적으로 보여주는 사이트 "pythontutor.com/live.html"
#1시간 41분 피곤하다..


#if 문

#여기 그때 해봤던거 쓰기


# for 문
#for 변수 in 리스트(또는 튜플 , 문자열):
    #수행할 문장1

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:  # 파이썬에 for문은 리스트를 순서대로 빼온다.
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for continue문 continue는 if문을 조건으로 부합하면 위로 올라가는 성질

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# range(x, y) 란 x<= ㅇ < y   // in 은 하나씩 빼서 넣는다.

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

#구구단 이중 for문
for i in range(2,10):
    for j in range(1, 10):  # 안쪽 for문임으로 바깥쪽 2를 부여받고 안쪽 for문 다 돌리고 바깥쪽으로 나감 i는 계속 2임
        print(i*j, end=" ")
    print('')

# 리스트 내포
# result = [num * 3 for num in a if num % 2 == 0]

# 2시간 30분까지 완료


