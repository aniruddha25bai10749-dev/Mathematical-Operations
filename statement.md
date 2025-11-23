**1. Problem Statement**

Modern computational tasks often rely on calculating complex mathematical functions. Developers, students, and researchers need reliable implementations of these functions. More critically, they require a clear understanding of the computational cost—specifically the execution time and memory footprint—associated with these implementations, especially as input size increases.

The core problem this project addresses is the need for a unified tool that not only correctly calculates fundamental mathematical values (like factorials, series sums, and partitions) but also provides built-in metrics to analyze and compare the efficiency of the underlying algorithms.

**2. Scope of the Project**

The scope of this project is to develop a modular Python library for calculating discrete and continuous mathematical functions, coupled with a performance tracking system.

**In Scope:**

Implementation of at least three core mathematical functions (Factorial, Riemann Zeta approximation, Integer Partition).

Integration of Python's time and tracemalloc modules to measure execution speed and memory usage, respectively.

Design of command-line interface (CLI) or simple script inputs for function parameters.

Focus on clear, readable, and well-documented Python code for each function.

**Out of Scope:**

Developing a full graphical user interface (GUI).

Implementing functions requiring external libraries (e.g., NumPy or SciPy), beyond basic system/utility libraries.

Formal mathematical proof or detailed analysis of theoretical Big O complexity (though the observed metrics will inform this).

**3. Target Users**

The toolkit is designed for users who are involved in computational mathematics, algorithm analysis, and software development:

Computer Science Students: Learning fundamental algorithms, data structures, and how to measure time/space complexity empirically.

Developers/Engineers: Needing quick, tested utilities for calculating common mathematical results in their projects.

Academics and Researchers: Requiring a baseline tool for performance testing different algorithmic approaches to mathematical problems.

**4. High-Level Features**

The core functionality of the toolkit is defined by the following high-level features:

**Mathematical Functionality**

**Factorial Calculation:** Computes the factorial ($n!$) for a given integer $n$.

**Riemann Zeta Approximation:** Approximates the value of the Riemann Zeta function $\zeta(s)$ for a given $s$ using a user-specified number of terms.

**Integer Partition Function:** Calculates the number of ways a positive integer $n$ can be expressed as a sum of positive integers $p(n)$, typically using Dynamic Programming.

**Performance and Utility Features**

**Execution Time Tracking:** Automatically measures and reports the execution time (in seconds) for each function call.

**Memory Usage Reporting:** Reports the peak and current memory (in bytes) allocated during the execution of each function.

**Interactive Input:** Allows the user to easily input the required parameters ($n$, $s$, number of terms) via standard input.
