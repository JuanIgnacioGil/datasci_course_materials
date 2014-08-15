#Step 4: Train a decision tree
library(rpart)

fol <- formula(pop ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
arbol <- rpart(fol, method="class", data=seaflowTrain)
print(arbol)