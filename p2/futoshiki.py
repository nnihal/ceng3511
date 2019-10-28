from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

inputFile=open("futoshiki_input.txt", "r")

model = cp_model.CpModel() 


A1 = model.NewInteger(1, num_i - 1, "A1")
A2 = model.NewInteger(1, num_i - 1, "A2")
A3 = model.NewInteger(1, num_i - 1, "A3")
A4 = model.NewInteger(1, num_i - 1, "A4")

B1 = model.NewInteger(1, num_i - 1, "X1")
B2 = model.NewInteger(1, num_i - 1, "X2")
B3 = model.NewInteger(1, num_i - 1, "X3")
B4 = model.NewInteger(1, num_i - 1, "X4")

C1 = model.NewInteger(1, num_i - 1, "Y1")
C2 = model.NewInteger(1, num_i - 1, "Y2")
C3 = model.NewInteger(1, num_i - 1, "Y3")
C4 = model.NewInteger(1, num_i - 1, "Y4")

D1 = model.NewInteger(1, num_i - 1, "Z1")
D2 = model.NewInteger(1, num_i - 1, "Z2")
D3 = model.NewInteger(1, num_i - 1, "Z3")
D4 = model.NewInteger(1, num_i - 1, "Z4")

elements.append(A1)
elements.append(A2)
elements.append(A3)
elements.append(A4)

elements.append(X1)
elements.append(X2)
elements.append(X3)
elements.append(X4)

elements.append(Y1)
elements.append(Y2)
elements.append(Y3)
elements.append(Y4)

elements.append(Z1)
elements.append(Z2)
elements.append(Z3)
elements.append(Z4)


for line in inputFile:
    lineArray=line.split(", ")
    if "\n" in lineArray[1]:
        lineArray[1]=lineArray[1][:-1]
    if lineArray[1].isdigit():
        
        model.Add(vars()[lineArray[0]]==int(lineArray[1]))
    else:
        model.Add(vars()[lineArray[0]]>vars()[lineArray[1]])
solver = cp_model.CpSolver()

status = solver.Solve(model)
if status == cp_model.P:
    fileOutput=open("futoshiki_output.txt", "w+")
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(A1),solver.Value(A2),solver.Value(A3),solver.Value(A4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(X1),solver.Value(X2),solver.Value(X3),solver.Value(X4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(Y1),solver.Value(Y2),solver.Value(Y3),solver.Value(Y4)))
    fileOutput.write("{0}, {1}, {2}, {3}".format(solver.Value(Z1),solver.Value(Z2),solver.Value(Z3),solver.Value(Z4)))
    fileOutput.close()



