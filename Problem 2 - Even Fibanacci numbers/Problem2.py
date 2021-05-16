prev, now, sums, next_no = 1, 2, 2, 0
while next_no < 4000000:
    next_no = prev + now
    prev = now
    now = next_no
    if next_no%2 == 0:
        sums = sums + next_no
print(sums)