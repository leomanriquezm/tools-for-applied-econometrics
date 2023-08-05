# Simulated data
set.seed(12345)
n <- 1000
k <-2
X <- cbind(1, matrix(rnorm(n * k), n, k))
true_coeff <- rnorm(k,1,1)
y <- X %*% true_coeffs + rnorm(n)

#Likelihood function
ols_likelihood <- function(params,data) {
  #parameters
  beta <- params
  #Y and X definition
  X <- data$X
  y <- data$y
  ###########
  predicted <- X %*% beta
  residuals <- y - predicted
  #Calculated log-likelihood to normal distribution (for residual terms)
  log_likelihood <- sum(dnorm(residuals, mean = 0, sd = 1, log = TRUE))
  return(log_likelihood)
}

#initial point
initial_params <- rep(1,ncol(X))
#Data for likelihood function
data <- list(X = X, y = y)
#Solving
result <- optim(initial_params, ols_likelihood, data = data, method = "BFGS")
print(result$par)