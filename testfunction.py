# function from youtube/Jie_Jenn
import os
from PIL import Image, ImageStat

# relative path to image folder
image_folder = "./images1"

# for any images (jpg) in image folder
image_files = [_ for _ in os.listdir(image_folder)if _.endswith(('.jpg', '.png'))]


# initialize empty array for duplicates
duplicate_files = []

# for original files in image_files
for original_file in image_files:
    #if it's not in duplicates array
    if not original_file in duplicate_files:
        # get mean pix value from ('./images','original_image')
        original_image = Image.open(os.path.join(image_folder, original_file))
        pix_mean1 = ImageStat.Stat(original_image).mean

    # second loop through image files
        for file_check in image_files:
            # if not the same as original_file loop current
            # I believe this just compares file names so not sure if this works with smae names
            if file_check != original_file:
                # get mean pix values for the second file to compare with the first
                image_check = Image.open(os.path.join(image_folder, file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean

                # originall this added both images in duplicate _files array
                # only one file should be in duplicaes and then deleted
                if pix_mean1 == pix_mean2:
                    # appends the SECOND file to the dupes array
                    duplicate_files.append(file_check)


# print all duplictes files 
print(f"duplicate files:\n{duplicate_files}")




