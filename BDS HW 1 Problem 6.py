import random
"""
This code uses Monte Carlo Estimation to approximate pi. 
"""
def generate_pi(num):
    in_circle = 0
    for x in range(0, num, 1):
        point = (random.uniform(-1,1), random.uniform(-1,1))
        if (point[0]**2 + point[1]**2) <= 1:
            in_circle += 1
    estimate = in_circle / float(num)
    return 4 * estimate


pi = generate_pi(100000)
print(pi)