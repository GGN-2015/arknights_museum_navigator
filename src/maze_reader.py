import os
import sys
from PIL import Image
from common import BLK_SIZE, HLF_SIZE, check_is_wall, maze_file, test_file, dump_file, HAM_CNT
from recognize import test_block_width

def generate_binary_matrix(height:int, width:int) -> list:
    image = Image.open(maze_file).convert("RGB")
    image = image.resize((BLK_SIZE * width, BLK_SIZE * height)) # 缩放
    test_img = Image.new("RGB", (width, height))
    matrix_now = []
    for i in range(height):
        vector_now = []
        for j in range(width):
            real_pos_x = BLK_SIZE * j + HLF_SIZE
            real_pos_y = BLK_SIZE * i + HLF_SIZE
            color_now  = image.getpixel((real_pos_x, real_pos_y))
            is_wall    = check_is_wall(color_now)
            vector_now.append(is_wall)
            test_img.putpixel((j, i), (0, 0, 0) if is_wall else (255, 255, 255))
        matrix_now.append(vector_now)
    test_img = test_img.resize((BLK_SIZE * width, BLK_SIZE * height))
    test_img.save(test_file)
    return matrix_now

def show_all(height:int, width:int, ham_cnt:int) -> None: # ouptut to stdout
    binary_matrix = generate_binary_matrix(height, width)
    fp = open(dump_file, "w")
    fp.write("%d %d %d\n" % (height, width, ham_cnt))
    for line in binary_matrix:
        fp.write((" ".join(list(map(str, line)))) + "\n")

if __name__ == "__main__":
    w, h = test_block_width()
    print("tested: h, w = ", h, w)
    show_all(h, w, int(sys.argv[1]))
