# 두 숫자를 입력받아 사칙연산 결과를 모두 출력하는 프로그램 (오류 처리 추가)

try:
    # 사용자로부터 두 숫자 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 사칙연산 수행 및 결과 출력
    print("\n===== 사칙연산 결과 =====")
    print(f"{num1} + {num2} = {num1 + num2}")  # 덧셈
    print(f"{num1} - {num2} = {num1 - num2}")  # 뺄셈
    print(f"{num1} * {num2} = {num1 * num2}")  # 곱셈
    
    # 나눗셈은 0으로 나누는 경우를 처리
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")  # 나눗셈
    else:
        print(f"{num1} / {num2} = 0으로 나눌 수 없습니다.")
        
except ValueError:
    print("유효한 숫자를 입력해주세요.")