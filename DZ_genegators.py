
def all_variants(n):
    for start in range(len(n)):
        for end in range(start + 1, len(n) + 1):
            yield n[start:end]

for s in all_variants('abc'):
    print(s)

