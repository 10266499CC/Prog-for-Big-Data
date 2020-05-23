# Import relevant packages

install.packages("tm")
install.packages("SnowballC")
install.packages("rpart")
install.packages("rpart.plot")
install.packages("rattle")
install.packages("randomForest")
install.packages("e1071")

# Load the dataset from UCI website
url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"

if (!file.exists("smsspamcollection.zip")) 
{
  download.file(url=url, destfile="smsspamcollection.zip", method="curl")
}
unzip("smsspamcollection.zip")

data <- read.delim("SMSSpamCollection", sep="\t", header=F, colClasses="character", quote="")

# Overview of Dataset

class(data)
sapply(data, class)
dim(data) 
ncol(data)
nrow(data)
names(data)
head(data,5)
tail(data, 5)
summary(data)
colSums(is.na(data))

# Rename the column names

colnames(data)
colnames(data) <- c("Class", "Text")
colnames(data)

# Convert the Class column from Character strings to factor

data$Class <- factor(data$Class)

# Display the proportion of ham to spam in the dataset

prop.table(table(data$Class))

# Clean the data for machine use

library(tm)
library(SnowballC)
corpus = VCorpus(VectorSource(data$Text))
as.character(corpus[[1]])
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords("english"))
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, stripWhitespace)
as.character(corpus[[1]])

# Create a DocumentTermMatrix to keep all the relevant words.

dtm = DocumentTermMatrix(corpus)
dtm
dtm = removeSparseTerms(dtm, 0.999)
dim(dtm)

# Convert the word frequencies to Yes and No Labels

convert_count <- function(x) {
  y <- ifelse(x > 0, 1,0)
  y <- factor(y, levels=c(0,1), labels=c("No", "Yes"))
  y
}

# Apply the convert_count function to get final training and testing DTMs

datasetNB <- apply(dtm, 2, convert_count)

dataset = as.data.frame(as.matrix(datasetNB))

# Keep words which appeared more than 60 times

freq<- sort(colSums(as.matrix(dtm)), decreasing=TRUE)
tail(freq, 10)

# Add response variable “Class” to the dataset

dataset$Class = data$Class
str(dataset$Class)

# Split data into Train and Test sets

# Set random seed

set.seed(222)
split = sample(2,nrow(dataset),prob = c(0.75,0.25),replace = TRUE)
train = dataset[split == 1,]
test = dataset[split == 2,] 

prop.table(table(train$Class))

# Print the structure of train and test

str(train)

str(test)

##### Random Forest Model 

library(randomForest)

rfc = randomForest(x = train[-1210], y = train$Class, ntree = 300)

rfc

# Predicting the Test set results

rfc_pred = predict(rfc, newdata = test[-1210])

# Making the Confusion Matrix

library(caret)

confusionMatrix(table(rfc_pred,test$Class))

#### Naive Bayes Classifier Model

library(e1071)
control <- trainControl(method="repeatedcv", number=10, repeats=3)
system.time( classifier_nb <- naiveBayes(train, train$Class, laplace = 1,
                                         trControl = control,tuneLength = 7) )

# Predicting the Test set results

nb_pred = predict(classifier_nb, type = 'class', newdata = test)

# Making Confusion Matrix

confusionMatrix(nb_pred,test$Class)

#### SVM

svm_classifier <- svm(Class~., data=train)
svm_classifier

# Predicting the Test set results

svm_pred = predict(svm_classifier,test)

# Making Confusion Matrix

confusionMatrix(svm_pred,test$Class)

