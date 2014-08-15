library(caret)
#Split the data into test and training sets
trainIndex<-createDataPartition(seaflow_21min$pop, 2,p=0.7,list = FALSE)
seaflowTrain <- seaflow_21min[ trainIndex,]
seaflowTest  <- seaflow_21min[-trainIndex,]

#What is the mean of the variable "time" for your training set?
trainsummary <- summary(seaflowTrain)

#Plot pe against chl_small   and color by pop

seaflow_21min$fpop <- factor(seaflow_21min$pop)
subdata <- subset(seaflow_21min, pop %in% c("crypto", "nano",
                                            "pico","synecho","ultra"))
p1<-ggplot(seaflow_21min, aes(x = chl_small, y = pe, 
                              colour = fpop)) + geom_point()


