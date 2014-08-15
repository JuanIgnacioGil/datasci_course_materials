#Step 7: Train a support vector machine model and compare results.
#Use the e1071 library and call model <- svm(fol, data=trainingdata).

#Answer Question 11.

library(e1071)
svmmodel <- svm(fol, data=seaflowTrain)

poppredict<-predict(svmmodel,seaflowTest,type = "class")
coincidences<-(poppredict==seaflowTest$pop)
accuracy<-sum(coincidences)/length(coincidences)
print(accuracy)