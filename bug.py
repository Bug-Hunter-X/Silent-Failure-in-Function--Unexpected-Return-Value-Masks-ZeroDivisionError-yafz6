def function_with_uncommon_bug(x):
    if x == 0:
        return 1  # This line might seem correct but it leads to unexpected behavior
    else:
        return x / 0  # ZeroDivisionError

result = function_with_uncommon_bug(0)
print(result)  # Unexpectedly prints 1, masking a potential error