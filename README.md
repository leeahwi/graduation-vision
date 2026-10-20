# Graduation Vision · 차선 및 객체 인식 졸업 프로젝트

[![Verify graduation projects](https://github.com/leeahwi/graduation-vision/actions/workflows/verify.yml/badge.svg)](https://github.com/leeahwi/graduation-vision/actions/workflows/verify.yml)

졸업 과제를 위해 개발한 **OpenCV 차선 인식, YOLOv5 객체 인식, ROS 차선 인식**을 한곳에 모은 저장소입니다. 각 프로젝트의 원본 커밋 이력과 실험 자료를 보존하고, 공통 빌드와 실행 안내를 추가했습니다.

세 모듈은 독립 실행 프로그램입니다. 하나의 프로세스나 ROS 파이프라인으로 연결하는 작업은 포함하지 않습니다.

## 프로젝트 구성

| 폴더 | 역할 | 주요 기술 / 입력 |
| --- | --- | --- |
| [`lane-detection/`](lane-detection/) | 도로 영상에서 좌우 차선 검출·시각화 | C++17, OpenCV, GSL / MP4 영상 |
| [`object-detection/`](object-detection/) | 웹캠 영상에서 객체 검출·라벨 표시 | C++17, OpenCV DNN, YOLOv5s ONNX / 카메라 0 |
| [`ros-lane-detection/`](ros-lane-detection/) | ROS 카메라 영상에서 차선과 주행 방향 계산 | Python, ROS 1, OpenCV, NumPy, Matplotlib / 이미지 토픽 |

차선 인식은 색상 필터, ROI, Canny/Hough 변환과 선형 회귀를 사용합니다. ROS 모듈에는 기본·Diff·Hough 변형이 있으며, 객체 인식에는 기존 `yolov5s.onnx`와 COCO 클래스 목록을 사용합니다. 원본 영상과 모델은 아래 릴리스에서 내려받습니다.

## 배포 파일 다운로드

**[v1.0.0 Releases](https://github.com/leeahwi/graduation-vision/releases/tag/v1.0.0)**에서 내려받을 수 있습니다.

| 파일 | 내용 |
| --- | --- |
| `graduation-vision-ubuntu-22.04-x86_64.tar.gz` | Ubuntu 22.04 x86_64용 C++ 실행 파일 2개, 설치·실행 안내, 동적 라이브러리 목록 |
| `graduation-vision-sample-videos.tar.gz` | 원본 실험 영상 5개 |
| `graduation-vision-yolov5-assets.tar.gz` | 기존 ONNX 모델과 COCO 클래스 목록 |
| `graduation-vision-ros-catkin-source.tar.gz` | ROS 1/catkin 패키지 소스와 실행 안내 |
| `SHA256SUMS`, `data-manifest.json` | 배포 파일 및 원본 입력 파일의 SHA-256 |

실행 파일은 시스템 OpenCV/GSL에 동적으로 연결됩니다. Ubuntu 22.04 x86_64에서 `sudo apt-get install libopencv-dev libgsl-dev`로 준비하고, 실행 파일 압축 안의 README를 따라 실행하세요. 다른 운영체제·CPU에서는 소스로 빌드합니다. ROS는 소스로 제공하며 별도 catkin 환경이 필요합니다.

소스 저장소에서 영상과 모델을 복원하려면 Python 3으로 다음 명령을 실행합니다. 저장된 SHA-256으로 압축 파일과 각 원본 파일을 검사한 뒤 기존 경로에 복원합니다.

```bash
python3 scripts/fetch-release-data.py
```

수동으로 영상·모델 압축을 저장소 루트에 풀어도 같은 경로가 만들어집니다. 파일은 Git 현재 트리에서 분리했으며 과거 커밋과 출처 이력에는 그대로 남아 있습니다. 따라서 전체 Git 이력을 clone할 때의 크기는 줄어들지 않습니다.

## C++ 프로젝트 빌드

필요한 도구는 CMake 3.16 이상, C++17 컴파일러, OpenCV, GSL입니다. Debian/Ubuntu 계열에서 기존 의존성을 설치하고 저장소 루트에서 빌드합니다.

```bash
sudo apt-get update
sudo apt-get install build-essential cmake libopencv-dev libgsl-dev

git clone https://github.com/leeahwi/graduation-vision.git
cd graduation-vision
python3 scripts/fetch-release-data.py
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel 2
```

OpenCV를 직접 설치했다면 구성 명령에 `-DOpenCV_DIR=/path/to/opencv/lib/cmake/opencv4`를 추가할 수 있습니다. ROS 패키지는 아래 catkin 절차로 별도 빌드합니다.

### 영상 차선 인식

저장소 루트에서 실행합니다.

```bash
./build/lane-detection/Live_LaneDetection lane-detection/challenge.mp4
```

첫 번째 인자로 다른 영상 경로를 지정할 수 있습니다. 인자를 생략하면 원본과 같은 `../challenge.mp4`를 사용합니다. 결과는 실행 폴더의 `live.avi`와 `img_annota1ted.jpg`에 저장되고 GUI 창에 표시됩니다. 종료는 `ESC`입니다. 영상 디코더와 XVID 인코더가 필요합니다.

기존 실험 자료 `KoreaTechLaneDetectionExample1.mp4`, `P1_example.mp4`, `raw-lines-example.mp4`, `solidWhiteRight.mp4`도 영상 릴리스 압축에 보존했으며, 복원하면 `lane-detection/`에 생성됩니다.

### 웹캠 객체 인식

저장소 루트에서 실행합니다.

```bash
./build/object-detection/Live_ObjectDetection   object-detection/coco.names   object-detection/yolov5s.onnx
```

첫 번째 인자는 클래스 목록, 두 번째 인자는 모델 파일입니다. 생략 시 각각 `../coco.names`, `../yolov5s.onnx`를 사용합니다. 카메라는 원본과 같이 장치 `0`을 사용하며 아무 키나 누르면 종료됩니다. GUI와 카메라 사용 권한이 필요합니다.

후처리는 포함된 모델의 출력 형상인 `25200 × 85`를 전제로 합니다. 다른 YOLO 모델로 교체하려면 후처리도 함께 검토해야 합니다.

## ROS 차선 인식

패키지 이름은 원본의 **`hg_lineDetection`**을 유지합니다. 원본 저장소는 ROS Melodic용으로 설명되어 있으며, ROS 1/catkin, `rospy`, `roscpp`, `std_msgs`, `sensor_msgs`, `cv_bridge`, `image_transport`, 그리고 Python용 OpenCV·NumPy·Matplotlib이 필요합니다. 사용 중인 ROS 배포판에 맞는 Python과 `cv_bridge` 조합을 준비해야 합니다.

아래 예시는 ROS가 준비된 Linux 환경에서 실행합니다. `GRADUATION_VISION_ROOT`는 clone한 저장소의 실제 경로입니다.

```bash
GRADUATION_VISION_ROOT=/absolute/path/to/graduation-vision
mkdir -p ~/catkin_ws/src
ln -s "$GRADUATION_VISION_ROOT/ros-lane-detection" ~/catkin_ws/src/hg_lineDetection
cd ~/catkin_ws
catkin_make
source devel/setup.bash

roslaunch hg_lineDetection lineDetection.launch
# 다른 변형은 하나씩 선택하여 실행
# roslaunch hg_lineDetection lineDetectionDiff.launch
# roslaunch hg_lineDetection lineDetectionHough.launch
```

카메라 노드는 별도로 실행해야 하며, 기본 입력은 **`/stereo/left/image_raw`** (`sensor_msgs/Image`)입니다. 입력 토픽이 다르면 roslaunch 실행 시 `/stereo/left/image_raw:=/your/camera/topic`을 뒤에 붙일 수 있습니다.

| 변형 | 기본 수치 출력 | 진단 영상 |
| --- | --- | --- |
| 기본 / Hough | `lane_pub` (`std_msgs/Float64`) | `/lane/raw_image`, `/lane/bev_image`, `/lane/filter_image`, `/lane/left_roi`, `/lane/right_roi` |
| Diff | `lane_left`, `lane_right` (`std_msgs/Float64`) | 위와 동일 |

상대 토픽 이름의 실제 전체 경로는 ROS 네임스페이스에 따라 달라집니다. 진단 시각화는 원본의 640×480 영상 가정을 포함합니다. launch 파일의 `publish`, `save` 파라미터는 현재 코드에서 읽지 않습니다.

## 통합 범위와 검증

- 세 저장소의 원본 커밋 9개를 병합 이력 안에 보존했습니다. 출처별 기준 커밋은 [`docs/source-repositories.json`](docs/source-repositories.json)에 기록했습니다.
- 인식 알고리즘과 임계값은 유지했습니다. 개인 컴퓨터 절대 경로, CMake 빌드 설정, ROS 실행 파일 설치, 기존 들여쓰기 오류를 정리했습니다.
- 영상·모델은 체크섬을 포함한 릴리스 자산에 보존하고 이미지·클래스 목록은 소스에도 유지했습니다. 또한 `build/`와 `.pyc` 같은 생성 파일은 현재 파일 목록에서 제외했습니다. 이전 파일은 Git 이력에 남아 있습니다.
- GitHub Actions는 C++ 두 프로그램의 Ubuntu 빌드, 없는 입력에 대한 종료 동작, Python 문법과 ROS XML 구문, 원본 데이터 체크섬을 확인하고 배포 압축과 체크섬을 생성합니다. `v*` 태그를 push하면 초안 릴리스를 준비하며, 영상·모델은 변경하지 않은 v1.0.0 기준 자산을 재사용합니다. 실제 검사 결과는 위 배지의 실행 기록을 확인하세요.
- GUI 영상 재생, 웹캠 추론, ROS/catkin 빌드와 실제 로봇 연결은 이 통합 과정에서 검증하지 않았습니다. 기존 Python 2/3 나눗셈 차이, 고정 영상 크기와 검출 개수 등의 제약도 남아 있습니다.

## 출처와 라이선스

원본 저장소와 변경 범위는 [`docs/PROVENANCE.md`](docs/PROVENANCE.md)에 정리했습니다. 기존 코드의 저작자·출처 표기를 유지합니다. 원본에는 통일된 라이선스가 없고 ROS manifest의 라이선스도 `TODO`이므로, 이 저장소에 새로운 전체 라이선스를 부여하지 않았습니다. 외부 코드·모델·영상의 재사용 조건은 각 원출처에서 확인해야 합니다.
