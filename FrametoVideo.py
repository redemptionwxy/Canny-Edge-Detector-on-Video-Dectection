import cv2
  
def images_to_video():
  fps = 30 # 帧率
  num_frames = 5105
  img_array = []

  for i in range(10000,num_frames+10001):
    filename = "./Frame/frame"+str(i)+".jpg"
    img = cv2.imread(filename)
    img_width = img.shape[1]
    img_height = img.shape[0]
    if img is None:
      print(filename + " is non-existent!")
      continue
    img_array.append(img)
  
  out = cv2.VideoWriter('demo3.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps,(img_width,img_height))
  
  for i in range(len(img_array)):
    out.write(img_array[i])
  out.release()
  
  
def main():
   
  images_to_video()
  
  
if __name__ == "__main__":
  main()