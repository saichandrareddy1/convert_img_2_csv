import numpy as np
import cv2
import os



def main(path):
    li = [img for img in os.listdir(path) if img.endswith(".jpg")]
    return li
li = main(os.getcwd()+"/jab/")
print("Done")
def reshape(li):
    print("Start")
    for i in range(len(li)):
        img = cv2.imread(os.getcwd()+"/jab/"+li[i])
        print("Readed........")
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img, (28, 28), cv2.INTER_CUBIC)
        cv2.imwrite(os.getcwd()+"/jab_blk/"+"00_"+str(i)+".png", img)
        print("Writed........")
    print("ENd")
reshape(li)



