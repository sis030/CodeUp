# 6042

# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

# 출력
a = float(input())
print(format(a, '.2f'))

#format(수, .0f) : 소수점 원하는 자리까지 정확하게 반올림 된 실수값 생성
#소수점 출력 시 형식으로 지정하는 방법-> format() 또는 f-string / 소수점 자릿수 반올림만 해주는거->round()
