n_lines = int(input())

full_capacity = 0

for i in range(n_lines):
    fill_quantity = int(input())
    full_capacity += fill_quantity
    if full_capacity > 255:
        print(f"Insufficient capacity!")
        full_capacity -= fill_quantity
        continue

print(f"{full_capacity}")