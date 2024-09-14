#%% 
import os, sys,cv2
os.chdir(os.path.dirname(__file__))

# 获取 所以mp4文件
mp4_files = [f for f in os.listdir() if f.endswith('.mp4')]

for mp4_file in mp4_files:
    print(mp4_file)
    cap = cv2.VideoCapture(mp4_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_cnt = 0
    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        frame_cnt += 1

        if frame_cnt%10==0 :
            if not os.path.exists('./image'):
                os.mkdir('./image')
            img_name = f"./image/{mp4_file.split('.')[0]}_{frame_cnt}.jpg"
            cv2.imwrite( img_name, frame)
    
# %%
import os, sys,cv2
os.chdir(os.path.dirname(__file__))
image_path = "./image"
images , xmls = [], []
for each in os.listdir(image_path):
    if each.endswith('.jpg'):
        images.append(each)
    elif each.endswith('.xml'):
        xmls.append(each)

# 去掉image中 有xml 但是没有jpg图片的文件
for xml in xmls:
    if xml.split('.')[0]+'.jpg' not in images:
        os.remove(os.path.join(image_path,xml))
        print(f"remove xml {xml}")


# 去掉xml中 有jpg 但是没有xml图片的文件
for image in images:
    if image.split('.')[0]+'.xml' not in xmls:
        os.remove(os.path.join(image_path,image))
        print(f"remove image {image}") 
#%%
 