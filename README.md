### Make sure to view in light mode to see maths!!

We are trying to solve 

<img src="https://render.githubusercontent.com/render/math?math=Ax=b">

for x, where 

<img src="https://render.githubusercontent.com/render/math?math=A\in\R^{m\times n}, x\in\R^{n}, A\in\R^{m}, n=27, m=556">

The exact solution is not always possible as b is in A's null space.

We are trying to bring $Ax$ as close as possible to $b$ - we can treat this like an optimisation problem:

<img src="https://render.githubusercontent.com/render/math?math=x^* = \argmin_x\|Ax - b\|_2^2 =\argmin_x\left((Ax - b)^\intercal(Ax-b)\right)">


Expanding the term in the minimisation, we have: 

<img src="https://render.githubusercontent.com/render/math?math=f(x) = (Ax - b)^\intercal (Ax-b) ">
<img src="https://render.githubusercontent.com/render/math?math=f(x) = (x^\intercal A^\intercal - b^\intercal)(Ax-b)">
<img src="https://render.githubusercontent.com/render/math?math=f(x) = x^\intercal A^\intercal Ax + b^\intercal b - b^\intercal Ax - x^\intercal A^\intercal b">


Differenting wrt $x$ and setting to zero:
<img src="https://render.githubusercontent.com/render/math?math=\nabla_xf(x)|_{x^*} = 2 A^\intercal A x^* - 2 A^\intercal b = 0">
<img src="https://render.githubusercontent.com/render/math?math=\implies x^* = (A^\intercal A)^{-1}A^\intercal b">

... we arrive at the pseudoinverse:
<img src="https://render.githubusercontent.com/render/math?math=A^+ \triangleq (A^\intercal A)^{-1}A^\intercal\ ; \quad x_{OLS} = A^+ b">

The psuedoinverse is implemented in solution.py


