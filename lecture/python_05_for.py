#제어문
# 1. 조건문(if)
# 2. 반복문(for, while)

#반복문(Loop)
# -반복적인 작업을 가능하게 해주는 도구
# -list, str, tuple, dict, set 등 컬렉션 타입의 아이템을 하나씩 순화하면서 사용가능(for)
# -특정 조건을 만족하는 경우(while)


# 반복횟수 O => for
# 반복횟수 X => while


# *for문 기본문법
# for i in [1, 2 ,3]
#   print(i)

# *range() 함수
# -default: 시작(0), 증감(+1)
# -range(시작, 끝, 증감)
# -range(3)       => 0, 1, 2
# -range(1, 10)   => 1, 2, 3, 4, 5, 6, 7, 8, 9
# -range(2, 5, 2) =>2, 4

# range()를 활용해서 1~9까지 출력하는 for문
for i in range(1, 10):
    print(i)
# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)
# *enumerate()
# 반복횟수(index) 출력하고 싶은 경우!
# -enumerate() : 0번 인덱스부터 시작
for i, alpha in enumerate (temp):
    print(i+1, alpha)

print("="*100)



# dict를 사용한 for문
temp = {"A": 1,
        "B": 2,
        "C": 3,
        "D": 4}
print("="*100)
# dict => for => Key값 출력
# keys(), values(), items()

for element in temp.values():
    print(element)

for key, value in temp.items():
    print("****")
    print(key)   #key
    print(value) #value

# break, continue
# break: 즉시 반목문을 빠져 나가세요.
# continue: 즉시 다음 반복으로 넘어가세요.


a = [1, 2, 3, 4, 5]
#a를 출력하다가 3을 만나면 멈추세요.
for i in a:
    if i == 3:
        break
    print(i)


print("="*100)
# 홀수만 출력
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)


#input() 활용해서 사용자가 입력한 값(2~9) => 해당 단 출력
# 문제1) 입력 된 단수를 출력하는 코드
dan = int(input("단수: "))
for i in range(1, 10):
    print(f"{dan}x{i}={dan*i}")

# 문제2) 구구단 2단 출력
# 2x1=2
# 2x2=4
# ...
# 2x9=18
for i in range(1, 10):
    print(f"2x{i}={2*i}")




print("="*100)
# 2단 9단까지 출력 => 중첩for
for i in range(2, 10):      #2~9단(i)
    for j in range(1, 10):  #단 내에서 1~9
        print(f"{i}x{j}={i*j}")

print("="*100)
# 문제3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total =>총합
total = 0
for num in a:
    total += num # total = total + num
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result, 2)) #평균값

#문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력


