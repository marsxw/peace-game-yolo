 
#%%
import os
import xml.etree.ElementTree as ET
import sys
current_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_path)

#在voc目录下生成对应的txt
class_dict = ["enemy"] 
voc_folder = './dataset_voc'    

for xml_file in os.listdir(voc_folder):
    if xml_file.endswith('.xml'):
        tree = ET.parse(os.path.join(voc_folder, xml_file))
        root = tree.getroot()

        txt_file = os.path.splitext(xml_file)[0] + '.txt'
        txt_path = os.path.join(voc_folder, txt_file)

        with open(txt_path, 'w') as f:
            for obj in root.findall('object'):
                cls = obj.find('name').text
                cls_num = class_dict.index(cls)
                bbox = obj.find('bndbox')
                x_center = (float(bbox.find('xmin').text) + float(bbox.find('xmax').text)) / 2
                y_center = (float(bbox.find('ymin').text) + float(bbox.find('ymax').text)) / 2
                width = float(bbox.find('xmax').text) - float(bbox.find('xmin').text)
                height = float(bbox.find('ymax').text) - float(bbox.find('ymin').text)
                x_center /= 1280
                y_center /= 720
                width /= 1280
                height /= 720

                txt_context = f"{cls_num} {x_center} {y_center} {width} {height}\n"
                f.write(txt_context)

#%%
# 按照8:1:1划分训练集、验证集和测试集
import os
import random
import shutil

output_folder = "dataset_yolo"
if   os.path.exists(output_folder):
    shutil.rmtree(output_folder)
paths = []
paths.append(f"{output_folder}/train/images")
paths.append(f"{output_folder}/train/labels")
paths.append(f"{output_folder}/val/images")
paths.append(f"{output_folder}/val/labels")
paths.append(f"{output_folder}/test/images")
paths.append(f"{output_folder}/test/labels")

for each in paths:
    if not os.path.exists(each):
        os.makedirs(each)
 
images = []
for each in os.listdir(voc_folder):
    if each.endswith('.jpg'):
        images.append(each)

random.shuffle(images)
images_num = len(images)
train_num = int(images_num * 0.8)
val_num = int(images_num * 0.1)
test_num = images_num - train_num - val_num
for  each_file in images[:train_num]:
    #复制到train
    shutil.copy(f"{voc_folder}/{each_file}", f"{output_folder}/train/images")
    shutil.copy(f"{voc_folder}/{os.path.splitext(each_file)[0]}.txt", f"{output_folder}/train/labels")
for  each_file in images[train_num:train_num+val_num]:
    #复制到val
    shutil.copy(f"{voc_folder}/{each_file}", f"{output_folder}/val/images")
    shutil.copy(f"{voc_folder}/{os.path.splitext(each_file)[0]}.txt", f"{output_folder}/val/labels")
for  each_file in images[train_num+val_num:]:
    #复制到test
    shutil.copy(f"{voc_folder}/{each_file}", f"{output_folder}/test/images")
    shutil.copy(f"{voc_folder}/{os.path.splitext(each_file)[0]}.txt", f"{output_folder}/test/labels")
# %%
#%%
 