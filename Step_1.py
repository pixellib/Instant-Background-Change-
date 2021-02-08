person,bus,car,aeroplane, bicycle, ,motorbike,bird, boat, bottle,  cat, chair, cow, dinningtable, dog,
horse pottedplant, sheep, sofa, train, tv

import pixellib
from pixellib.tune_bg import alter_bg
change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.change_bg_img(f_image_path = "sample.jpg",b_image_path = "background.jpg", output_image_name="new_img.jpg")

Step 2:
change_bg.change_bg_img(f_image_path = "sample2.jpg",b_image_path = "background.jpg", output_image_name="new_img.jpg")
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.change_bg_img(f_image_path = "sample2.jpg",b_image_path = "background.jpg", output_image_name="new_img.jpg", detect = "person")
change_bg.change_bg_img(f_image_path = "sample2.jpg",b_image_path = "background.jpg", output_image_name="new_img.jpg", detect = "person")
change_bg.change_bg_img(f_image_path = "sample2.jpg",b_image_path = "background.jpg", output_image_name="new_img.jpg", detect = "car")

Step 3:
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.color_bg("sample2.jpg", colors = (0,0,255), output_image_name="colored_bg.jpg", detect = "person")
change_bg.color_bg("sample2.jpg", colors = (0, 0, 255), output_image_name="colored_bg.jpg", detect = "person")

Step4 : Gray Scale background
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.gray_bg("sample2.jpg",output_image_name="gray_img.jpg", detect = "person")
change_bg.gray_bg("sample.jpg",output_image_name="gray_img.jpg", detect = "person")

Step 5: Background Blure:
change_bg.blur_bg("sample2.jpg", low = True, output_image_name="blur_img.jpg")
change_bg.blur_bg("sample2.jpg", moderate = True, output_image_name="blur_img.jpg")
change_bg.blur_bg("sample2.jpg", extreme = True, output_image_name="blur_img.jpg")

Full Code:
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.blur_bg("sample2.jpg", moderate = True, output_image_name="blur_img.jpg")
Blure:
change_bg.blur_bg("sample2.jpg", extreme = True, output_image_name="blur_img.jpg", detect = "person")
Refernce:
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
output = change_bg.change_bg_img(f_image_path = "sample.jpg",b_image_path = "background.jpg", detect = "person")
cv2.imwrite("img.jpg", output)
array color:
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
output = change_bg.color_bg("sample.jpg", colors = (0, 0, 255), detect = "person")
cv2.imwrite("img.jpg", output)
Blure:
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
output = change_bg.blur_bg("sample.jpg", moderate = True, detect = "person")
cv2.imwrite("img.jpg", output)
Gray:
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
output = change_bg.gray_bg("sample.jpg", detect = "person")
cv2.imwrite("img.jpg", output)

Background change:
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")

capture = cv2.VideoCapture(0)
while True:
 ret, frame = capture.read()
 output = change_bg.change_frame_bg(frame, "flowers.jpg", detect = "person")
 cv2.imshow("frame", output)
 if  cv2.waitKey(25) & 0xff == ord('q'):
     break
     
     
 Blure Frames:
 import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")

capture = cv2.VideoCapture(0)
while True:
 ret, frame = capture.read()
 output = change_bg.blur_frame(frame, extreme = True, detect = "person")
 cv2.imshow("frame", output)
 if  cv2.waitKey(25) & 0xff == ord('q'):
     break

