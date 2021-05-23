import argparse
import cv2
import pytesseract
from PIL import Image


input_parser = argparse.ArgumentParser(prog="npd.py", usage="python npd.py input_image img.jpg")
input_parser.add_argument("input_image", help="str, absolute path to input image in jpg format")
args = input_parser.parse_args()

def extract_number_plate_info(img_pth:str):
  """
  Function to extract info from the img passed
  """
  # read image as grayscale
  img = cv2.imread(img_pth,1)

  text_content = pytesseract.image_to_string(Image.open(img_pth)).split('\n')
  user_name = ' '.join(text_content[2].split()[:-1])
  father_name = text_content[6]
  dob = text_content[7]
  pan_id = text_content[10]
  print(f"""User Name: {user_name}
Father Name: {father_name}
dob: {dob}
pan_id: {pan_id}
  """)

if __name__ == "__main__":
  extract_number_plate_info(args.input_image)