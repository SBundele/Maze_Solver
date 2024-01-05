import random
from colorama import init
from termcolor import colored

init()

# Generate Maze Function
def generateMaze(size, wall):
    maze = [["◌" for col in range(size)] for row in range(size)]
    
    for i in range(size):
        for j in range(size):
            if random.randint(1, 60) <= wall:
                maze[i][j] = "▓"
                
    maze[0][0] = colored('|S|',"green","on_black")
    maze[size-1][size-1] = colored('|E|',"green","on_black")
    
    return maze

# Display Generate Maze Function
def displayMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze)):
            if maze[row][col] == "◌":
                print(colored("|◌|", "blue","on_black"), end=" ")
            elif maze[row][col] == "▓":
                print(colored("|▓|","red","on_black"), end=" ")
            elif maze[row][col] == "◍":
                print(colored("|◍|","green","on_black"),end=" ")
            else:
                print(maze[row][col], end= " ")
        print() 

# Finding Path Function
def find_path(maze, size, position = (0,0), visited = None):
    if visited is None:
        visited = set()
    
    if position == (size-1,size-1):
        return  [position]
    
    visited.add(position)
    
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for dir in direction:
        new_row,new_col = position[0] + dir[0], position[1] + dir[1]
        
        if 0 <= new_row < size and 0 <= new_col < size and maze[new_row][new_col] != "▓" and (new_row,new_col) not in visited:
            path = find_path(maze, size, (new_row,new_col), visited)
            if path:
                return [(position[0], position[1])] + path

    return []

# Displaying Finded Path Function
def display_path(maze, path):
    for position in path:
        row,col = position
        maze[row][col] = "◍"
    maze[0][0] = colored('|S|',"green","on_black")
    maze[len(maze)-1][len(maze)-1] = colored('|E|',"green","on_black")
    displayMaze(maze)

def main():
    size = int(input("Enter the size of the maze: "))
    wall = int(input("Enter the wall percentage you want in the maze(1-25): "))
    
    maze = generateMaze(size, wall)
    print("Generated Maze:")
    displayMaze(maze)
    
    while True:
        choice = input("Enter you choice (1.Print Path, 2.Generate Another Puzzle, 3.Exit): ")
        
        if choice == '1':
            path = find_path(maze,size)
            if path:
                print("Path: ")
                display_path(maze, path)
            else:
                print("No path exists.")
        elif choice == '2':
            size = int(input("Enter the size of the maze: "))
            wall = int(input("Enter the wall percentage you want in the maze(1-25): "))
            maze = generateMaze(size, wall)
            print("Generated Maze")
            displayMaze(maze)
        elif choice == '3':
            print("Thank you for using the app!")
            break
        else:
            print("Invalid Input")

main()
