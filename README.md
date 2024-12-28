# Silent Failure in Python Function

This repository demonstrates an uncommon bug in Python where an unexpected return value masks a potential `ZeroDivisionError`.  The function `function_with_uncommon_bug` returns 1 when the input is 0, while raising a `ZeroDivisionError` for all other inputs.  This behavior is not immediately obvious and could lead to hard-to-debug issues in larger applications.

## Bug Description
The function's unexpected behavior when x == 0 prevents the detection of a more significant error. This behavior can lead to difficult to debug issues, especially in larger applications where it may not be apparent that the function is failing in certain situations.

## Solution
The recommended solution is to handle potential `ZeroDivisionError` exceptions and to maintain a consistent behavior to avoid unexpected outcomes.
