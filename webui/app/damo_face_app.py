
import os
os.system("pip install 'mmengine>=0.6.0'")
os.system("pip install 'mmcv>=2.0.0rc4,<2.1.0'")
os.system("pip install 'mmdet>=3.0.0,<4.0.0'")
# os.system("pip install mmcv-full==1.7.0")
# os.system("pip install 'mmengine'")
# os.system("pip install 'mmdet'")
os.system("pip install tensorflow")
os.system("pip install modelscope")

import cv2
import gradio as gr
import numpy as np
import PIL.Image as Image
import torch
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.utils.cv.image_utils import draw_face_detection_result
from modelscope.preprocessors.image import LoadImage

import warnings

warnings.filterwarnings("ignore")


# 定义推理函数
def detect_faces(img_pil, model_name):
    # 定义模型
    face_detection = pipeline(task=Tasks.face_detection, model='damo/cv_ddsar_face-detection_iclr23-damofd')
    img_dir = "input_img.jpg"
    img_pil.save(img_dir)
    # 进行人脸检测
    result = face_detection(img_dir)
    # 可视化结果
    img_cv = draw_face_detection_result(img_dir, result)
    # 将结果转换为 Gradio 的输出格式
    img_out_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    return img_out_pil

def download_test_image():
    # Images
    torch.hub.download_url_to_file(
        'https://user-images.githubusercontent.com/59380685/269160118-91a4a758-1ee0-47a3-a873-28bfd8c24a7f.jpg',
        'faces.jpg')
    torch.hub.download_url_to_file(
        'https://user-images.githubusercontent.com/59380685/269160674-bbf4af8b-a5f1-4754-a272-fd7d278050a3.jpg',
        '000000000110.jpg')


easyface_model_list = ['damo/cv_ddsar_face-detection_iclr23-damofd',
                       'damo/cv_resnet101_face-detection_cvpr22papermogface',
                       'damo/cv_resnet50_face-detection_retinaface',
                       'damo/cv_manual_face-detection_mtcnn']

if __name__ == '__main__':
    download_test_image()
    # 定义输入和输出
    inputs = gr.inputs.Image(type='pil', label="input")
    model_name = gr.inputs.Dropdown(choices=easyface_model_list, label="model list",
                                    default="damo/cv_ddsar_face-detection_iclr23-damofd")
    example = [["faces.jpg", "damo/cv_ddsar_face-detection_iclr23-damofd"],
               ["000000000110.jpg", "damo/cv_manual_face-detection_mtcnn"]]
    outputs = gr.outputs.Image(type='pil', label="output")
    title = "EasyFace Web Demo"
    description = "EasyFace旨在快速选型/了解/对比/体验人脸相关sota模型，依托于Modelscope开发库和Pytorch框架"
    # 启动 Gradio 应用
    gr.Interface(fn=detect_faces,
                 inputs=[inputs, model_name],
                 outputs=outputs, title=title,
                 examples=example,
                 description=description).launch()
