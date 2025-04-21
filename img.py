from PIL import Image
import os

# 이미지 파일 경로 (실제 파일 경로로 변경하세요)
image_path = 'input.png'

try:
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지 정보 출력
    print(f"이미지 형식: {img.format}")
    print(f"이미지 크기 (가로x세로): {img.size}")
    print(f"이미지 모드: {img.mode}") # 'RGB', 'L'(흑백), 'RGBA'(투명도 포함) 등

    # 이미지를 화면에 표시 (기본 이미지 뷰어 사용)
    img.show()

    # 사용 후에는 파일을 닫아주는 것이 좋습니다.
    img.close()

except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다 - {image_path}")
except Exception as e:
    print(f"이미지 처리 중 오류 발생: {e}")