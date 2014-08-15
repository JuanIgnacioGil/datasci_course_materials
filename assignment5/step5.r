#Step 5: Evaluate the decision tree on the test data.
#Use the predict function to generate predictions on your test data. 
#Then, compare these predictions with the class labels in the test data itself.

#In R, if you write A==B and A and B are vectors, 
#the result is a vector of 1s and 0s. The sum of this vector will be the number 
#of correct predictions. Dividing this sum by the size of the test 
#dataset will give you the accuracy.

#Answer Question 8.

poppredict<-predict(arbol,seaflowTest,type = "class")
coincidences<-(poppredict==seaflowTest$pop)
accuracy<-sum(coincidences)/length(coincidences)
print(accuracy)