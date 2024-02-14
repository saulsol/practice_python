import platform

print(platform.python_version())
print("파이썬 첫 걸음")

# 문자열 합치기
head = "python "
tail = "is fun"
print(head + tail)

# 문자열 곱하기
a = "python"
print(a * 2)

# 문자열 길이 구하기
a = "life is short"
print("문자열 길이 구하기 : " + str(len(a)))
# int 값을 String 값으로 변환 " str()
# 문자열 길이 함수 len()

# 문자열 인덱싱
a = "Life is fun"
print(a[3])

# 문자열 뒤애서 읽기
print(a[-0] + a[-1])
# a[-0]은 같은 a[0] 과 같은 값을 보여준다.

# 문자열 슬라이싱
print(a[0:4])
# life 가 출력된다 끝 번호는 출력되지 않는다.
# 0 <= a < 3
print(a[0:])
# 끝 번호를 생략하면 시작 인덱스 부터 끝까지 모두 나온다.

a = "20010331Rainy"
date = a[:8]
print(date)
whether = a[8:]
print(whether)


# 문자 개수 세기(count)
a = "hubby"
print(a.count('b'))
# 문자열에서 b의 개수를 세어준다.

print(a.find('x')) # 없으면 -1 반환

# 문자열 조인
print(",".join('ㅁㅁㅁㅁ'))
# String의 char에 하나씩 String 값을 하나씩 대입해준다.

# 대문자 변환
a = a.upper()
print(a)
# 소문자 변환
print(a.lower())

# 문자열 나누기
a = "life is too short"
print(a.split())
# 아무 값도 입력하지 않으면 공백을 기준으로 split

b = "a:b:c:d"
print(b.split(':'))






