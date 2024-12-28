def function_with_uncommon_bug_fixed(x):
    try:
        if x == 0:
            return 0 # Fixed: Returning 0 instead of 1 for consistency
        else:
            return x / x #Fixed:Avoiding ZeroDivisionError
    except ZeroDivisionError:
        return float('inf')  # Handle ZeroDivisionError gracefully

result = function_with_uncommon_bug_fixed(0)
print(result)  # Prints 0
result = function_with_uncommon_bug_fixed(5)
print(result) #Prints 1.0
result = function_with_uncommon_bug_fixed(0)
print(result) #Prints 0