
ages <- c(89,89,87,86,85,83,83,82,81,80,78,78,77,76,73,73,73,72,69,69,68,67,66,66,65,65,64,63,61,61,60,59,58,57,56,54,54,53,53,51,51,49,47,46,44,43,42,36,2000)

###### II #########
# The mean, median frequency table and mode of the ages from 50 people here
ages_mean1<-mean(ages)
ages_mean1
ages_median1<-median(ages)
ages_median1
ages_frequency1 <- table(ages)
ages_mode1<-as.numeric(names(ages_frequency1[ages_frequency1 == max(ages_frequency1)]))
ages_mode1

# Here median is the best description of central tendency because the it will affected less by the value 2000


######### III ##########
# Replacing 2000 with 35 in the position where 2000 is
ages[ages==2000]<-35

ages_mean2<-mean(ages)
ages_mean2
ages_median2<-median(ages)
ages_median2
ages_frequency2 <- table(ages)
ages_mode2<-as.numeric(names(ages_frequency2[ages_frequency2 == max(ages_frequency2)]))
ages_mode2

#lets determine the differences by creating a data frame
data.frame(c(ages_mean1,ages_median1,ages_mode1),c(ages_mean2,ages_median2,ages_mode2))
# we can see that the value of mean fluctuated mostly and the least fluctuation is in mode


########## IV #########

# sorting ages in ascending order
ages_sorted<-sort(ages)

# length after trimming 2% of observation 
trimmed_length<-round(length(ages)*2/100)
# trimmed mean after trimming 2% from both starting and ending
ages_mean_trimmed<-mean(ages[(trimmed_length+1):(length(ages)-trimmed_length)])
ages_mean_trimmed

###### V #######
# construction of frequency distribution table after replacing 2000 with 35 
ages_frequency<-table(ages)
data.frame(ages_frequency)


####### VI #########
#construction of relative frequency table and histogram
ages_frequency_relative<-ages_frequency/length(ages)
barplot(ages_frequency_relative, main="Histogram for relative frequency", xlab="Ages", ylab="Relative frequency")

####### VII ########
#Skewness and Kurtosis
x<-ages
ages_skewness<-sum((x-mean(x))^3)/(sqrt(sum((x-mean(x))^2)))^3
ages_skewness

ages_kurtosis<-sum((x-mean(x))^4)/(sum(x-mean(x))^2)^2
ages_kurtosis
# comment:

######## VIII #########
# Standard deviation, Mean deviation about median and Coefficient of varience
ages_sd<-sd(ages)
ages_sd

ages_mdm<- mean(abs(ages-median(ages)))
ages_mdm

ages_cofvar<-ages_sd/mean(ages)
ages_cofvar