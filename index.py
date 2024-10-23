from pdf2image import convert_from_path, convert_from_bytes
import os
from PIL import Image

cwd = os.getcwd()
input_path = cwd +"/PDF/"
destination_path = cwd +"/PPM/"
image_save_path = cwd +"/JPG/"


def remove_suffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s



def conversion(input_files):
    # conversion method
    try:
        for x in input_files:
            print(x)
            dest_file = input_path + x
            dest_path = destination_path + x + '/'
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
            images_from_path = convert_from_path(dest_file, output_folder=dest_path)
            for x in images_from_path:
                x.close()

        # for loop for input files
        for x in input_files:
            #
            dest_path = destination_path + x + '/'
            txt_files = [f for f in os.listdir(dest_path) if f.endswith('.ppm')]
            # print(txt_files)
            #counter = 0
            x = remove_suffix(x, ".pdf")
            for txt_file in txt_files:
                image = Image.open(dest_path + txt_file)
                image_input_path = image_save_path + x + '/'
                if not os.path.isdir(image_input_path):
                    os.makedirs(image_input_path)
                t = txt_file.split("-")
                txt_file = remove_suffix(t[len(t)-1], ".ppm")
                filename = image_input_path + x + "_" + str(txt_file) + ".jpg"
                #print(filename)
                image.save(filename)
                image.close()
                #counter += 1
    except err:
        print(err)
        return "Exception Occured"

    else:
        return "conversion successfull"









input_files = [f for f in os.listdir(input_path) if f.endswith('.pdf')]


if len(input_files)>0:
    print(conversion(input_files))
else:
    print("There are no input PDF files. Please paste some files in PDF Folder")

    








