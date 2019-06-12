# 实时：实时人脸检测
import cv2
import dlib

# 基于5特征点的人脸检测
detector = dlib.get_frontal_face_detector()
win = dlib.image_window()
cap = cv2.VideoCapture(0)

# 从视频流循环帧
while cap.isOpened():
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # 检测灰度帧中的人脸
    dets = detector(image, 0)
    print("检测到人脸数量: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))
    win.clear_overlay()
    win.set_image(image)
    win.add_overlay(dets)
cap.release()
