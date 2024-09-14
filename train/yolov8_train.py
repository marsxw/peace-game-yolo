#%%
from ultralytics import YOLO
from ultralytics import settings
import os 
if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))

    settings.reset()
    runs_dir = './runs'
    os.system(f'rm -rf {runs_dir}')
    settings.update({'runs_dir': runs_dir})

    
    model = YOLO('./config/yolov8.yaml') 
    results = model.train(data='./config/coco.yaml', epochs=300)
    results = model.val()
    # results = model('https://ultralytics.com/images/bus.jpg')
    success = model.export(format='onnx')
#%%
# import os
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# from ultralytics import YOLO
# from ultralytics import settings
# settings.reset()
# runs_dir = '/huangwenxi/ultralytics/runs'
# import os
# os.system(f'rm -rf {runs_dir}')
# settings.update({'runs_dir': runs_dir})
# #%%
# model = YOLO('yolov8n.yaml')
# # model.train(data='/huangwenxi/ultralytics/dataset_seg/coco8-seg.yaml',  epochs=3, imgsz=640)
# # results = model.val()
# # results = model('/huangwenxi/ultralytics/dataset/yolo_dataset/images/test/2024030151521_116690.jpg')
# success = model.export(format='onnx')


