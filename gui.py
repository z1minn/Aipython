import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os # 파일 경로 관련 작업을 위해 추가

# GUI 창 생성
window = tk.Tk()
window.title("간단 이미지 뷰어")
window.geometry("600x500") # 창 초기 크기 설정

# 이미지를 표시할 라벨 생성
# 처음에는 비어있는 상태로 둡니다.
image_label = tk.Label(window)
image_label.pack(pady=20) # 라벨을 창에 배치하고 상하 여백 추가

# 이미지 파일을 열고 화면에 표시하는 함수
def open_image():
    # 파일 열기 대화상자 실행
    # initialdir: 처음 열릴 디렉토리 (여기서는 현재 스크립트 실행 위치)
    # title: 대화상자 제목
    # filetypes: 선택 가능한 파일 종류 지정
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(), # 현재 작업 디렉토리에서 시작
        title="이미지 파일 선택",
        filetypes=(("이미지 파일", "*.png *.jpg *.jpeg *.gif *.bmp"), ("모든 파일", "*.*"))
    )

    # 사용자가 파일을 선택했는지 확인
    if file_path:
        try:
            # Pillow를 사용하여 이미지 열기
            img = Image.open(file_path)

            # --- 이미지 크기 조절 (선택 사항) ---
            # 이미지가 너무 크면 창 크기에 맞게 조절할 수 있습니다.
            max_width = 500
            max_height = 400
            img.thumbnail((max_width, max_height)) # 원본 비율 유지하며 최대 크기 제한
            # ---------------------------------

            # 이미지를 Tkinter에서 사용할 수 있는 형태로 변환
            tk_image = ImageTk.PhotoImage(img)

            # 라벨의 이미지를 업데이트
            image_label.config(image=tk_image)

            # *** 중요 ***: 이미지 객체에 대한 참조 유지
            # 함수 내에서 생성된 tk_image 객체는 함수 종료 시 가비지 컬렉션될 수 있으므로,
            # 라벨의 속성으로 저장하여 참조를 유지해야 이미지가 사라지지 않습니다.
            image_label.image = tk_image

            # 창 제목에 파일 이름 표시 (선택 사항)
            window.title(f"간단 이미지 뷰어 - {os.path.basename(file_path)}")

        except Exception as e:
            # 이미지 파일이 아니거나 문제가 있을 경우 오류 메시지 출력 (터미널)
            print(f"이미지를 여는 중 오류 발생: {e}")
            # 사용자에게 알림 (선택 사항 - 메시지 박스 등 사용 가능)
            image_label.config(image=None, text=f"이미지 로드 실패:\n{os.path.basename(file_path)}")
            image_label.image = None # 참조 제거


# "이미지 열기" 버튼 생성
# command=open_image : 버튼 클릭 시 open_image 함수 실행
open_button = tk.Button(window, text="이미지 열기", command=open_image)
open_button.pack(pady=10) # 버튼을 창에 배치하고 상하 여백 추가

# GUI 이벤트 루프 시작 (창을 화면에 표시하고 사용자 입력 대기)
window.mainloop()