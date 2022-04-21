/*****************************************************************************
* Class:        CSC 665-01 Artificial Intelligence Spring 2021
* Name:         Sabrina Dang
* Student ID:   918586947
* Project:      Assignment 5: Machine Learning
*
* Description:
*   This assignment purpose was to help me get into machine learning, so it was
*   basically an introduction to machine learning. The project will allow me
*   to build a neural network that will be able to classify digits and more.
*
*  Installation Part:
*   The installation part was not bad at all. Just had to click the link that 
*   redirected me to the installation guide and installed it in the terminal.
*     
* Question 1:
*   First step was to make sure numpy and matplotlib was installed. Next was
*   to implement the run(self,x) method. Within that method we are returning
*   a nn.DotProduct object which I returned nn.DotProduct(x,self.w).
*   Then was to implement get_prediction(self,x). We needed to use nn.as_scalar
*   to convert Node into a python floating point number. I used nn.as_scalar
*   and stuck in the self.run method which was used to calculate that score for
*   data point x. Then we used that to do a comparison. If it was a negative 
*   number we returned -1, if it was non negative we returned 1. Next is the 
*   train method. We need to Loop the dataset and if the examples are 
*   misclassified, then we need to update the weights using nn.Parameter. So
*   we set the data set as true. Then we need to loop/iterate through the
*   data set. Then we need to compare the python floating point number from
*   nn.as_scalar(y) and see if it's equal to the prediction. If all of the data
*   set is true, then that means 100% training accuracy and it can terminate. 
*   If even one of the dataSet is not true, set the dataset to false and then 
*   update. Continue to iterate and update the data set. Once everything has 
*   gone through and updated, then end the method.
*
*
*   All in all, a lot of it was reading through what methods were already done and
*   working from there. A lot of it was checking, rechecking, and pushing the 
*   necessary information. In some cases comparisons needed to be made to get
*   the correct answer. I spent maybe about 1-2 hours on this assignment. It was
*   not too bad. The assignment instructionsn basically was easy to follow and 
*   helped guide me for this assignment, for question 1 that is. Reading the
*   rest of the questions was hard. There was a lot of read and a lot to understand.
*   I started on the Linear Regression one where you first initialize the model 
*   parameters like the example shown in the assignment. Then in the run is where
*   you need to compute the model predictions and start adding the bias vector to 
*   each feature vector. In get_loss, to construct that loss node it is shown on
*   the assignment that we can use the SquareLoss method to get that. I didn't do
*   the rest of the questions, but I am still looking it over and trying to 
*   understand it.
*
*****************************************************************************/

