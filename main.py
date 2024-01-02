import random

def generateMaze(size, wall):
    maze = [[" " for col in range(size)] for row in range(size)]
    
    for i in range(size):
        for j in range(size):
            if random.randint(1, 60) <= wall:
                maze[i][j] = "#"
    
    maze[0][0] = 'S'
    maze[size-1][size-1] = "E"
    
    return maze
    

def main():
    size = int(input("Enter the size of the maze: "))
    wall = int(input("Enter the wall percentage you want in the maze(1-25): "))
    
    maze = generateMaze(size, wall)
    print("Generated Maze")
    for row in maze:
        print(row)
    
    while True:
        choice = input("Enter you choice (1.Print Path, 2.Generate Another Puzzle, 3.Exit): ")
        
        if choice == '1':
            print("path_finder")
        elif choice == '2':
            size = int(input("Enter the size of the maze: "))
            wall = int(input("Enter the wall percentage you want in the maze(1-25): "))
            maze = generateMaze(size, wall)
            print("Generated Maze")
            for row in maze:
                print(row)
        elif choice == '3':
            print("Thank you for using the app!")
            break
        else:
            print("Invalid Input")

main()
