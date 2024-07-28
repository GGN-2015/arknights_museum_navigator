all: run_in_maze.out

clean:
	rm -rf *.out

run_in_maze.out: run_in_maze.cpp
	$(CXX) -std=c++17 run_in_maze.cpp -o run_in_maze.out

.PHONY: all clean
