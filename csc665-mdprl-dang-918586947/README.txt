/*****************************************************************************
* Class:        CSC 665-01 Artificial Intelligence Spring 2021
* Name:         Sabrina Dang
* Student ID:   918586947
* Project:      Assignment 3: MDP and Reinforcement Learning
*
* Description:
*   This assignment purpose was to figure out and implement value iteration and
*   Q-learning.
*
*   First step I did was to start working on computeActionFromValues and
*   computeQValueFromValues. For computeActionFromValues we needed to make
*   sure that if there are no legal actions to be made, return none. Other than
*   that we needed to find the best action/value. Did a comparison to find that
*   value. For computeQValueFromValues we needed to iterate through the next state
*   and probability of the transition, and from there we needed to calculate the
*   q value each time which is shown in the equation in the code.
*
*   Q2-3 -> see code
*
*   For Q6 we needed to follow the instruction to write a Q-learning agent that 
*   is able to learn by trial and error from the interactions with the 
*   environment. First we did was fill out __init__ so we can initialize the 
*   q values there. Then on to the next thing which is returning the qval's
*   state and action. If not a possible state, return 0.0. For computing valueus
*   from q values we need to explore the legal actions and for every legal action 
*   we need to append the state/actions of the q value into an array of values. 
*   then we return the max of those values. The same kind of goes for computing 
*   action from q values. Need to find best action to take from the legal actions.
*
*   Q7 we needed to  implement epsilon-greedy action in getAction. This is where
*   random actions are selected and it follows its current best Q-value. As the 
*   instruction has stated, we can stimulate the binary variable with a probability
*   of p of success by using util.flipCoin(p), which returns True with probability 
*   p and False with probability 1-p. Once we did that, we can dom use 
*   random.choice(list), but more specifically we are randomly choosing from a list
*   of legal actions.
*
*   Q8 -> see code
*
*   Q9 I ran python autograder.py -q q9 and python pacman.py -p PacmanQAgent -n 10 
*   -l smallGrid -a numTraining=10 to see what's going on. Reading the learning 
*   status I did see that it wasn't Pacman playing poorly and slowly getting 
*   better till he was just the best. Pooyan's guide explained well that Pacman
*   can/will play poorly even after having learned a good policy due to him
*   making that random exploratory move as a ghost. Just watching the 10 games and
*   seeing him move very little and to do similatly in the next test was really
*   slow. I see how after 1000-2000 games he starts to remain in the positive for
*   rewards.
*
*   Q10 we needed to implement approx Q-learning agent that learns weights for
*   features of states. First thing to do was getQValue. Here we had to iterate
*   through the features and get both the feature's weight and value. We will
*   have our initial value of 0 and keep adding to it each time it iterates. The
*   qvalue is the feature's value times the feature's weight. Then we return value.
*   Next is to do update(). The equation for the difference is given in the 
*   assignment. So we have our reward added to the value of the next state multiplied
*   by the discount. Then that total will minus our self.getQValue(). The next thing
*   is to get that self weight and update it by the equation also given by the 
*   assignment.
*

*   In the end, a lot of it was reading through what methods were already done and
*   working from there once again. The comments/documentation on some of the code
*   blocks were very helpful. Especially getAction since the hints were basically
*   the answer and what I needed to do. Had a bit trouble doing Q3 and reading/tracking
*   what it wanted me to do and what the correct values that would lead to the
*   expected outcome. I spent maybe about 8-14 hours on this assignment. 
*
*****************************************************************************/

