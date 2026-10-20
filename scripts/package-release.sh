#!/usr/bin/env bash
set -euo pipefail
# Run only after a successful Ubuntu 22.04 x86_64 build and verified data restore.
repo_root=$(cd "$(dirname "$0")/.." && pwd)
cd "$repo_root"
output=${1:-dist}
mkdir -p "$output"
output=$(cd "$output" && pwd)
staging=$(mktemp -d)
trap 'rm -rf "$staging"' EXIT
bundle=graduation-vision-ubuntu-22.04-x86_64
mkdir -p "$staging/$bundle/bin"
install -m 755 build/lane-detection/Live_LaneDetection "$staging/$bundle/bin/"
install -m 755 build/object-detection/Live_ObjectDetection "$staging/$bundle/bin/"
cp docs/releases/BINARY-README.md "$staging/$bundle/README.md"
cp docs/PROVENANCE.md "$staging/$bundle/PROVENANCE.md"
ldd "$staging/$bundle/bin/Live_LaneDetection" > "$staging/$bundle/linked-libraries.txt"
ldd "$staging/$bundle/bin/Live_ObjectDetection" >> "$staging/$bundle/linked-libraries.txt"
if grep -q 'not found' "$staging/$bundle/linked-libraries.txt"; then
  echo 'Missing linked libraries' >&2
  exit 1
fi
tar -C "$staging" -czf "$output/$bundle.tar.gz" "$bundle"
mkdir -p "$staging/ros-source/hg_lineDetection"
cp -R ros-lane-detection/. "$staging/ros-source/hg_lineDetection/"
cp docs/releases/ROS-README.md "$staging/ros-source/README.md"
cp docs/PROVENANCE.md "$staging/ros-source/PROVENANCE.md"
tar -C "$staging/ros-source" -czf "$output/graduation-vision-ros-catkin-source.tar.gz" .
# Data was verified against the committed manifest by fetch-release-data.py.
cp release-data/graduation-vision-sample-videos.tar.gz "$output/"
cp release-data/graduation-vision-yolov5-assets.tar.gz "$output/"
cp docs/releases/data-manifest.json "$output/"
(cd "$output" && sha256sum ./*.tar.gz data-manifest.json > SHA256SUMS)
