# int 정수 float 실수형
# 나누기 /  몫 // 나머지 %
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

a = "%10s" % " hi"
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
print(a)

#count는 리스트 안에 수를 세어준다

# extend는 확장해준다.


# 57분까지 완료 했습니다. 점프 투 파이썬 조코딩!! s