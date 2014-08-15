#Step 8: Construct confusion matrices
#Use the table function to generate a confusion matrix for each of your 
#three methods. Generate predictions using the predict function, 
#then call the table functions like this:
  
#table(pred = predictions, true = testingdata$pop)

#Answer Question 12.

#Tree
poppredict<-predict(arbol,seaflowTest,type = "class")
treeconf<-table(pred = poppredict, true = seaflowTest$pop)

#Random Forest
library(randomForest)
poppredict<-predict(rfmodel,seaflowTest,type = "class")
rfconf<-table(pred = poppredict, true = seaflowTest$pop)

#Support Vector Machine
library(e1071)
poppredict<-predict(svmmodel,seaflowTest,type = "class")
svmconf<-table(pred = poppredict, true = seaflowTest$pop)

#Total confusion
totalconf<-treeconf+rfconf+svmconf
print(totalconf)