# Localization: Histogram Filters

---

Localization focuses on the problem of how to find where an agent is within a state space (I.e. its environment). It
basically just a series of sensing and motion updates. Sensing reduces the amount of uncertainty there is in the robot
location where as the motion updates increase the amount of uncertainty (due to stochasticity or non-deterministic
movements). Histogram filters are defined by a **discrete state space where the distribution is defined over a finite set of bins**

**Note**: these methods depend on having a detailed map of the environment, otherwise they won't work well

**Localization Summary**:

- Belief = Prior Probability
- Sense = Product of probabilities followed by normalization
- Move = Convolution (Addition)
  <br>

## How a Histogram Filter Works

- The robot starts with a uniform distribution over the belief states (where it currently is) and uses features of the
  environmentto update it's beliefs and compute the posterior distribution
  <br>

## Localization Process:

Localization is really just two main steps:

1. Sense
   1. Gains information
2. Move
   1. Loses information

To compute the posterior distribution, we can follow the below steps:

1. Determine prior belief distribution
2. Compute posterior (products of probabilities)
3. Compute Sum
4. Normalize Distribution
   <br>

## Limit Distribution:

- How does the posterior distribution for inexact motion look like after infinite steps?
  - Also called the stationary distribution
  - It eventually becomes a uniform distribution because we lose information every-time we make a step
  - Distribution of absolute least information

<br>

## Bayes Rule: Measurement Update

---

The measurement update seeks to calculate a belief after seeing the measurement

$p(X_i | Z) = \dfrac {p(Z|X_i)* p(X_i)} {p(Z)}$

- Takes the prior distribution p(X) and multiplies in the chance of seeing a red or green cell -p(Z|X) - for every possible location

  - $p(Z|X)* p(X)$ == Non-Normalized posterior distribution
  - $p(Z)$ == Probability of seeing a measurement devoid of any location information
    - $p(Z) == \sum_i p(Z | X_i) * p(X_i)$

#### Cancer Test Example:

- A Rare cancer is present in 1/1000 people —> p(c) = 0.001 & p(Not c) = 1 - p(c)
  - $p(positive | \space cancer) = 0.8$
  - $p(positive | \space not \space cancer) = 0.1$
- What is $p(cancer | \space positive)$?
  - $p(cancer | \space positive) == \dfrac {p(positive | \space cancer) * p(c)} {p(positive)}$ == 0.8 \* 0.001 / 0.1007 == 0.0079
  - $p(positive) = p(not \space cancer | positive) = 0.999 * 0.1 == 0.0999$
  - Alpha (Normalizer) = 0.0999 + 0.0008 == 0.1007

<br>

## Motion - Theorem of Total Probability:

$P(X^{t}_i) = \sum_j P(X_j^{t-1}) * P(X_i | X_j) == P(A) = \sum_B P(A|B) * P(B)$

- Xi = Grid cell i
- t = time step t
- The probability of reaching grid cell $X_j$ is equal to the probabilities from all the cells the robot could have come from one
  time step earlier multiplied by the probability that our motion command would take us from $X_j to X_i$ - I.e. $P(X_i) ==$ the
  probability of all places where we could have come (cell J) from multiplied by the probability of transitioning from J to I

<br>

## Scaling Challenges

- Histogram filters scale exponentially
  - X-Y Plane: X, Y, Theta
    - If we have 20 different values for each state variable, then the number of possible values is $20^N$ where N is the number of state dimensions
      - Exponential
  - Any grid defined over K dimensions, will end up having exponentially many grid cells in the number of dimensions
  - Cant represent high dimensional problems well
