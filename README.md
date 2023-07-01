# Ai_genetic_Algorithms
This code implements a genetic algorithm to solve an optimization problem. The problem is not specified in the code, but it is assumed that a solution is represented by a list of 8 integers, and the fitness of a solution is evaluated using the fitness function.

The work function is the main driver of the genetic algorithm. It takes a population of candidate solutions (pop) and the number of iterations (n) as inputs. The function first evaluates the fitness of each candidate solution using the fitness function, and stores them in a dictionary (dec) where the keys are the fitness values and the values are the candidate solutions.

The function then selects the two candidate solutions with the highest fitness values, and creates two new candidate solutions by applying the mutation operator to them. The mutation operator randomly changes one of the integers in the candidate solution to a new random value between 0 and 9.

The function then creates a new population of candidate solutions by combining the two original candidate solutions and the two new candidate solutions. This new population is passed to a recursive call of the work function with n+1 iterations.

The code also includes a commented-out section that implements a cross function to create new candidate solutions by performing one-point crossover on the two original candidate solutions with the highest fitness values. However, this section is not used in the current implementation.

The code is executed by calling the work function with an initial population of candidate solutions (inti_pop) and 0 iterations. The best solution found by the genetic algorithm after 100 iterations is printed.

Overall, the code is a simple implementation of a genetic algorithm for a generic optimization problem.
