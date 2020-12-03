resources = {}
line_count = 0
resource = ""

data = input()

while not data == "stop":

    if line_count % 2 == 0:
        resource = data
        if resource not in resources:
            resources[resource] = 0

    elif not line_count % 2 == 0:
        quantity = int(data)
        resources[resource] += quantity

    line_count += 1
    data = input()

for resource in resources:
    print(f"{resource} -> {resources.get(resource)}")