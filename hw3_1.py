multiples = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            multiples[j] += 1

print(multiples)
