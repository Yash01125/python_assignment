#69)How  will you set the starting value in generating random numbers?

# --> use the random.seed() function. Setting a seed ensures that the sequence of random numbers
# generated is reproducible.
#
# --> ex.
#     import random
#
#     random.seed(42)  # Set the seed to a fixed value
#     print(random.randint(1, 10))  # Output will always be the same for this seed
#     print(random.random())        # Output will always be the same for this seed
