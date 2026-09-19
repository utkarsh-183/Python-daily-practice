work = "education"

# 1. Basic slicing
print(work[0:5])      # educa
print(work[1:5])      # duca

# 2. Default start and end
print(work[:5])       # educa
print(work[3:])       # cation
print(work[:])        # education

# 3. Negative indexing
print(work[-1])       # n
print(work[-3:])      # ion
print(work[:-3])      # educat

# 4. Step
print(work[0:8:2])    # euto
print(work[::2])      # euto

# 5. Reverse string
print(work[::-1])     # noitacude

# 6. Reverse with step
print(work[7:2:-1])   # noita