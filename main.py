
def main():
    size = int(input("Enter the size of the maze: "))
    walls = int(input("Enter the wall percentage you want in the maze(1-25): "))
    
    while True:
        choice = input("Enter you choice (1.Print Path, 2.Generate Another Puzzle, 3.Exit): ")
        
        if choice == '1':
            print("path_finder")
        elif choice == '2':
            print("generated another path")
        elif choice == '3':
            print("Thank you for using the app!")
            break

main()
