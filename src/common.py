import os
dirnow    = os.path.dirname(os.path.abspath(__file__))
maze_file = os.path.join(dirnow, "maze.png")
finl_file = os.path.join(dirnow, "finl.png")
rout_file = os.path.join(dirnow, "route.txt")
test_file = os.path.join(dirnow, "test.png")
dump_file = os.path.join(dirnow, "test.txt")
assert os.path.isfile(maze_file)

HAM_CNT     = 3
BLK_SIZE    = 23
HLF_SIZE    = 12
WALL_THRESH = 0.1

def check_is_wall(color_now) -> int:
    assert len(color_now) == 3
    avg = sum(color_now) / len(color_now)
    return int(avg <= 255 * WALL_THRESH)

def avg_color(c1, c2) -> tuple:
    return tuple([(c1[i] + c2[i]) >> 1 for i in range(len(c1))])
