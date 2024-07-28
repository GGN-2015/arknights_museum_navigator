#!/bin/bash
HAMMER_CNT=$1

echo "generating .out file ..."
make all

echo "generating binay_matrix ..."
python3 maze_reader.py ${HAMMER_CNT}

echo "generating navigation route ..."
./run_in_maze.out < test.txt > route.txt

echo "merging navigation image ..."
python3 render.py
