import os
import random
from PIL import Image
from common import check_is_wall, maze_file

def in_graph(W, H, nx, ny) -> bool:
    return 0 <= nx < W and 0 <= ny < H

def check_wall(image:Image, nx, ny):
    return check_is_wall(image.getpixel((nx, ny)))

TEST_CNT = 2000
def get_block_width_at(image:Image, x:int, y:int, xset, yset):
    DX = [-1, 0, 1, 0]
    DY = [ 0,-1, 0, 1]
    W, H = image.size
    for d in range(len(DX)):
        px = x
        py = y
        while True:
            nx = px + DX[d]
            ny = py + DY[d]
            if (not in_graph(W, H, nx, ny)) or (check_wall(image, nx, ny) != check_wall(image, x, y)):
                break
            px = nx
            py = ny
        if DX[d]:
            xset.append(px)
        else:
            yset.append(py)

BORDER = 20

def del_conti(arr_set:list) -> list:
    assert len(arr_set) > 0
    new_arr = [arr_set[0]]
    for i in range(1, len(arr_set)):
        if abs(arr_set[i] - new_arr[-1]) >= 4:
            new_arr.append(arr_set[i])
        else:
            new_arr[-1] = arr_set[i]
    return new_arr

def test_block_width(): # 检测格子宽度
    widths = []
    image = Image.open(maze_file).convert("RGB")
    W, H = image.size
    xset = []
    yset = []
    for _ in range(TEST_CNT):
        x = random.randint(BORDER, W - 1 - BORDER)
        y = random.randint(BORDER, H - 1 - BORDER)
        widths.append(get_block_width_at(image, x, y, xset, yset))
    xset = [0] + sorted(list(set(xset))) + [W - 1]
    yset = [0] + sorted(list(set(yset))) + [H - 1]
    xset = del_conti(xset)
    yset = del_conti(yset)
    dxset = [xset[i] - xset[i-1] for i in range(1, len(xset))]
    dyset = [yset[i] - yset[i-1] for i in range(1, len(yset))]
    yset = del_conti(yset)
    dx = sum(dxset) / len(dxset)
    dy = sum(dyset) / len(dyset)
    assert abs(dx - dy) < 0.5
    return round(W / dx), round(H / dx)

if __name__ == "__main__":
    print(test_block_width())
