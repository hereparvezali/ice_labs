######### I #########
# Generate a range of Z values
z_values <- seq(-4.0, 4.0, by = 0.1)

# Calculate the corresponding PDF values
pdf_values <- dnorm(z_values)

# Plot the PDF
plot(z_values, pdf_values, type = "l", col = "blue", xlab = "Z", ylab = "Density",
     main = "Standard Normal Distribution (Z~N(0,1))")


# This is a symmetric distribution

############# II ###################
# Define parameters
mean_X <- 1000
variance_X <- 250000
standard_deviation_X <- sqrt(variance_X)

# Generate a range of X values
x_values <- seq(0, 2000, by = 10)

# Calculate the corresponding PDF values
pdf_values_X <- dnorm(x_values, mean = mean_X, sd = standard_deviation_X)

# Calculate the corresponding CDF values
cdf_values_X <- pnorm(x_values, mean = mean_X, sd = standard_deviation_X)



############# III #############

# Define the values for calculations
x_value_a <- 850
x_value_b <- 1200
lower_limit_c <- 1000
upper_limit_c <- 2000

# a) P(X = 850)
pdf_value_850 <- dnorm(x_value_a, mean = mean_X, sd = standard_deviation_X) #p(X=850) = 0.0007627756

# b) P(X > 1200) = 1 - P(X ≤ 1200)
cdf_value_1200 <- pnorm(x_value_b, mean = mean_X, sd = standard_deviation_X)
p_x_gt_1200 <- 1 - cdf_value_1200 #P(X > 1200): 0.3445783 

# c) P(1000 < X < 2000) = P(X < 2000) - P(X < 1000)
cdf_value_2000 <- pnorm(upper_limit_c, mean = mean_X, sd = standard_deviation_X)
cdf_value_1000 <- pnorm(lower_limit_c, mean = mean_X, sd = standard_deviation_X)
p_x_between_1000_and_2000 <- cdf_value_2000 - cdf_value_1000 #P(1000 < X < 2000): 0.4772499



# Plot the PDF
plot(x_values, pdf_values_X, type = "l", col = "blue", xlab = "X", ylab = "Density",
     main = "Normal Density Curve")

# Plot the CDF
plot(x_values, cdf_values_X, type = "l", col = "red", xlab = "X", ylab = "Probability",
     main = "Normal Cumulative Distribution Curve")