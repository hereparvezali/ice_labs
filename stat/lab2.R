score<-c(77,44,49,33,38,33,76,55,68,39,44,59,36,55,47,61,53,32,65,51,29,41,32,45,83,58,73,47,40,26,59,43,66,44,41,25,39,72,37,55,34,47,66,53,55,58,49,45,61,41,55,92,83,77,45,62,45,36,78,48,54,50,51,66,80,73,57,61,56,50,45,82,71,48,46,69,38,72,56,64)

######### I ########

score_mean<-mean(score)
score_median<-median(score)
score_var<-var(score)
score_sd<-sd(score)

# mean of the scores
score_mean
# median of the scores divides the score in two such as left and right part
score_median
# score_mode
sort(table(score),decreasing = TRUE)[1]
# variance of the score of 80 students
score_var
# the standard deviation of 80 students
score_sd



######## II ##########
# Five number summaries where the corresponding five values determines the minimum, first quantile, median, third quantile and the maximum value of the score for 80 students
fivenum(score)

######## III ######
# selection of appropriate class interval and organizing data into a frequency distribution
score_frequency<-table(score)
k=1+3.322*log(80)
score_interval<-(max(score)-min(score))/k
score_frequency_break<-seq(25,95,by=floor(score_interval))
score_frequency_final<-table(cut(score,score_frequency_break,left=FALSE,right=FALSE))
score_frequency_result<-as.data.frame(score_frequency_final)
score_frequency_result


########### IV #########
# Histogram and Ogive from the classified frequency table

d<-data.frame(score_frequency_final)

# Create a histogram of the frequency distribution
score_hist<-barplot(height = d$Freq, names.arg = d$Var1, main = "Histogram", xlab = "Class Interval", ylab = "Frequency")
score_hist
# Add a vertical line at the mean and median to the barplot
abline(v = mean_value, col = "red", lwd = 3)
abline(v = median_value, col = "blue", lwd = 3)

cumulative_freq <- cumsum(d$Freq)
plot(cumulative_freq, type = "o", main = "Ogive for the frequency distribution", xlab = "Scores", ylab = "Cumulative Frequency",col = "red")

# Mark Mean on Ogive

abline(h = mean_value, col = "red", lty = 2, lwd = 2)

# Mark Median on

Ogive abline(h = median_value, col = "blue", lty = 2, lwd = 2)


########### V ##########\
# Create a data frame with the frequency distribution
data <- data.frame(
  ClassInterval = c("25-30",
                    "30-35", "35-40", "40-45", "45-50", "50-55", "55-60","60-65", "65-70", "70-75", "75-80", "80-85",
                    "85-90","90-95"),
  Frequency =c(3, 5, 7, 8, 13, 7, 12, 5, 6, 5, 4, 4, 0, 1)
)

# Calculate the midpoint of each class interval
data$Midpoint <- sapply(strsplit(data$ClassInterval, "-"), function(x) mean(as.numeric(x)))

# Calculate the weighted mean
mean_w <- sum(data$Midpoint * data$Frequency) / sum(data$Frequency)

# Calculate the median
cumulative_freq <- cumsum(data$Frequency)
total_freq <- sum(data$Frequency)
median_class <- data$ClassInterval[which(cumulative_freq >= total_freq / 2)[1]]

#Median
median <- as.numeric(unlist(strsplit(median_class, "-")))[1]

# Calculate the mode
mode <- data$Midpoint[which.max(data$Frequency)]


######### VI ###########
# Showing the leaf display and data stem
stem(score)