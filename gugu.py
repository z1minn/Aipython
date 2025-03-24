# 구구단 프로그램 (오류 처리 추가)
try:
    # 사용자로부터 단수 입력받기
    dan = int(input("출력할 구구단의 단수를 입력하세요: "))
    
    # 구구단 출력하기
    print(f"===== {dan}단 =====")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
        
except ValueError:
    print("숫자만 입력해주세요.")