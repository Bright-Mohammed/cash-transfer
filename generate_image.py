# Import Image for basic functionlities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont
import qrcode
import pyqrcode
import os

url = "www.portal.nasarawastatesip.com/NSCCT-LAF-WAK-01-0004.html"

def generate_qrcode(url):
    # Link for website
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img.save('qrcode.png')

def qrcode_with_image(url, id):
    qrobj = pyqrcode.create(url)
    with open(id + '.png', 'wb') as f:
        qrobj.png(f, scale=10, module_color='#51c2d5')
    # Now open that png image to put the logo
    img = Image.open(id + '.png')
    img = img.convert('RGBA')
    width, height = img.size

    # How big the logo we want to put in the qr code png
    logo_size = 60

    # Open the logo image
    print(os.getcwd())
    logo = Image.open("C:\\Users\\Ibrah\\PycharmProjects\\cash-transfer\\logo.png")

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))


# qrcode_with_image(url)

# generate_qrcode(url)

# gfg_logo.jpeg image opened using open function
# and assigned to variable named img
# img = Image.open('ct.png')

# Image is converted into editable form using Draw
# function and assigned to d1
# d1 = ImageDraw.Draw(img)

# Font selection from the downloaded file
# myFont = ImageFont.truetype('/home/raghav/PycharmProjects/gfg/Mistral.ttf', 20)

# Decide the text location, color and font
# d1.text((325, 173), "Suleiman Abubakar Iya", fill=(0, 0, 0))
# d1.text((325, 208), "Female", fill=(0, 0, 0))
# d1.text((325, 240), "Civil servant", fill=(0, 0, 0))
# d1.text((325, 275), "Nasarawa South", fill=(0, 0, 0))
#
# d1.draw()
# # show and save the image
# img.show()
# img.save("results.jpeg")