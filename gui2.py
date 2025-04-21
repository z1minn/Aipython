import tkinter as tk
from PIL import Image, ImageTk
import os # 파일 경로를 다루기 위해 import

# --- 함수 정의 ---
def show_image(animal_type):
    """선택된 동물 타입에 맞는 이미지를 로드하여 화면에 표시하는 함수"""
    global photo_image # 이미지 참조 유지를 위한 전역 변수 사용

    # 이미지 파일 경로 설정 (스크립트와 같은 디렉토리에 있다고 가정)
    # 파일 확장자가 다를 경우 이 부분을 수정하세요 (예: .png)
    file_name = f"{animal_type}.jpg"
    file_path = os.path.join(os.path.dirname(__file__), file_name) # 스크립트 기준 상대 경로

    try:
        # Pillow를 사용하여 이미지 열기
        pil_image = Image.open(file_path)

        # (선택 사항) 이미지 크기 조정
        max_width = 400
        max_height = 350
        pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        # Pillow 이미지를 Tkinter용 PhotoImage 객체로 변환
        photo_image = ImageTk.PhotoImage(pil_image)

        # 이미지 레이블 업데이트
        image_label.config(image=photo_image, text="") # 기존 텍스트 제거
        image_label.image = photo_image # 레이블 객체에 참조 유지 (가비지 컬렉션 방지)

        print(f"{animal_type} 이미지 로드 완료.")

    except FileNotFoundError:
        error_message = f"오류: '{file_name}' 파일을 찾을 수 없습니다.\n스크립트와 같은 폴더에 있는지 확인하세요."
        print(error_message)
        image_label.config(text=error_message, image='') # 오류 메시지 표시, 기존 이미지 제거
    except Exception as e:
        error_message = f"오류: {file_name} 이미지 로드 중 문제 발생\n{e}"
        print(error_message)
        image_label.config(text=error_message, image='') # 오류 메시지 표시, 기존 이미지 제거

# --- GUI 설정 ---
# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 사진 보기")
window.geometry("500x500") # 초기 창 크기

# 전역 변수 초기화 (이미지 참조 유지를 위해)
photo_image = None

# 버튼을 담을 프레임 생성 (버튼들을 가로로 배치하기 위함)
button_frame = tk.Frame(window)
button_frame.pack(pady=10) # 상단에 여백을 주고 프레임 배치

# 강아지 버튼 생성
# command=lambda: show_image('dog') -> 버튼 클릭 시 show_image 함수에 'dog' 인자를 전달
dog_button = tk.Button(button_frame, text="강아지", width=10, command=lambda: show_image('dog'))
dog_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 고양이 버튼 생성
cat_button = tk.Button(button_frame, text="고양이", width=10, command=lambda: show_image('cat'))
cat_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 토끼 버튼 생성
rabbit_button = tk.Button(button_frame, text="토끼", width=10, command=lambda: show_image('rabbit'))
rabbit_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 이미지를 표시할 레이블 생성
image_label = tk.Label(window, text="버튼을 클릭하여 동물을 선택하세요.", compound=tk.CENTER)
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10) # 창 크기에 맞춰 확장

# --- 메인 루프 시작 ---
window.mainloop()