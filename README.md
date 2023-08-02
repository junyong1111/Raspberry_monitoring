# Raspberry_monitoring

## 라즈베리파이 초기 설정

### 1. **운영체제에 맞게 Imager SW 다운로드**

[Raspberry Pi OS - Raspberry Pi](https://www.raspberrypi.com/software/)

### 2. **라즈베리파이 이미지 다운로드(오래 걸림)**

[Operating system images - Raspberry Pi](https://www.raspberrypi.com/software/operating-systems/)

### 3. Image SW를 실행 **(오래 걸림)**

사용자 정의 사용 → 다운받은 이미지 삽입 + 노트북에 SD카드 삽입

<img width="683" alt="1" src="https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/df64bff1-126a-4179-9f48-b5019ad4d8f3">


<img width="687" alt="2" src="https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/8c31fb89-33ae-40f5-b3d4-4adf5817cdca">

**주의: 실수로 저장소를 노트북의 내장 SSD를 선택할 경우 노트북의 운영체제가 파괴한다.**

### 4. SD제거 전 기본 설정

- **노트북에서 USB microSD카드의 /boot 폴더에 빈 ssh 파일 생성**

```bash
cd /Volumes/boot
touch ssh
```

- **/boot 폴더의 cmdline.txt 편집**

```bash
sudo nano cmdline.txt
```

```bash
// cmdlin.txt
console=serial0,115200 console=tty1 root=PARTUUID=d9b3f436-02 
rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles 
ip="자신의 IP 주소"
```

**이후 안전하게 SD 카드를 제거 후 라즈베리파이에 SD카드 삽입 후 2~5분 정도 대기**

### 5. 노트북 유선랜 설정

<img width="258" alt="3" src="https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/3ab6fad0-dc15-4f8a-a117-ae680f47a4ca">

<img width="665" alt="4" src="https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/53928800-cea1-4934-bca7-13a0e66b901a">

<img width="671" alt="5" src="https://github.com/junyong1111/Raspberry_monitoring/assets/79856225/a4a7e51f-e743-4896-b104-2da70b2fb046">
