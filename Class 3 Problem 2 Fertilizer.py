from pulp import *
#Step 1
prob = LpProblem("Minimize Cost",LpMinimize)
#Step 2 Identify the decision variables
x1 = LpVariable("Product A", lowBound= 0, cat="integer")
x2 = LpVariable("Product B", lowBound= 0, cat="integer")
#Step 3 Objective function
prob += 10*x1 + 15*x2, "Minimize Cost"
#Step 4 Define the contraints
prob += 2*x1 + 1*x2 >= 100, "Potassium"
prob += 0.3*x1 + 0.6*x2 >= 25, "Nitrogen"
prob += 0.2*x1 + 0.2*x2 >= 10, "Ammonia"

prob.solve()
print("Optimal solution:")
print("Product A",x1.varValue)
print("Product B",x2.varValue)
print("Cost",prob.objective.value())