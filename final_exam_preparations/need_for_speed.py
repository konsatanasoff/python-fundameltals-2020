def drive(cars, car, d, f):
    if cars[car]['fuel'] >= f:
        cars[car]['fuel'] -= f
        cars[car]['mileage'] += d
        print(f"{car} driven for {d} kilometers. {f} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    else:
        print("Not enough fuel to make that ride")
    return cars


def refuel(cars, car, f):
    car_fuel = cars[car]['fuel']
    car_fuel += f
    if car_fuel > 75:
        r_fuel = 75 - (car_fuel - f)
        car_fuel = 75
        print(f"{car} refueled with {r_fuel} liters")
    else:
        print(f"{car} refueled with {f} liters")
    cars[car]['fuel'] = car_fuel
    return cars


def revert(cars, car, km):
    cars[car]['mileage'] -= km
    if cars[car]['mileage'] < 10000:
        cars[car]['mileage'] = 10000
    else:
        print(f"{car} mileage decreased by {km} kilometers")
    return cars


n_cars = int(input())

cars = {}

for n in range(n_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()

while not command == "Stop":
    action = command.split(" : ")[0]

    if action == "Drive":
        car, distance, given_fuel = command.split(" : ")[1:]
        distance = int(distance)
        given_fuel = int(given_fuel)
        cars = drive(cars, car, distance, given_fuel)

    elif action == "Refuel":
        car, given_fuel = command.split(" : ")[1:]
        given_fuel = int(given_fuel)
        cars = refuel(cars, car, given_fuel)

    elif action == "Revert":
        car, kms = command.split(" : ")[1:]
        kms = int(kms)
        cars = revert(cars, car, kms)

    command = input()

cars = dict(sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0])))

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
