# Requires 2 libraries -> QRcode and Image

import qrcode as q


def generate (link):
    qr = q.QRCode(
        version =1, 
        error_correction = q.constants.ERROR_CORRECT_L,
        box_size = 10,
        border= 4
    )
    
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color = '#', back_color = '#212121')
    img.save('githubQR.png')
    

if __name__ == '__main__':
    # Generating QR for my github Profile
    generate('https://github.com/mr-ayush-agrawal')