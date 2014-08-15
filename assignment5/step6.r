#Step 6: Build and evaluate a random forest.
#Load the randomForest library, then call randomForest using 
#the formula object and the data, as you did to build a single tree:
  
library(randomForest)
rfmodel <- randomForest(fol, data=seaflowTrain)

#Evaluate this model on the test data the same way you did for the tree.
poppredict<-predict(rfmodel,seaflowTest,type = "class")
coincidences<-(poppredict==seaflowTest$pop)
accuracy<-sum(coincidences)/length(coincidences)
print(accuracy)

#Answer Question 9.
#Random forests can automatically generate an estimate of 
#variable importance during training by permuting the values in a given variable and measuring the effect on classification. If scrambling the values has little effect on the model's ability to make predictions, then the variable must not be very important.
#A random forest can obtain another estimate of variable importance 
#based on the Gini impurity that we discussed in the lecture. 
#The function importance(model) prints the mean decrease in gini 
#importance for each variable. The higher the number, the more the 
#gini impurity score decreases by branching on this variable, 
#indicating that the variable is more important.

#Call this function and answer Question 10.

importance(rfmodel)

