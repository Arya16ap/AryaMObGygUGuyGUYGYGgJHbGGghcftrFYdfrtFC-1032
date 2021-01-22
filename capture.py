import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames when camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save the image in any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken")
    #release the camera
    videoCaptureObject.release()
    #closes all the windows the windows while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "qvX2uJoWLh8AAAAAAAAAAVoA5R6tDW3NHhrW1RFEAsFTuzg1oRb80wRRF7u2CtfB"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=3):
            name = take_snapshot()
            upload_file(name)

main()