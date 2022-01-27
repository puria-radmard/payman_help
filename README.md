### Make sure to view in light mode to see maths!!

We are trying to solve 

<img src="https://render.githubusercontent.com/render/math?math=Ax=b">

for x, where 

<img src="https://render.githubusercontent.com/render/math?math=A\in\R^{m\times n}, x\in\R^{n}, A\in\R^{m}, n=27, m=556">

The exact solution is not always possible as b is in A's null space.

We are trying to bring $Ax$ as close as possible to $b$ - we can treat this like an optimisation problem:

<img src="https://render.githubusercontent.com/render/math?math=x^* = \argmin_x\|Ax - b\|_2^2 =\argmin_x\left((Ax - b)^\intercal(Ax-b)\right)">


Expanding the term in the minimisation, we have: 

<img src="https://render.githubusercontent.com/render/math?math=f(x) = (Ax - b)^\intercal (Ax-b)">
<img src="https://render.githubusercontent.com/render/math?math=f(x) = (x^\intercal A^\intercal - b^\intercal)(Ax-b)">
<img src="https://render.githubusercontent.com/render/math?math=f(x) = x^\intercal A^\intercal Ax + b^\intercal b - b^\intercal Ax - x^\intercal A^\intercal b">


Differenting wrt $x$ and setting to zero:
<img src="https://render.githubusercontent.com/render/math?math=\nabla_xf(x)|_{x^*} = 2 A^\intercal A x^* - 2 A^\intercal b = 0">
<img src="https://render.githubusercontent.com/render/math?math=\implies x^* = (A^\intercal A)^{-1}A^\intercal b">

... we arrive at the pseudoinverse:
<img src="https://render.githubusercontent.com/render/math?math=A^+ \triangleq (A^\intercal A)^{-1}A^\intercal\ ; \quad x_{OLS} = A^+ b">

The psuedoinverse is implemented in solution.py

However, you also have another loss function to minimise, which is the distance from the target, $\tilde x$.

You can generalise the overall loss function as <img src="https://render.githubusercontent.com/render/math?math=f(x) = (x^\intercal A^\intercal - b^\intercal)(Ax-b) + \lambda (x - \tilde x)^\intercal (x - \tilde x)">

Where lambda weighs the importance of staying close to the target vector. Following the same logic, the solution is now

<img src="https://render.githubusercontent.com/render/math?math=x^*_\lambda = (A^\intercal A + \lambda I)^{-1} (\lambda \tilde x + A^\intercal b)">

This is implemented in solution2.py, and performance is compared for some values of $\lambda$

By comparing the scales of the summed pairs (that is comparing $A^\intercal A$ with $\lambda I$, and $\lambda \tilde x$ with $A^\intercal b$), we can tell that \lambda must be on the order of 10000. Indeed, errors.png shows need for a lambda on this order when errors equal each other.

By adjusting `_l` in ` x_regularised = regularised_ordinary_least_squares(A, b, target_x, _l)`, you can find a solution that suits you. NB: the errors in errors.png are not the actual, raw errors for each regularisation weight, but the normalised errors. See function documentation for more information here.
