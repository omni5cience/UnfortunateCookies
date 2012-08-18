import Image, ImageDraw, ImageFont, sys

def draw_word_wrap(img, text, xpos=0, ypos=0, max_width=130,
                   fill=(0,0,0), font=ImageFont.load_default()):
    '''Draw the given ``text`` to the x and y position of the image, using
    the minimum length word-wrapping algorithm to restrict the text to
    a pixel width of ``max_width.``
    '''
    draw = ImageDraw.Draw(img)
    text_size_x, text_size_y = draw.textsize(text, font=font)
    remaining = max_width
    space_width, space_height = draw.textsize(' ', font=font)
    # use this list as a stack, push/popping each line
    output_text = []
    # split on whitespace...
    for word in text.split(None):
        word_width, word_height = draw.textsize(word, font=font)
        if word_width + space_width > remaining:
            output_text.append(word)
            remaining = max_width - word_width
        else:
            if not output_text:
                output_text.append(word)
            else:
                output = output_text.pop()
                output += ' %s' % word
                output_text.append(output)
            remaining = remaining - (word_width + space_width)
    for text in output_text:
        draw.text((xpos, ypos), text, font=font, fill=fill)
        ypos += text_size_y

image = Image.open("BlankFortuneCookie.jpg")
font = ImageFont.truetype("Geneva.ttf", 24)
draw = ImageDraw.Draw(image)
text = sys.argv[1]
text += " in bed"
x, y = image.size
#draw.text((x/2, y/2-96), text, fill=0, font=font)
draw_word_wrap(image, text, x/2-34, y/2-96, max_width=288, font=font)
image.show()



