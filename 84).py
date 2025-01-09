# 84)How many except statements can a try-except block have? Name Some built-in exception classes:
#
# --> In Python, a try-except block can have multiple except statements to handle different types of exceptions.
#
# --> ex.
#     try:
#         x = 10 / 0  # ZeroDivisionError
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     except ValueError:
#         print("ValueError occurred!")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
