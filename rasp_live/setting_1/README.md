## 1. 라즈베리파이 OpenCV 설치
### 실시간 웹캠을 스트리밍 하기 위한 OpenCV 설치

- **OpenCV**
    - OpenCV(Open Source Computer Vision)은 오픈 소스 컴퓨터 비전 라이브러리로, 이미지 처리, 컴퓨터 비전 및 기계 학습 알고리즘을 지원하는 강력한 라이브러리이다. Python, C++, Java 등 다양한 언어에서 사용할 수 있으며 일반적으로 Python을 사용하며 정보도 많다.

### Step1.  프로젝트 폴더 생성 및 가상환경 설치

- **라즈베리파이 OS 업데이트**
    
    ```bash
    sudo apt-get -y update && sudo apt-get -y upgrade
    #-- 오래 걸려용~
    ```
    

- **자신이 원하는 이름의 프로젝트 폴더 생성**
    
    ```bash
    mkdir live_stream
    #-- live_stream이라는 이름의 폴더 생성(자신이 원하는 이름으로)
    ```
    
- **생성한 프로젝트 폴더로 이동**
    
    ```bash
    cd live_stream
    ```
    
- **자신이 원하는 이름의 가상환경 설치**
    
    ```bash
    python3 -m venv stream
    #-- stream이라는 이름의 가상환경 설치(자신이 원하는 이름으로)
    ```
    
- 가상환경 실행
    
    ```bash
    source stream/bin/activate # 활성화
    #-- stream이라는 이름의 가상환경 실행
    ```
    

### Step2.  OpenCV 설치

**라즈베리파이 원격 제어를 통해 터미널 실행**

- **OpenCV 설치**
    
    ```bash
    sudo apt install python3-opencv
    #-- 없어도 될듯
    ```
    
    ```bash
    pip install opencv-contrib-python==4.5.1.48
    #-- python 3.7 버전 기준 위 버전을 설치해야 오류가 없음
    ```
    
- **OpenCV 설치 확인**
    
    ```python
    python3 -c 'import cv2;print(cv2.__version__)'
    ```
    

### Step3.  OpenCV 테스트

- **Test 이미지 다운로드**
    
    ```python
    pip install gdown
    gdown "https://drive.google.com/uc?id=1uZdnottKMLRiRg_Qa-asCYkvlOOFw--n"
    ```
    
    ![corgi-g1abb5de4c_1280](https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/41bf134d-7604-461b-b422-5a6f4920ae7a)
    
    픽사베이 무료 이미지
    
- **Test.py 파일 생성**
    
    ```python
    nano test.py
    ```
    
- **OpenCV 샘플 코드 작성**
    
    ```python
    import cv2
    
    # 이미지를 읽어옵니다.
    image = cv2.imread('이미지_파일_경로/이미지_파일_이름.jpg')
    
    # 이미지를 윈도우 창에 표시합니다.
    cv2.imshow('이미지 창 제목', image)
    
    # 아무 키나 누를 때까지 기다립니다.
    cv2.waitKey(0)
    
    # 모든 창을 닫습니다.
    cv2.destroyAllWindows()
    ```
    
- **test.py 파일 실행**

    ```
    python3 test.py
    ```

    ![corgi-g1abb5de4c_1280](https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/41bf134d-7604-461b-b422-5a6f4920ae7a)