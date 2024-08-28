# libigl Studies

## What is libigl?

Libigl is an open-source C++ library for geometry processing research and development. It is a header-only library. 

1. No complex data types.
2. Minimal dependencies. 
3. Header-only. 
4. Function encapsulation. 


## Libigl expects vertices and faces to be in Eigen matrices

```C++
Eigen::Matrix<double, Eigen:;Dynamic,3> V;
Eigen::Matrix<int, Eigen::Dynamic, 3> F;

// OR
Eigen::MatrixXd V;
eigen::MatrixXi F;

```

