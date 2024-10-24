# 6047

# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

# 출력(1) 거듭제곱 사용
a,b=map(int,input().split())
print(a*(2**b))

#출력(2) 비프시프트 사용 -> 더 빠름
a,b=map(int,input().split())
print(a<<b)

#비프시프트 총 정리
#왼쪽 연산 << : a << b == a * (2 ** b), 
# a의 이진수 표현을 왼쪽으로 b만큼 이동, 숫자가 2의 b제곱 만큼 커짐
# a << 1은 a * 2**1 = a * 2
# a << 2는 a * 2**2 = a * 4
# a << 3은 a * 2**3 = a * 8

#오른쪽 연산 >> : a >> b == a // (2 ** b),
# a의 이진수 표현을 오른쪽으로 b만큼 이동, 숫자가 1/2씩 줄어듦
# a >> 1은 a // 2**1 (1비트 오른쪽 이동은 2로 나누는 것과 같음)
# a >> 2는 a // 2**2 (2비트 오른쪽 이동은 4로 나누는 것과 같음)
# a >> 3은 a // 2**3 (3비트 오른쪽 이동은 8로 나누는 것과 같음)

