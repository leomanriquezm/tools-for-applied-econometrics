#some dataframe
df <- data.frame(X1 = c(1, 2, 3),
                 X2 = c(4, 5,6),
                 X3 = c(7, 8, 9))

#dataset variable names
variables <- colnames(df)

#generates all possible combinations of the variables
combinations <- unlist(lapply(1:length(variables), function(i) combn(variables, i, simplify = FALSE)), recursive = FALSE)





