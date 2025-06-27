import tkinter as tk
from tkinter import filedialog, messagebox
import json
import heapq
import time
import threading

CELL_SIZE = 30


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.start = self.find_point("O")
        self.end = self.find_point("X")

    def find_point(self, symbol):
        for i, row in enumerate(self.maze):
            for j, val in enumerate(row):
                if val == symbol:
                    return (i, j)
        return None

    def get_neighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row + 1 < len(self.maze):
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col + 1 < len(self.maze[0]):
            neighbors.append((row, col + 1))
        return neighbors


class MazeGUI:
    def __init__(self, root, maze_data):
        self.root = root
        self.root.title("Pathfinding Visualizer")
        self.maze_obj = Maze(maze_data)
        self.rows = len(maze_data)
        self.cols = len(maze_data[0])
        self.delay = tk.DoubleVar(value=0.05)
        self.algo_choice = tk.StringVar(value="A*")
        self.running = False

        self.canvas = tk.Canvas(
            root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="white"
        )
        self.canvas.grid(row=0, column=0, columnspan=5)

        self.control_frame = tk.Frame(root)
        self.control_frame.grid(row=1, column=0, columnspan=5, pady=10)

        tk.Label(self.control_frame, text="Speed:").pack(side=tk.LEFT)
        tk.Scale(
            self.control_frame,
            variable=self.delay,
            from_=0.01,
            to=0.5,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            length=100,
        ).pack(side=tk.LEFT)

        tk.Label(self.control_frame, text="Algorithm:").pack(side=tk.LEFT)
        tk.OptionMenu(self.control_frame, self.algo_choice, "A*", "BFS", "DFS").pack(
            side=tk.LEFT
        )

        self.start_btn = tk.Button(
            self.control_frame, text="Start", command=self.start_pathfinding
        )
        self.start_btn.pack(side=tk.LEFT)

        self.reset_btn = tk.Button(self.control_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(side=tk.LEFT)

        self.draw_maze()

    def draw_maze(self, path=[]):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                color = "white"
                val = self.maze_obj.maze[i][j]
                if val == "#":
                    color = "black"
                elif val == "O":
                    color = "green"
                elif val == "X":
                    color = "red"
                elif (i, j) in path:
                    color = "yellow"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def start_pathfinding(self):
        if not self.running:
            threading.Thread(target=self.run_algorithm).start()

    def reset(self):
        self.running = False
        self.draw_maze()

    def run_algorithm(self):
        self.running = True
        algo = self.algo_choice.get()
        if algo == "A*":
            self.a_star()
        elif algo == "BFS":
            self.bfs()
        elif algo == "DFS":
            self.dfs()

    def a_star(self):
        start = self.maze_obj.start
        end = self.maze_obj.end
        open_set = [(0, [start])]
        g_score = {start: 0}

        def h(pos):
            return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

        visited = set()

        while open_set and self.running:
            _, path = heapq.heappop(open_set)
            current = path[-1]

            if current == end:
                self.draw_maze(path)
                return

            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.maze_obj.get_neighbors(*current):
                r, c = neighbor
                if self.maze_obj.maze[r][c] == "#":
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f = tentative_g + h(neighbor)
                    heapq.heappush(open_set, (f, path + [neighbor]))

            self.draw_maze(path)
            time.sleep(self.delay.get())

    def bfs(self):
        start = self.maze_obj.start
        end = self.maze_obj.end
        queue = [(start, [start])]
        visited = set()

        while queue and self.running:
            current, path = queue.pop(0)

            if current == end:
                self.draw_maze(path)
                return

            for neighbor in self.maze_obj.get_neighbors(*current):
                if neighbor in visited:
                    continue
                r, c = neighbor
                if self.maze_obj.maze[r][c] == "#":
                    continue
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

            self.draw_maze(path)
            time.sleep(self.delay.get())

    def dfs(self):
        start = self.maze_obj.start
        end = self.maze_obj.end
        stack = [(start, [start])]
        visited = set()

        while stack and self.running:
            current, path = stack.pop()

            if current == end:
                self.draw_maze(path)
                return

            if current in visited:
                continue
            visited.add(current)

            for neighbor in reversed(self.maze_obj.get_neighbors(*current)):
                r, c = neighbor
                if self.maze_obj.maze[r][c] == "#":
                    continue
                stack.append((neighbor, path + [neighbor]))

            self.draw_maze(path)
            time.sleep(self.delay.get())


def load_maze_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            maze_data = json.load(f)
        root = tk.Tk()
        MazeGUI(root, maze_data)
        root.mainloop()


if __name__ == "__main__":
    load_maze_file()
