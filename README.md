We are trying to solve $Ax=b$ for $x$, where $A\in\R^{m\times n}, x\in\R^{n}, A\in\R^{m}$, with $n=27, m=556$.

The exact solution is not always possible as $b$ is in $A$'s null space, which we denote as $b\in \text{N}(A)$.

We are trying to bring $Ax$ as close as possible to $b$ - we can treat this like an optimisation problem:

$$
x^* = \argmin_x\|Ax - b\|_2^2 =\argmin_x\left(
    (Ax - b)^\intercal (Ax-b)
    \right)
$$

Expanding the term in the minimisation, we have: 
$$
f(x) = (Ax - b)^\intercal (Ax-b) 
\\ f(x) = (x^\intercal A^\intercal - b^\intercal)(Ax-b)
\\ f(x) = x^\intercal A^\intercal Ax + b^\intercal b - b^\intercal Ax - x^\intercal A^\intercal b
$$

Differenting wrt $x$ and setting to zero:
$$
\nabla_xf(x)|_{x^*} = 2 A^\intercal A x^* - 2 A^\intercal b = 0
\implies x^* = (A^\intercal A)^{-1}A^\intercal b
$$

... we arrive at the pseudoinverse: 
$$
A^+ \triangleq (A^\intercal A)^{-1}A^\intercal\ ; \quad x_{OLS} = A^+ b
$$

The psuedoinverse is implemented in solution.py


