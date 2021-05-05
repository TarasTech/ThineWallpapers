import glob
import json
import PIL
from PIL import Image

def getDimension(imageFilename):
    im = Image.open(imageFilename)
    w, h = im.size
    return str(w) + 'x' + str(h)

class Wallpaper:
    name = ""
    author = ""
    url = ""
    thumbnail = ""
    dimensions = ""
    copyright = ""
    collections = ""
    featured = True
    downloadable = True

myWallpapers = []

for f in glob.glob('*.png'):
    wall = Wallpaper()
    wall.name = f.split('.')[0].title()
    wall.author = "WhyMS"
    wall.url = "https://raw.githubusercontent.com/TarasTech/ThineWallpapers/main/" + f
    wall.thumbnail = "https://raw.githubusercontent.com/TarasTech/ThineWallpapers/main/" + f
    wall.dimensions = getDimension(f)
    wall.copyright = "Designed by WhyMS"
    wall.collections = "undefined"
    wall.featured = True
    wall.downloadable = True
    
    myWallpapers.append(wall.__dict__)
    
print(json.dumps( myWallpapers ))
input("Press any key to exit")