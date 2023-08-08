from logger_module import logger

# Define a different path for the log file
path = 'another_log.log'

# Apply the logger decorator to functions
@logger(path)
def multiply(a, b):
    return a * b

@logger(path)
def power(base, exponent):
    return base ** exponent

# Test the functions
result_multiply = multiply(5, 3)
result_power = power(2, 4)

print("Multiplication result:", result_multiply)
print("Power result:", result_power)
