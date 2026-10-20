# Graduation Vision v1.0.0 — Ubuntu 22.04 x86_64

These two C++17 executables were compiled in GitHub Actions on Ubuntu 22.04 x86_64 with distribution OpenCV and GSL. They are dynamically linked, not universal Linux binaries. Use Ubuntu 22.04 x86_64 (or build source on your own platform).

## Dependencies and assets

```bash
sudo apt-get update
sudo apt-get install libopencv-dev libgsl-dev
```

Download all three archives and SHA256SUMS from https://github.com/leeahwi/graduation-vision/releases/tag/v1.0.0 into the same directory. SHA256SUMS also lists the optional ROS archive and data-manifest.json; download those if you want to verify the entire list. For only downloaded files:

```bash
sha256sum --ignore-missing -c SHA256SUMS
tar -xzf graduation-vision-ubuntu-22.04-x86_64.tar.gz
tar -xzf graduation-vision-sample-videos.tar.gz
tar -xzf graduation-vision-yolov5-assets.tar.gz
./graduation-vision-ubuntu-22.04-x86_64/bin/Live_LaneDetection lane-detection/challenge.mp4
./graduation-vision-ubuntu-22.04-x86_64/bin/Live_ObjectDetection object-detection/coco.names object-detection/yolov5s.onnx
```

Run from the directory where the archives were extracted. Lane detection accepts a video path, shows a window and writes live.avi/img_annota1ted.jpg in the current directory; press ESC to exit. Object detection uses camera 0 and exits on any key. It requires a webcam and display session; the supplied model expects 25200 × 85 output. XVID and video decoding support must be available in OpenCV.

## Verification and limits

CI compiled both programs, checked missing-input failure and recorded linked libraries in linked-libraries.txt. Original input file hashes were verified. No GUI playback, camera inference, real-time performance, ROS or robot runtime was tested. These are preserved graduation experiments, with original thresholds and assumptions.

Original sources: https://github.com/leeahwi/graduation-vision — see PROVENANCE.md. No new license is granted over third-party source, models or videos.
