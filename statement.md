### Problem Statement  
There is a significant lack of **ready-to-run, educational, and performance-aware** implementations of classic and advanced number-theoretic functions in a single, accessible place. Students, competitive programmers, and self-learners often have to search multiple sources, copy incomplete code, or write everything from scratch — without any insight into time and memory efficiency of different approaches.

This project solves that problem by providing a **comprehensive, interactive, zero-install Jupyter Notebook** containing over 40 fundamental and advanced mathematical functions related to integers, all implemented in pure Python with automatic performance benchmarking.

### Scope of the Project  
The notebook covers a wide spectrum of number theory and recreational mathematics topics including but not limited to:

- Basic arithmetic and digit manipulation  
- Special number classifications (abundant, deficient, Harshad, automorphic, etc.)  
- Prime factorization, primality testing (deterministic & probabilistic), Mersenne primes, twin primes  
- Divisor functions, aliquot sums, amicable pairs  
- Sequences: Lucas, polygonal, integer partitions, Collatz conjecture steps  
- Modular arithmetic: fast exponentiation, modular inverse, Chinese Remainder Theorem, multiplicative order  
- Cryptographic and advanced primitives: Miller-Rabin, Pollard Rho factorization, Carmichael numbers  
- Mathematical approximations: Riemann zeta function, multiplicative persistence  

Each implementation includes real-time measurement of **execution time** and **peak memory usage**.

### Target Users  
This project is designed for:

- Undergraduate and high-school students learning number theory or algorithms  
- Competitive programming enthusiasts (CP platforms: Codeforces, AtCoder, LeetCode, etc.)  
- Interview candidates preparing for technical roles requiring mathematical reasoning  
- Educators and tutors looking for clean, executable examples  
- Hobbyists and math lovers who enjoy exploring properties of numbers interactively  

### High-Level Features  

| Feature                                 | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| 40+ complete implementations           | From basic factorial to Pollard Rho factorization and Miller-Rabin primality |
| Zero external dependencies              | Runs on any Python 3 environment — including Google Colab                   |
| Interactive input                       | Each function prompts the user for input — no code modification needed      |
| Built-in performance benchmarking       | Automatic timing and memory profiling using `time` and `tracemalloc`        |
| One-click execution                     | Works instantly in Google Colab or any local Jupyter installation          |
| Educational & comparison-ready          | Compare naive vs. optimized algorithms side-by-side with real metrics      |
| Fully self-contained cells              | Run any function independently in any order                                |
| Clean, readable, well-commented code    | Ideal for learning and teaching purposes                                    |

This notebook serves as both a **practical toolkit** and an **interactive learning resource** for anyone passionate about mathematics and efficient programming.
