from PIL import Image
from PIL.ExifTags import TAGS
import csv

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    #print(info)
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    print(ret)
    return ret

file = 'Z:\Fotoset\Khakassia_big\DSC_0407.JPG'
exif_data = get_exif(file)

print(exif_data['Model'])

#with open('exif_data.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerow(exif_data)
with open('Z:\Fotoset\Khakassia_big\exif_data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in exif_data.items():
       writer.writerow([key, value])

