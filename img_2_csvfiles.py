import cv2
import numpy as np
import pandas as pd
import os

class Img_2_csv(object):

    def __init__(self):
        pass
    
    def path_(self, path):
        li = [img for img in os.listdir(path) if img.endswith(".png")]
        return li

    def create_img_array(self, images):
        images_array = []
        for i in range(len(images)):
            img = cv2.imread(os.getcwd()+"/jab_blk/"+images[i])
            img = img.flatten().tolist()
            images_array.append(img)
            #print(len(img))
        return images_array

    def convert_dataframe(self, image_array, li):
        data = {}
        
        for i in range(len(image_array)):
            data[li[i]] = image_array[i]
        data = pd.DataFrame(data=data)
        data.T.to_csv("lstm.csv")

        data = pd.read_csv("lstm.csv")
        data['labels'] = ["jab" for i in range(len(image_array))]
        data.to_csv("final_lstm.csv")

images = os.getcwd()+"/jab_blk/"
main = Img_2_csv()
path = main.path_(images)
img_array = main.create_img_array(path)
main.convert_dataframe(img_array, path)

    
