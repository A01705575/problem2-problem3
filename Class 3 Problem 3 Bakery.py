from pulp import *
#Step 1
prob = LpProblem("Maximize Profits",LpMaximize)
#Step 2 Identify the decision variables
x1 = LpVariable("Imperial Cake", lowBound= 0, cat="integer")
x2 = LpVariable("Lime Cake", lowBound= 0, cat="integer")
#Step 3 Objective function
prob += 8*x1 + 10*x2, "Maximize Profits"
#Step 4 Define the contraints
prob += 0.5*x1 + 1*x2 <= 10, "Sugar (kg)"
prob += 8*x1 + 8*x2 <= 120, "Eggs"

prob.solve()
print("Optimal solution:")
print("Imperial Cake",x1.varValue)
print("Lime Cake",x2.varValue)
print("Profit",prob.objective.value())