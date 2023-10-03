# coding = utf-8
import cv2 as cv
import sys
import numpy as np

print("微信二维码识别")
cameIdx = 0

try:
    detector = cv.wechat_qrcode.WeChatQRCode("detect.prototxt", "detect.caffemodel",
                                             "sr.prototxt", "sr.caffemodel")
except:
    print("-" * 50)
    print("初始化模块失败！请检查模块是否存在或是否已经损坏！")
    print("-" * 50)
    sys.exit(0)

# 打开摄像头
cap = cv.VideoCapture(cameIdx)
while True:
    # 读入
    res, img = cap.read()
    if img is None:
        break

    # 识别
    res, points = detector.detectAndDecode(img)

    # 绘制位置并输出
    for idx in range(len(points)):
        box = points[idx].astype(np.int32)
        cv.drawContours(img, [box], -1, (0, 255, 0), 3)
        print(f"二维码{idx}: {res[idx]}")

    cv.imshow("Check QRcode", img)
    # 关闭
    if cv.waitKey(30) >= 0:
        break


cap.release()
cv.destroyAllWindows()
