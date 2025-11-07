# Set the seed for reproducibility
set.seed(1234)

# Initialize a vector X to store the outcomes
vec <- rep(0, 1000)
n <- 5
x <- 0:n
p <- 0.3

# Generate the random sample
for(i in 1:1000){
  uni <- runif(n, 0, 1)  # Generate n random numbers from a uniform(0,1) distribution
  vec[i] <- sum(uni < p)   # Count how many val %>% ues are less than p
}

# Calculate the true probability distribution
prob <- dbinom(x, n, p)
prob
# Calculate the observed probability distribution
f <- as.numeric(table(vec))
observed_prob <- f/1000
observed_prob