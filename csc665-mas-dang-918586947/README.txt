/*****************************************************************************
* Class:        CSC 665-01 Artificial Intelligence Spring 2021
* Name:         Sabrina Dang
* Student ID:   918586947
* Project:      Assignment 2 - Multi-Agent Search
*
* Description:
*   	This assignment purpose is to design agents for the classic version of 
*   	Pacman including the ghosts. It will include the implementation of
*   	both minimax and  expectmax search.
*
*	The issue just running it was that the score was not functioning properly.
*	Within the evaluationFunction I went and did two checks. One is if the
*	game has been won where all pellets are eaten succesfully. The other is to
*	check if pacman has stopped moving, if so decrement the score till he
*	dies completely. Then we needed to compare the current number of food
*	acquired from pacman to the success game state number of food. If it 
*	reaches that success state then increment the score. Lastly return the
*	total score.
*
*	Need to write search agent where it will handle any number of ghost
*	agents in the game. First thing I needed to do was to do a series of
*	checks of the game state. If it has been won, lost, or if the depth
*	has reached it's end we will return right there and then. If not continue.
*	Need to check when min is called to max then Pacman successor state needs
*	to be passed to the 1st ghost. Need to pass the successor state to the min
*	node. Then we can do the checking to see if the node is the root or not.
* 	If it is the root return node with max value and current action. Else
*	we are returning node with max value but with previous node action.
*	
*	For the alpha-beta we needed the minimax values to be identical to the 
*	minimax agent minimax values. Needs to process successor states in order
*	and call State.generateSuccessor minimally.
*
*	I spent about 10 - 15 hours on this assignment. A lot of just reading 
*	the code here and there to get a grasp of what it's doing then start
*	to code. I had a lot of issues with the testing just running infinitely
*	or my pacman won't move, stuck in an area, etc. I guess one of the issues
* 	I can think of is not doing my checks correctly like checking if we won
*	or if we lost. Also appending all of that information kind of got to me
* 	as well.
*****************************************************************************/
