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


