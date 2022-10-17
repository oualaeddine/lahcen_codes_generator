import sys

from PIL import Image, ImageFont, ImageDraw

i = str(sys.argv[1])
print(i)
image_list = []
with open('txt/file0' + i + '.txt') as f:
    lines = [line.rstrip('\n') for line in f]

    counter = 0
    for line in lines:
        my_image = Image.open("code.jpg")
        title_font = ImageFont.truetype('arial.ttf', 90)
        title_text = line
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((570, 310), title_text, (0, 0, 0), font=title_font)
        # my_image.save("result_jpg/" + line + ".jpg")
        im_x = my_image.convert('RGB')
        image_list.append(im_x)
        counter = counter + 1
        if counter % 50 == 0:
            my_image.save('result_pdf/' + i + '_' + str(counter) + '_my_images.pdf', save_all=True,
                          append_images=image_list)
            print("generated : " + str(counter - 50) + "-" + str(counter))
