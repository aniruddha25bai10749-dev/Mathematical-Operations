# ProgramCodes.ipynb – Ultimate Number Theory Toolkit in Python

A single, well-structured Jupyter Notebook containing **40+ pure-Python implementations** of classic and advanced number-theoretic functions, special number checks, sequences, and cryptographic primitives.

Every function is self-contained, takes interactive user input, and automatically measures **execution time** and **peak memory usage** using `tracemalloc`.

Perfect for learning, competitive programming practice, interviews, or just exploring the beauty of integers!

## Features

| Category                    | Functions                                                                                                               |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Basic Math                  | `factorial`, `is_palindrome`, `mean_of_digits`, `digital_root`                                                          |
| Special Numbers             | `is_abundant`, `is_deficient`, `is_harshad`, `is_automorphic`, `is_pronic`, `is_perfect_power`                         |
| Primes & Factorization      | `prime_factors`, `count_distinct_prime_factors`, `is_prime_power`, `is_mersenne_prime`, `twin_primes`                 |
| Divisors & Sums             | `count_divisors`, `aliquot_sum`, `are_amicable`                                                                         |
| Sequences & Persistence     | `multiplicative_persistence`, `collatz_length`, `lucas_sequence`, `polygonal_number`, `partition_function`            |
| Modular Arithmetic          | `mod_exp` (fast exponentiation), `mod_inverse`, `crt` (Chinese Remainder Theorem), `order_mod`                         |
| Advanced Number Theory      | `is_quadratic_residue`, `is_carmichael`, `is_prime_miller_rabin` (probabilistic), `pollard_rho` factorization         |
| Approximations & More       | `zeta_approx` (Riemann zeta), `is_highly_composite`, `is_fibonacci_prime`                                               |

All implementations include built-in performance profiling so you can instantly compare speed and memory usage.

## Technologies / Tools Used

- **Python 3**
- Standard library only: `time`, `tracemalloc`, `math`, `random`
- **Jupyter Notebook** (`.ipynb` format)
- No external packages required

## Steps to Install & Run the Project

### Option 1 – Run locally (recommended)
```bash

# 1. Install Jupyter (once)
pip install jupyterlab          # or: pip install notebook

# 2. Download the file ProgramCodes.ipynb
#    (or clone the whole repository)

# 3. Start Jupyter
jupyter lab                     # or: jupyter notebook


# 4. Open ProgramCodes.ipynb
```
### Manual Option 2 – Google Colab (Zero setup)
```bash

1. Go to → https://colab.research.google.com  
2. Click **File → Upload notebook**  
3. Choose the file `ProgramCodes.ipynb` from your computer  
4. That's it! Now simply click any cell and press **Shift + Enter**
```


### How to Test / Use

1. Scroll to any function you like  
   Example: `is_mersenne_prime`, `pollard_rho`, `partition_function`, etc.  
2. Click the code cell  
3. Press **Shift + Enter**  
4. Type the requested number when prompted  
5. Instantly see:  
   - The mathematical result  
   - Execution time  
   - Memory used


### How to Test Any Function

1. **Find the function** you want to try  
   (Each has a clear markdown title, e.g. `is_mersenne_prime(p)`, `pollard_rho(n)`, `partition_function(n)`, etc.)

2. **Click inside its code cell**

3. **Press `Shift + Enter`** (or click the Play button)

4. **When prompted, type your number and press Enter**  
   Examples:
   - For `factorial(n)` → type `20`
   - For `is_prime_miller_rabin(n, k)` → type `123456789012345678901` then `10`
   - For `twin_primes(limit)` → type `1000`

5. **Instant results appear below the cell**  
   You will immediately see:
   - The correct mathematical answer  
   - Execution time (in seconds)  
   - Peak memory usage (bytes or KB)

### Quick Testing Tips

| Goal                              | Recommended Functions to Try                          | Sample Input        |
|-----------------------------------|--------------------------------------------------------|---------------------|
| Speed comparison                  | Naive primality vs `is_prime_miller_rabin`            | `10**12 + 39`       |
| Memory comparison                 | `is_highly_composite` vs optimized versions          | `5040`              |
| Large numbers                     | `mod_exp`, `pollard_rho`                              | `2**64-1`           |
| Sequences                         | `lucas_sequence`, `partition_function`               | `50`, `100`         |
| Fun math                          | `collatz_length`, `multiplicative_persistence`        | `27`, `277777788888899` |

