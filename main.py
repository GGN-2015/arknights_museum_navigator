import os
import subprocess
import sys
from PIL import Image
dirnow      = os.path.dirname(os.path.abspath(__file__))
script_file = os.path.join(dirnow, "src", "pipeline.sh")

def main():
    img_path = sys.argv[1]
    assert os.path.isfile(img_path)
    Image.open(img_path).save(os.path.join(dirnow, "src", "maze.png"))
    hammer_cnt = int(sys.argv[2])
    assert 0 <= hammer_cnt <= 10 # 限制锤子的数量范围
    os.chdir(os.path.join(dirnow, "src"))
    subprocess.run(["bash", script_file, str(hammer_cnt)])
    Image.open("finl.png").show()

if __name__ == "__main__":
    main()
