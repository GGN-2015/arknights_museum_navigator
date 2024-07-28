import os
from PIL import Image, ImageDraw
from common import BLK_SIZE, avg_color, maze_file, finl_file, rout_file
from recognize import test_block_width

def render(pos_list, height, width):
    image = Image.open(maze_file).convert("RGB")
    image = image.resize((BLK_SIZE * width, BLK_SIZE * height)) # 缩放
    raw   = image.copy()
    draw = ImageDraw.Draw(image)
    for x, y in pos_list:
        draw.rectangle((y * BLK_SIZE, x *BLK_SIZE, (y + 1) * BLK_SIZE, (x + 1) * BLK_SIZE), fill=(255, 0, 0))
    w, h = raw.size
    for i in range(w):
        for j in range(h):
            image.putpixel((i, j), avg_color(raw.getpixel((i, j)), image.getpixel((i, j))))
    image.save(finl_file)

def get_pos_list() -> list:
    pos_list = []
    for line in open(rout_file):
        line = line.strip()
        if line == "": # jump empty line
            continue
        x, y = line.split()
        pos_list.append((int(x) - 1, int(y) - 1))
    return pos_list

def main(height, width):
    pos_list = get_pos_list()
    render(pos_list, height, width)

if __name__ == "__main__":
    w, h = test_block_width()
    main(h, w)
