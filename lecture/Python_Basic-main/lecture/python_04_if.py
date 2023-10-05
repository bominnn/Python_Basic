#조건문(Condition) : if~elif~else

# - 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# - 모든 조건은 boolean으로 표현 됨
# - 조건문의 경우 if, elif, else 블록 내 종속된 코든 들여쓰기
# - 모든 블록문의 시작점은 마지막에 :(콜론, colon) 추가
# - python에서 블록 내에 코드는 반드시 들여쓰기(tan) 강제!


# if (조건1){             if 조건1:
#    code                   code
# } else if(조건2){     elif 조건2:
#    code                   code
# }

#제어문 기본 문법 ->1set(chain)
# if 조건1:
#    code
# elif 조건2:
#    code
# elif 조건3:
#    code
# else:
#    code

#->별개의 if문! 3개의 if문!
# if 조건1:
#    code
# if 조건2:
#    code
# if 조건3:
#    code

# 조건문 4가지 조합
# 1. if
# 2. if~elif~elif
# 3. if~else
# 4. if~elif~else

# 점수계산기
# - 91~100 : A
# - 81~90 : B
# - 71~80 : C
# - 61~70 : D
# - 60이하 : F
score = 95 #0~100점

if score>= 91:
    print("A")
elif score>=81:
    print("B")
elif score>=71:
    print("C")
elif score>=61:
    print("D")
else:
    print("F")

# 논리연산자: AND, OR, NOT  **기말고사 필기시험
# 조건 1  조건 2   결과
#   F  and  F      F
#   T  and  F      F
#   F  and  T      F
#   T  and  T      T


# 2. OR
# 조건 1   조건 2   결과
#   F   or   F      F
#   T   or   F      T
#   F   or   T      T
#   F   or   T      T


# 3. NOT
# T -> F
# F -> T


#문제1. 어떤 종류의 학생인지 맞히기?
#(초등, 중등, 고등, 대학생, 학생X)

from datetime import datetime

# input(): 키보드 값 입력 => String(문자열)
born = input("당신이 태어난 년도를 입력하세요: ") #"2004"
today = datetime.today().year
print(today)
age = today -int(born)+1 #2023 - 2004 = 19
print(age)

if 8<=age<26:
    if age>= 20:
        print("대학생")
    elif age>=17:
        print("고등학생")
    elif age>= 14:
        print("중학생")
    elif age >= 8:
        print("초등학생")
else:
    print("학생이 아닙니다.")
 121 changes: 121 additions & 0 deletions121
lecture/python_05_for.py
@@ -0,0 +1,121 @@
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
