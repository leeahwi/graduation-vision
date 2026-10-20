# 원본 이력과 통합 내역

## 원본 저장소

| 원본 | 통합 폴더 | 기준 커밋 | 원본 커밋 수 |
| --- | --- | --- | --- |
| [leeahwi/RosLaneDetection](https://github.com/leeahwi/RosLaneDetection) | `ros-lane-detection/` | `40ecffb79132c888453c8f384484093d992f28ee` | 1 |
| [leeahwi/Live_LaneDetection](https://github.com/leeahwi/Live_LaneDetection) | `lane-detection/` | `561db5fed3f1d524d4251297bee7e56814b220ac` | 6 |
| [leeahwi/Live_ObjectDetection](https://github.com/leeahwi/Live_ObjectDetection) | `object-detection/` | `5ae827aa96603682948fb0d42b3ea0ac66036415` | 2 |

일반 파일 복사 대신 각 원본을 별도 부모 이력으로 병합했습니다. 원본 커밋은 모두 새 `main`의 조상으로 남으며, 원래 커밋의 파일 경로는 당시 저장소 루트 기준입니다. 원본 기준점에는 `source/<원본 저장소명>` 태그도 붙였습니다.

## 최소 변경

- C++: 두 프로젝트를 루트 CMake에서 함께 빌드하도록 구성했습니다. 기존 OpenCV/GSL 의존성은 유지하며 개인 OpenCV 설치 경로와 C++ 표준 설정 오타를 제거했습니다.
- 차선 인식: 선택적인 영상 경로 인자를 추가했습니다. 기본 영상 경로와 결과 파일 이름은 유지했습니다.
- 객체 인식: 개인 경로 대신 클래스 목록과 모델 경로 인자를 사용하며, 클래스 목록이 없으면 카메라 접근 전에 오류로 종료합니다.
- ROS: 테스트 이미지를 스크립트 상대 경로에서 읽고, 기본 노드의 두 줄 들여쓰기를 수정했습니다. 노드 실행 권한과 catkin 설치 구성을 보완했습니다.
- 현재 트리에서 원본 ROS `build/`와 `ransac_1d.pyc`를 제거했습니다. 해당 파일과 원본 소스는 과거 커밋에서 확인할 수 있습니다.
- 패키지 이름·기존 저작자 정보·라이선스 placeholder·인식 알고리즘·토픽·임계값은 유지했습니다.

## 기존 외부 출처

차선 인식 `main.cpp`에는 [georgesung/road_lane_line_detection](https://github.com/georgesung/road_lane_line_detection)과 [webnautes 글](https://webnautes.tistory.com/1186)이 원본·수정 출처로 기재되어 있습니다. 이 표기를 유지합니다.

YOLOv5s 모델과 영상 파일은 원본 저장소에 포함된 파일을 그대로 가져왔습니다. 모델 변환 버전이나 모든 영상의 최초 제작자는 원본 자료만으로 확인하지 못했습니다. 전체 저장소에 적용할 새 라이선스는 추가하지 않았습니다.
