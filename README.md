 **Python Computational Number Theory & Mathematics Library**

 **Overview of the Project**

This project is a collection of Python functions implemented within a single Jupyter Notebook (ProgramCodes.ipynb). It serves as a comprehensive computational library primarily focused on Number Theory (primes, factorization, divisibility, properties of numbers) and Computational Mathematics (sequences, modular arithmetic, approximations).

The primary goal of the notebook is to provide runnable, self-contained implementations of these mathematical concepts, with an emphasis on measuring performance. Each function implementation is accompanied by code using Python's built-in time and tracemalloc modules to calculate execution time and peak memory usage, offering basic insights into the efficiency of each algorithm.

 **Features**

The library includes implementations for a wide range of mathematical functions, categorized as follows:

**1. Number Properties & Classification**

**Factorial**

Checking for properties like Palindromic, Abundant, Deficient, Harshad, Automorphic, and Pronic numbers.

Calculations such as Mean of Digits and Digital Root.

Checking if a number is a Perfect Power.

**2. Prime Numbers & Factorization**

Calculating Prime Factors and Counting Distinct Prime Factors.

Testing for Prime Power and Mersenne Primes.

Generating Twin Primes.

Advanced primality testing using the Miller-Rabin Algorithm.

Factorization using the Pollard's Rho Algorithm.

Checking for Carmichael Numbers.

**3. Divisibility & Modular Arithmetic**

Calculating Aliquot Sum (sum of proper divisors) and Count Divisors.

Checking for Amicable Numbers.

Efficiently calculating Modular Exponentiation (mod_exp).

Finding the Modular Multiplicative Inverse and the Multiplicative Order.

Checking for Quadratic Residues.

Note: An incomplete implementation of the Chinese Remainder Theorem (crt) is included.

**4. Sequences & Iterative Processes**

Calculating the length of the Collatz Sequence.

Generating the Lucas Sequence.

Calculating Multiplicative Persistence.

Calculating the $n$-th Polygonal Number.

Checking for Fibonacci Primes.

**5. Advanced Computational Math**

Approximation of the Riemann Zeta function ($\zeta(s)$).

Computation of the Partition Function $p(n)$.

**Technologies/Tools Used:**

**Language**: Python 3.x

**Environment**: Jupyter Notebook (.ipynb file format)

**Key Python Modules:**

**math:** For core mathematical operations (e.g., square roots, powers).

**time:** For measuring function execution time.

**tracemalloc:** For tracking and measuring memory allocation (peak memory usage).

 **Steps to Install & Run the Project:**

Since the project is distributed as a Jupyter Notebook, the setup is straightforward.

**Prerequisites:**

You need to have Python and the necessary packages installed. We recommend using pip and potentially a virtual environment.

**Python:** Ensure Python 3.x is installed on your system.

**Jupyter:** Install the Jupyter Notebook package.

pip install jupyter


**Running the Notebook:**

**Download:** Download the ProgramCodes.ipynb file to your local machine.

**Start Jupyter:** Open your terminal or command prompt, navigate to the directory where you saved the file, and start the Jupyter Notebook server:

jupyter notebook


**Open Project:** A browser window will automatically open showing the Jupyter dashboard. Click on ProgramCodes.ipynb to open the file.

**Execute:** You can run all cells sequentially by selecting Cell > Run All from the menu, or run cells individually. Many functions prompt the user for input (input()) in the code cell itself.

** Instructions for Testing:**

Every function in the notebook is designed to be tested directly within its respective code cell.

**1. Manual Input Testing**

Each function's code block already includes an input() call to test the function immediately upon execution.

**Select a Cell:** Click on the code cell for the function you want to test (e.g., the cell for is_pronic(n)).

**Run the Cell:** Press Shift + Enter or click the "Run" button.

**Provide Input:** The cell will prompt you to enter a number (e.g., Enter n: ).

**Verify Output:** The function's result (e.g., True or False, or a calculated value) will be printed, followed by the Execution Time and Memory Used metrics.

**2. Performance Verification**

The integrated performance measurement ensures that every test run also acts as a performance check.

To verify the performance analysis, simply observe the values printed after the function output:

**Execution Time:** Confirms the time taken.

**Memory Used:** Confirms the peak memory utilized.

**Testing Edge Cases:** It is recommended to manually edit the n = int(input(...)) line to test:

**Small Inputs (1-10):** For basic verification.

**Large Inputs (10^6 or higher):** To observe performance scaling and memory consumption for functions like prime_factors or mod_exp.
