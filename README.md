# Cursor_Aimbot
Please do not use this in online game
I am trying to make an aimbot for single player game, right now the object detection and cursor aimlock is successed, but when there is no recognizable crosshair on the screen, it will stop working.
If you have any idea please feel free to make some changes

The module I am using is yolov10, please follow the steps to setup your environment:

1. pip install supervision labelme  labelme2yolo huggingface_hub google_cloud_audit_log
2. pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  (if you don't have the Nvidia GPU just skip this line)
3. pip install git+https://github.com/THU-MIG/yolov10.git

Run yolo_screenshot.py if you want to make your own dataset from zero to hero, but if you have one, you can go roboflow.com or use labelme to start label your dataset (this is a long process so have some patience)

Download training model from https://github.com/THU-MIG/yolov10/releases/tag/v1.1

After everything sets up, you can run this in your virtual-environment: yolo detect train data=re4_aimbot/data.yaml model=yolov10n.pt epochs=30 batch=8 imgsz=640 device=0
"data=re4_aimbot/data.yaml" is data=folder/data.yaml
"model=yolov10n.pt" is the model that you have downloaded from https://github.com/THU-MIG/yolov10/releases/tag/v1.1
Set "epochs" and "batch" that fit your computer, don't make it too large otherwise you won't have pc to use in next few days(if your pc is slow or no GPU support)
"device=0" is activate GPU, if you don't have one, just remove this

I am using a dataset that has around 200 pictures, yolov10x.pt
I have uploaded trained model called best.pt, but in zips, you have to extract, but if you can train a better model please do :>

Last thing(at least right now) launch the game and run yolo_detect_aim.py, it allows you to observe how the detection works in real time, the as I said the aimbot function is not complete yet, but you can run the code and use picture to try out
the accuracy is ok

# Training Result
![results](https://github.com/user-attachments/assets/02e52971-3393-4139-a77c-66d0fb163cb3)
![val_batch0_labels](https://github.com/user-attachments/assets/002de4fe-2863-483f-ad57-ba11126ef4d4)
![train_batch1](https://github.com/user-attachments/assets/d6f4da40-92eb-4791-bb22-fd902a30d3a5)
![val_batch1_labels](https://github.com/user-attachments/assets/3261712e-d2d5-47c3-8a9f-197358993234)

# In Game:
![1730669454849](https://github.com/user-attachments/assets/ef751369-72dc-4537-8204-a808ec5953de)
![1730669420025](https://github.com/user-attachments/assets/49562c85-9b53-4c36-9a93-df7738ea46a7)
![1730669549648](https://github.com/user-attachments/assets/5c3a26c9-d467-41ab-9ad9-0e84e12a5bd3)
![RE1](https://github.com/user-attachments/assets/81d2dd2a-3820-416e-8a5a-24e8d42fd77a)
![RE2](https://github.com/user-attachments/assets/076a9177-65f8-4478-a642-be7d5a11862d)



