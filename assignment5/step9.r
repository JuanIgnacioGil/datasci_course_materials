#Step 8: Sanity check the data
#As a data scientist, you should never trust the data, 
#especially if you did not collect it yourself. 
#There is no such thing as clean data. 
#You should always be trying to prove your results wrong by finding 
#problems with the data. Richard Feynman calls it 
#"bending over backwards to show how you're maybe wrong." 
#This is even more critical in data science, 
#because almost by definition you are using someone else's data 
#that was collected for some other purpose rather than the experiment 
#you want to do. So of course it's going to have problems.

#The measurements in this dataset are all supposed to be continuous 
#(fsc_small, fsc_perp, fsc_big, pe, chl_small, chl_big), but one is not. 
#Using plots or R code, figure out which field is corrupted.

p3<-ggplot(seaflow_21min, aes(x = time, y = fsc_small, 
                              colour = fpop)) + geom_point()

p4<-ggplot(seaflow_21min, aes(x = time, y = fsc_perp, 
                              colour = fpop)) + geom_point()

#(fsc_big is the discrete field)
p5<-ggplot(seaflow_21min, aes(x = time, y = fsc_big, 
                              colour = fpop)) + geom_point()

p6<-ggplot(seaflow_21min, aes(x = time, y = pe, 
                              colour = fpop)) + geom_point()

p7<-ggplot(seaflow_21min, aes(x = time, y = chl_small, 
                              colour = fpop)) + geom_point()

p8<-ggplot(seaflow_21min, aes(x = time, y = chl_big, 
                              colour = fpop)) + geom_point()

#Answer Question 13

#There is more subtle issue with data as well. 
#Plot time vs. chl_big, and you will notice a band of the data looks out of place.
#This band corresponds to data from a particular file for 
#which the sensor may have been miscalibrated. 
#Remove this data from the dataset by filtering out all data associated 
#with file_id 208, then repeat the experiment for all three methods, 
#making sure to split the dataset into training and test sets after 
#filtering out the bad data.

#Answer Question 14

#Filter the data set
filteredseaflow<-subset(seaflow_21min,file_id != 208)

#Split the data into test and training sets
library(caret)
trainIndex<-createDataPartition(filteredseaflow$pop, 2,p=0.7,list = FALSE)
seaflowTrain <- filteredseaflow[ trainIndex,]
seaflowTest  <- filteredseaflow[-trainIndex,]


