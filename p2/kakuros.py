
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model


model = cp_model.CpModel()

def Kakuros(xy,yx):

    a1 = model.NewIntVar(1, 9, 'a1')
    a2 = model.NewIntVar(1, 9, 'a2')
    a3 = model.NewIntVar(1, 9, 'a3')
    x1 = model.NewIntVar(1, 9, 'x1')
    x2 = model.NewIntVar(1, 9, 'x2')
    x3 = model.NewIntVar(1, 9, 'x3')
    z1 = model.NewIntVar(1, 9, 'z1')
    z2 = model.NewIntVar(1, 9, 'z2')
    z3 = model.NewIntVar(1, 9, 'z3')


    Row1 = [a1, a2, a3]
    Row2 = [x1, x2, x3]
    Row3 = [z1, z2, z3]
    Col1 = [a1, x1, z1]
    Col2 = [a2, x2, z2]
    Col3 = [a3, x3, z3]

    model.AddAllDifferent(Row1)
    model.AddAllDifferent(Row2)
    model.AddAllDifferent(Row3)
    model.AddAllDifferent(Col1)
    model.AddAllDifferent(Col2)
    model.AddAllDifferent(Col3)

    model.Add((a1 + a2 + a3) == xy[3])
    model.Add((x1 + x2 + x3) == xy[4])
    model.Add((z1 + z2 + z3) == xy[5])
    model.Add((a1 + x1 + z1) == xy[0])
    model.Add((a2 + x2 + z2) == xy[1])
    model.Add((a3 + x3 + z3) == xy[2])


    status = solver.Solve(model)
    if status == cp_model.POSS:
        xy.write(
            str(xy[3]) + ", " + str(solver.Value(a1)) + ", " + str(solver.Value(a2)) + ", " + str(solver.Value(a3)) + "\n")
        xy.write(
            str(xy[4]) + ", " + str(solver.Value(x1)) + ", " + str(solver.Value(x2)) + ", " + str(solver.Value(x3)) + "\n")
        xy.write(
            str(xy[5]) + ", " + str(solver.Value(z1)) + ", " + str(solver.Value(z2)) + ", " + str( solver.Value(z3)))




with open('kakuro_input.txt', "r") as md:
     line = md.readlines()
     
     s =[]
     for i in line:
         line_split = i.strip().split(",")
         for x in line_split:
             s.append(int(x))


with open("kakuro_output.txt", "w") as xy:
    line = line[0].strip()
    xy.writelines("x" + ", " + str(line) + "\n")
    Kakuros(s,xy)



