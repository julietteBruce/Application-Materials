loadPackage "TorAlgebra"

R = QQ[x_{1},x_{2},x_{3},Degrees=>{4,1,2}]

I = ideal(x_{3}^2*x_{1}-x_{3}*x_{2}^6-x_{1}^2-x_{2}^8)

S = R/I 

isGorenstein S

S = QQ[x_{3,0},x_{4,0},x_{4,1},x_{5,0},x_{5,1},Degrees=>{3,4,4,5,5}]

I = ideal (x_{4,1}*x_{4,0} + 66817*x_{4,0}^2 + 393744*x_{5,0}*x_{3,0},
x_{4,1}^2 + 166845*x_{4,0}^2 + 393744*x_{5,1}*x_{3,0} + 293716*x_{5,0}*x_{3,0},
x_{5,0}*x_{4,1} + 460560*x_{5,1}*x_{4,0},
x_{5,1}*x_{4,1} + 236078*x_{5,1}*x_{4,0} + 364132*x_{5,0}*x_{4,0} + 96429*x_{3,0}^3,
x_{5,1}^2 + 236078*x_{5,1}*x_{5,0} + 364132*x_{5,0}^2 + 436527*x_{4,1}*x_{3,0}^2 +
96429*x_{4,0}*x_{3,0}^2,
x_{5,0}*x_{4,0}^2 + 390903*x_{5,1}*x_{5,0}*x_{3,0} + 439423*x_{5,0}^2*x_{3,0} +
21137*x_{4,0}*x_{3,0}^3,
x_{5,1}*x_{4,0}^2 + 369681*x_{5,1}*x_{5,0}*x_{3,0} + 230903*x_{5,0}^2*x_{3,0} +
229658*x_{4,0}*x_{3,0}^3)

betti res I
