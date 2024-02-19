# Maze_Solver
---
## Description

- A Terminal Based App to find the path from S point to E point in 2D Matrix
- 2D matrix should have starting point at (0,0) and Ending point (n,n)
- It has walls(obstacles)🧱 between 1-25% of the matrix cells
- Asking user whether to generate maze or to print path from S to E if possible
- You have to find all the possible path

---

## Approach

- You can use the **BFS(Breadth First Search)** technique to achieve the goal
- In BFS we check all the possible direction i.e top, right, bottom, left and similarly it goes on till its possible.
- I have used **Set and Queue data structure** to keep the track of visited cells and queue to traverse in bfs manner as it follows **FIFO principle**

**Refer below visiual representation**

![bfs-represtation](https://th.bing.com/th/id/R.3ef5ccca5ecf1ee5bc180b3332560a65?rik=chP7JJh5X%2fy78Q&riu=http%3a%2f%2fwww.codesdope.com%2fstaticroot%2fimages%2falgorithm%2fbfs.gif&ehk=Ac5K1clS9L%2bwewQ5bZFl4IxWER%2b5Bxt15%2bFvHwTphAQ%3d&risl=&pid=ImgRaw&r=0)

---

## Reference

- [Rat In Maze Problem](https://www.geeksforgeeks.org/rat-in-a-maze/)
- [Set Data Structure](https://www.geeksforgeeks.org/sets-in-python/)
