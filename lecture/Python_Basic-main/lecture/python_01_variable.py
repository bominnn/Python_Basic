#주석(comment) : 단순 메모, 개발 실행 X
# 출력 함수(print)
#  - ()안에 값을 출력
# - 변수 값 확인 용도 또는 메세지 출력 용도
print("Python")
print("="*200)
# 실행 : ctrl + shift + f10

#문자열 타입(String Type)
# - python : '', "" -- String
# - C, CAVA : ''(Char), ""(String)

#GIT으로 올리기 왼쪽 - open in - explorer - 드래그 드롭

# 참고 : Escape code
# - 문법 : \(역슬러쉬) + @
# - 문자열 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n: 한줄 개행, \t: 탭(8칸 공백)
print('Hello \nPython')
print('Hello \tPython')
print("="*200)


# 자료형 : Type
# - Python의 모든 자료형은 객체(Object)
# - C,JAVA에서 문자형(char): 'A', 'E' 키보드제어 할때 사용. 파이선에서는 없음
# 1) 문자열(sting) : "Hi", 'Hello'
# 2) 정수형(int) : 2, 3
# 3) 실수형(float) : 0.2, -3.14
# 4) 논리형(boolean) : 참,거짓

# 다양한 종류의 자료형을 사용하는 이유
# 예) JAVA - 정수형 : byte, short, int, long
#   Python - 정수형 : int
# 만들어진지 오래된언어는 다양한 자료형을 사용한다.
# 자원(=메모리)을 효율적으로 사용하기 위해서
# 자료형은 담을 수있는 크기의 범위가 지정되어 있음
# 따라서 사용하려는 특정값이상의 자료형을 사용하면 메모리 낭비!

# Python은 동적 타이핑언어 -> Python이 실행 될 때 type를 지정
# - type()함수: ()안의 값의 type을 확인할때 사용
print(type("ABC"))
print(type(123))
print("="*200)


#형 변환(Type Casting)
# - type Casting을 사용하면 값을 원하는 자료형으로 변환가능
# 1) int() : 정수형으로 변환
# 2) float() : 실수형으로 변환
# 3) str() : 문자형으로 변환

# Type Casting 실습
int_a = 3
float_b = 3.14
str_int_c = "9"
str_float_d = "9.2"
# 1) 문자열 정수형("9") -> 정수형(9)
print(int(str_int_c))
# 2) 문자열 정수형("9") -> 실수형(9.0)
print(float(str_int_c))
# 3) 문자열 실수형("9.2") -> 정수형
# print(int(str_float_d)) 에러발생
# 4) 문자열 실수형("9.2") -> 실수형(9.2)
print(float(str_float_d))
# 5) 정수형(3) -> 실수형(3.0)
print(float(int_a))
# 6) 정수형(3) -> 문자열("3")
print(str(int_a))
# 7) 실수형(3.0) -> 정수형(3)
print(int(float_b))
# 8) 실수형(3.14) -> 문자열("3.14")
print(str(float_b))
# * float("Hello"), int("Hello")형 변환불가!
print("="*200)

# None
# - 아무런 값을 갖지않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을때 사용
# - 기타언어의 Null과 같은 의미로 사용!
# C언어 변수생성 : int b; (= 변수 생성, 값은 X)
# Python -> b(= 변수 호출) : 동적이기 때문
# 예) stduent_name
stduent_name = None  #절대 사용금지
stduent_name = ""    #적극 권장
#이유? "Null Pointer Exception" Error 개발자 공포의 대상 프로그램 꺼짐

# 기본 자료형(Primitive Type) : 변수에 값이 저장
# - int num = 4;
# 객체 자료형(Reference Type) : 변수에 값의 "주소"가 저장 = 참조대상이 있어야함
# - stduent_name = "10";
# * JAVA : 기본, 객체 모두 사용
# * Python : 객체만 사용
print("="*200)

# 변수(Variable)
# 변수 : '하나의 값'을 저장할 수 있는 메모리 공간
num = 4
num = 10
print(num)  #출력 : 10
print("="*200)

# - 변수 생성num 및 초기화(= 변수에 값 저장)
# num = 5  #문법
# 대입연산자(=) : 우측의 값(5)을 좌측(num)에 저장
# 동등연산자(==) : Equal

# name  변수 생성
# "Bo Min Kim" 값을 name 변수에 담기

# name(변수명), =(대입연산자), "Bo Min Kim"(값)
name = "Bo Min Kim"

#명령 규칙(Naming Rule)
# *변수, 함수, 클래스 등의 사용자 정의 이름을 붙일 때 사용!
# *명확하고 알아보기 쉽게 짓기!
#
# 1. 영문 대소문자, 숫자, 특수문자(_)만 사용 *외우기
# 2. 숫자로 시작할 수 없음
#    abc1(o), 1abc(x)
# 3. 영어 대소문자 구별
#   abc Abc ABc abC 모두 다른 변수
# 4. 예약어 사용 불가
#   예약어: Python에서 미리 선점하여 사용중인 키워드
#          ex)print, for, while, if, else, class, try, except, True, False
#              and, return, import, def, pass, break, continue, del,...


# Naming Method *******시험에 나옴**********
# - 변수, 함수, 클래스 등의 사용자 정의 이름에 사용하는 기법
# - 프로그래밍 언어별로 사용하는 Naming Method가 다름!

# 1. snake_case: 소문자만 사용, 합성어는(_)사용
#    ex) student_name
# 2. camelCase: 첫 글자 소문자, 합성어 첫글자 대문자
#    ex)studentName
# 3. PascalCase: 첫 글자 대문자, 합성어 첫글자 대문자
#    ex)StudentName


#           변수          함수             클래스
# Java, C  camelCase    camelCase()     PascalCase
# Python   snake_case   snake_case()    PascalCase



# 개발자: web(프론트엔드, 백엔드), 앱(Android, Apple) 웹 퍼블리셔
# 웹 드자이너
# 서버 엔지니어(lINUS 운영관리) + 클라우드 개발자
# 네트워크 엔지니어
# 데이터베이스 엔지니어
# SOL 튜너
# 데이터 모델러
# ERP 개발자
# 보안 개발자
# 인공지능, 데이터분석가, 데이터 사이언티스트, 프롬프트 엔지니어
# 데이터 엔지니어

# 동적 출력!
print("="*200)
student_num = 20223161
student_name = "Bo Min Kim"

# 출력 예: "조선대학교 20223161, Bo Min Kim 입니다."
print("조선대학교 20223161, Bo Min Kim 입니다.") #하드 코딩 지양!

# 1.format()함수 - Old
print("조선대학교 {} , {} 입니다.".format(student_num, student_name))
# 2. f-string - New
print(f"조선대학교 {student_num} , {student_name} 입니다.")

# 간단한 사칙연산
# + : 더하기
# - : 빼기
# * : 곱하기
# / : 나누기
# // : 나누기(몫)
# % : 나누기(나머지)
# ** or ^ : 제곱

# 5/2 : 나누기        2.5
# 5//2 : 나누기(몫)    2
# 5%2 : 나누기(나머지)  1

#문제?
num = 9
num - 1
num + 2
print(num)