
print("="*100)
# 문제6) 사용자가 입력한 값 1, 2, 3 통과 아닌 경우 다시 입력하도록
count = 0  #틀린 횟수
while True:
    if count>=3:
        print("프로그램을 사용할 수 없습니다.")
        break
    num = int(input("값: "))
    # if 4> num >0:  # num = 1, 2, 3
    if num in [1, 2, 3]:
        print(f"{num}을 입력하셨습니다.")
        break
    else:
         print("1, 2, 3의 값만 입력해주세요.")
         count+=1

# 문제 7) 1부터 100까지 총합을 출력하는 코드

# - for문으로 작성
for num in range(1, 100):
    total +=num
print(f"총합(for): {total}")

# - while문으로 작성
num = 0
total = 0

while True:
    num +=1
    if num == 101:
        break
    total += num
print("f총합(while): {total}")
