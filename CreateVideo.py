import os
import cv2

path = "Images/"

images=[]

for file in os.listdir(path):
    name,extension=os.path.splitext(file)

    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        fileName=path+"/"+file
        print(fileName)

        images.append(fileName)

count=len(images)

frame= cv2.imread(images[0])
width, height, channels=frame.shape
size=(width,height)
print(size)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)

for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)

out.release
print("Done")