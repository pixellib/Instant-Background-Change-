import pixellib
from pixellib.tune_bg import alter_bg
import cv2

# change_bg = alter_bg(model_type = "pb")
# change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
output = change_bg.change_bg_img(f_image_path = input_im,b_image_path = bak_dir, detect = "person")
cv2.imwrite(out_dir, output)
plt.imshow(output)
plt.show()
