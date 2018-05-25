library(randomForest)

df = read.csv(file="./data/proposed-assessments-as-of-april-18th.csv", header=TRUE, sep=",")
orig = read.csv(file="./data/proposed-assessments-as-of-april-18th.csv", header=TRUE, sep=",")
df = df[sapply(df, is.numeric)]
undesired <- c('X2018.Assmt.Taxable', 'X2018.Assmt.Exempt', 'X2018.Assmt.Total')
idx = !(colnames(df) %in% undesired)
df = df[,idx]

for(i in 1:ncol(df)){
  df[is.na(df[,i]), i] = median(df[,i], na.rm = TRUE)
}

rf = randomForest(X2018.Taxes.Estimated ~ ., data=df)
diff = predict(rf, df) - df$X2018.Taxes.Estimated

x = seq(0,5,0.1)
plot(seq(0,5,0.1), sapply(x, function(w) dim(df[abs(diff)>w*sd(diff),])[1]))
