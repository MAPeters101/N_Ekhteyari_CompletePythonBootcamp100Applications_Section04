
"""
try:
    # Code that may raise an exception
    # ...
except SomeExceptionType as e:
    # Code to handle the exception
    # ...
else:
    # Code to run if no exception is raised
    # ...
finally:
    # Code that runs regardless of whether an exception is raised or not.
    #...
"""

try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division Successful.")
finally:
    print("Cleanup code.")
print()


try:
    result = 10/5
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division Successful.")
finally:
    print("Cleanup code.")
print()



try:
    number = int('abc')
except ValueError as e:
    print(f"Value Error: {e}")
except TypeError as e:
    print(f"Type Error: {e}")
else:
    print("Conversion successful.")
finally:
    print("Cleanup code.")
print()

try:
    number = int(4.3)
except ValueError as e:
    print(f"Value Error: {e}")
except TypeError as e:
    print(f"Type Error: {e}")
else:
    print("Conversion successful.")
finally:
    print("Cleanup code.")
print()

try:
    number = int(4j)
except ValueError as e:
    print(f"Value Error: {e}")
except TypeError as e:
    print(f"Type Error: {e}")
else:
    print("Conversion successful.")
finally:
    print("Cleanup code.")
print()

