# General Notes

## **Algorithms' Summary**
### **1. Brute Force**
This approach finds all the possible solutions and selects desired solution per given the constraints.

### **2. Dynamic Programming** 
It uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.

### **3. Backtracking** 
It uses Brute Force approach but to find ALL the solutions.
  - Solutions to the Backtracking problems can be represented as **State-Space Tree**.
  - The constrained applied to find the solution is called Bounding function.
  - Backtracking follows **Depth-First Search method**.
  - Branch and Bound is also a Brute Force approach, which uses Breadth-First Search method.
  
---
## Graph Theory
1. https://medium.com/@nick.kearns_74871/graph-theory-and-flight-maps-df2e9f7fa684

## Recursive Function - Pass by Value / Pass by Reference
Recursive functions cannot pass boolean in a recursive function and change it in the recursive function.
Because, boolean like many other types is `immutable`, hence passed by value and not reference.

### References:
1. https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
2. https://stackoverflow.com/questions/13299427/python-functions-call-by-reference
---