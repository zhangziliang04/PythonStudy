# 实时：实时人脸特征点标定程序设计
import cv2
import dlib

# 重点！！！！：基于自己的路径进行调整
predictor_path = './model/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
win = dlib.image_window()
cap = cv2.VideoCapture(0)
# 从视频流循环帧
while cap.isOpened():
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # 人脸检测
    dets = detector(image, 0)
    win.clear_overlay()
    win.set_image(image)
    print("检测到人脸数量: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))
        # 特征点标定:68
        shape = predictor(image, d)
        print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                  shape.part(1)))
        # Draw the face landmarks on the screen.
        win.add_overlay(shape)
    win.add_overlay(dets)
cap.release()

