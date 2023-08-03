## 실시간 웹캠을 스트리밍

### Step0.  Flask 설치

**Flask** 

Flask는 파이썬으로 웹 애플리케이션을 개발하기 위한 간단하고 가벼운 마이크로 웹 프레임워크이다.  Flask는 모듈화가 잘 되어 있고, 확장성이 뛰어나며, 초보자부터 전문가까지 쉽게 사용할 수 있다. 간단한 웹 애플리케이션부터 복잡한 웹 사이트까지 다양한 용도로 사용할 수 있다.

- 터미널에서 flask 설치

```bash
python3 -m pip install --upgrade pip
#-- pip 업데이트
```

```bash
pip install Flask
```

### Step1.  프로젝트 폴더에 추가 폴더 및 파일 생성

- **현재 파일 경로/live_stream**
    
    ```bash
    mkdir templates
    
    ```
    
- **templates 폴더 안에 index.html 파일 생성 후 다음 코드 입력**
    
    ```bash
    <html>
    	<head>
    		<meta charset="utf-8">
    		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    			  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    		<title>STREAMING</title>
    	</head>
    <body>
    	<div class="container">
    		<div class="row">
    			<div class="col-lg-8  offset-lg-2">
    				<h3 class="mt-5">Live Streaming</h3> 
    				<img src="{{ url_for('Stream') }}" width="100%"> #-- URL이랑 flask router 함수랑 똑같게 해야함
    			</div>
    		</div>
    	</div>
    </body>
    </html>
    ```
    
- **flask 스트리밍 stream.py  코드 작성**
    
    ```python
    from flask import Flask, render_template, Response
    from time import sleep
    import cv2
    
    app = Flask(__name__)
    capture = cv2.VideoCapture(0)  # 웹캠으로부터 비디오 캡처 객체 생성
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 캡처된 비디오의 폭 설정
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 캡처된 비디오의 높이 설정
    
    def GenerateFrames():
        while True:
            sleep(0.1)  # 프레임 생성 간격을 잠시 지연시킵니다.
            ref, frame = capture.read()  # 비디오 프레임을 읽어옵니다.
            if not ref:  # 비디오 프레임을 제대로 읽어오지 못했다면 반복문을 종료합니다.
                break
            else:
                ref, buffer = cv2.imencode('.jpg', frame)  # JPEG 형식으로 이미지를 인코딩합니다.
                frame = buffer.tobytes()  # 인코딩된 이미지를 바이트 스트림으로 변환합니다.
                # multipart/x-mixed-replace 포맷으로 비디오 프레임을 클라이언트에게 반환합니다.
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    @app.route('/')
    def Index():
        return render_template('index.html')  # index.html 파일을 렌더링하여 반환합니다.
    
    @app.route('/stream')
    def Stream():
        # GenerateFrames 함수를 통해 비디오 프레임을 클라이언트에게 실시간으로 반환합니다.
        return Response(GenerateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    if __name__ == "__main__":
        # 라즈베리파이의 IP 번호와 포트 번호를 지정하여 Flask 앱을 실행합니다.
        app.run(host="자신의IP주소", port="8080")
    ```
    
- **전체 파일 구조**
    
    ```bash
    ...
    |-- live_stream
    |-- stream.py
    |-- templates
    |   └── index.html
    ```
    

#— 자신의 IP 번호를 모른다면 터미널에서 다음 명령어 수행 후 

```bash
ifconfig | grep inet
```

### Step2.  Falsk 스트리밍 확인

- **스트리밍 서버 코드 실행**
    
    ```bash
    python3 stream.py
    ```
    
- **이후 자신의 IP주소 + 포트번호로 GET 요청**
    
    ```bash
    http://자신의IP주소:8080/stream
    ```
    
    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcMDrg0%2FbtspUn4CiWS%2FQF2ya1Zd4kkoPJrus4ixN0%2Fimg.png)





    잘 나온당
