# Calculate the mean and median
mean_score <- mean(scores)
median_score <- median(scores)

# Create a histogram from the classified data frame
hist(freq_df$Class_Interval, 
     breaks = seq(0, max(freq_df$Class_Interval) + interval_width, by = interval_width), 
     main = "Histogram of Scores", 
     xlab = "Score Ranges", 
     ylab = "Frequency",
     col = "lightblue", 
     border = "black")

# Add labels to the x-axis
axis(1, at = seq(0, max(freq_df$Class_Interval) + interval_width, by = interval_width), 
     labels = unique(freq_df$Class_Interval))

# Add grid lines
grid()

# Add vertical lines for mean and median
abline(v = mean_score, col = "red", lwd = 2, lty = 2)  # Mean in red dashed line
abline(v = median_score, col = "blue", lwd = 2, lty = 2)  # Median in blue dashed line

# Show the histogram
