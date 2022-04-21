/*****************************************************************************
* Class:        CSC 665-01 Artificial Intelligence Spring 2021
* Name:         Sabrina Dang
* Student ID:   918586947
* Project:      Assignment 1: Search
*
* Description:
*   This assignment purpose was to help me get figure out how to make the 
*   Pacman's paths work in certain ways such as: to reach a certain location,
*   to collect food effeiciently, and build different search algorithms for
*   those paths. What the assignment asked for was implemenation for the
*   different searches like Depth First Search (DFS).So with DFS I needed to
*   get to the deepest nodes. To get to those deepest nodes I needed to create
*   a stack, make sure it wasn't empty, check to see if it has reached its goal
*   state or not, check if the current node is in visited, if not visited add it
*   and then push the new node state and direction. Iterate through till we have 
*   gotten all the adjacent vertices and added all that has not been visited onto
*   the stack. 
*
*   Next was Breadth First Search (BFS). I practically worked off of the DFS and 
*   the code was taken from that. The difference this time was that we had to 
*   keep track of that cost as well and push all the updated new node values onto
*   the queue.
*
*   For Uniform Cost Search I needed to search for the node with the LEAST total cost.
*   Also used the code from the previous methods, and this time I had to compare the
*   successor's path cost and compare it to what's been visited. If it is less than 
*   what we have visited we need to get that updated cost and push that onto the 
*   priority queue.
*
*   A* Search needed me to search for the node with the LOWEST combined cost AND 
*   heuristic. For this I needed to use the current node and compare it with each
*   and every node we have previously visisted. If it hasn't been visited and it
*   has a lower cost than the previous, set our alreadyVisited bool to true. If we
*   have one that has not been visited yet, we nee dto push the node with the 
*   priority number of the total cost.
*
*   All in all, a lot of it was reading through what methods were already done and
*   working from there. A lot of it was checking, rechecking, and pushing the 
*   necessary information. In some cases comparisons needed to be made to get
*   the correct answer. I spent maybe about 32-35 hours on this assignment. It
*   didn't really stick to me and I am pretty slow. I had to read, try the code out, 
*   and had tons of errors such as infinite loops or crashes. I have not used Python 
*   before this class so the syntax sometimes got to me and now I know Python is finicky 
*   with spacing.
*
*****************************************************************************/

