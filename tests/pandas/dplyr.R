library(dplyr)
library(microbenchmark)
n <- 1e7
df <- tibble(x = rnorm(n), y = rnorm(n))
microbenchmark(
  df[["z"]] <- df[["x"]] + df[["y"]],
  df %>% mutate(z = x + y),
  df <- df %>% mutate(z = x + y)
)