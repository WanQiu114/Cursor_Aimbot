import cv2
import numpy as np
import mss
import pygetwindow as gw
from ultralytics import YOLO
import win32api
import torch
import supervision as sv

# if you have any question about ultralytics, please visit https://github.com/ultralytics/ultralytics/issues/13587

# load your model, my model is called best.pt but you can bring your own model
model = YOLO('best.pt')
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# detecting the window that you want to capture.
windows = gw.getWindowsWithTitle('Resident Evil 4')
if not windows:
    print("Not found")
    exit()

game_window = windows[0]

with mss.mss() as sct:
    monitor = {"top": game_window.top, "left": game_window.left, "width": game_window.width, "height": game_window.height}

    # using PI control to for mouse control
    class PI_control:
        def __init__(self, Kp, Ki):
            self.Kp = Kp
            self.Ki = Ki
            self.integral = 0
            self.previous_error = 0

        def __call__(self, error):
            delta_error = error - self.previous_error
            self.previous_error = error
            self.integral += delta_error
            delta_u = (self.Kp * delta_error) + (self.Ki * self.integral)
            return delta_u

    x_pi = PI_control(0.35, 0.5)
    y_pi = PI_control(0.17, 0.26)

    while True:
        screen = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
        annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

        cv2.imshow('Resident Evil 4 Detection', annotated_image)

        # get detection boxes and move mouse
        boxes = results.boxes.xyxy.cpu().numpy()  
        if len(boxes) > 0:

            
            # the closest one is always the primary target to aim at
            box = max(boxes, key=lambda b: (b[2] - b[0]) * (b[3] - b[1]))



            # calculate the center point of object, when you detect object, convert its position into related window coordinate
            target_center_x = (box[0] + box[2]) / 2
            target_center_y = (box[1] + box[3]) / 2
            screen_target_x = int(target_center_x + monitor["left"])
            screen_target_y = int(target_center_y + monitor["top"])




            # get current cursor position, update cursor position and move the cursor
            current_position = win32api.GetCursorPos()
            x_error = screen_target_x - current_position[0]
            y_error = screen_target_y - current_position[1]
            x_movement = x_pi(x_error)
            y_movement = y_pi(y_error)

            new_position = (int(current_position[0] + x_movement), int(current_position[1] + y_movement))
            win32api.SetCursorPos(new_position)

        # exit window
        if cv2.waitKey(1) % 256 == 27:
            print("Escape hit, closing...")
            break

    cv2.destroyAllWindows()
