import cv2

# 이미지를 읽어옵니다.
image = cv2.imread('rasp_live/setting_1/live_stream/stream/test_img.jpg')

# 이미지를 윈도우 창에 표시합니다.
cv2.imshow('test', image)

# 아무 키나 누를 때까지 기다립니다.
cv2.waitKey(0)

# 모든 창을 닫습니다.
cv2.destroyAllWindows()