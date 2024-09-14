#%%
import cv2
import numpy as np
image_path = 'd:/game_yolov8/test/6.jpg'
image = cv2.imread(image_path) 
# image = cv2.imread(image_path)[400:600, 900:1200, :] 
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

 
# 转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义红色的HSV范围  创建掩模
lower_red1 = np.array([0, 200, 240])
upper_red1 = np.array([5, 255, 255]) 
mask = cv2.inRange(hsv, lower_red1, upper_red1)
 
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 对掩模应用一些形态学变换以去除噪声
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


# 检测圆形
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, param1=50, param2=15, minRadius=5, maxRadius=50)

# 确保至少找到一个圆
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # 在图像上绘制圆
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # 显示结果
    cv2.imshow("Detected Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles were found.")

#%%
import numpy as np
import cv2

# 定义 RGB 颜色值列表
rgbs = np.array([  [ (250,52,47)]], dtype=np.uint8)

# 将 RGB 颜色值转换为 HSV 颜色值
hsvs = cv2.cvtColor(rgbs.reshape(-1, 1, 3), cv2.COLOR_RGB2HSV)

# 计算 HSV 颜色值的平均值
hsv_mean = np.mean(hsvs, axis=0).astype(np.uint8)

# 打印结果
print("RGB颜色值列表:")
print(rgbs)
print("\n对应的HSV平均值:")
print(hsv_mean)

 

# %%
 