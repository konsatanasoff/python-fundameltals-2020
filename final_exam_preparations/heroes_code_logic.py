def cast_spell(heroes, hero, mp_needed, spell):
    hero = hero.strip()
    spell = spell.strip()
    if heroes[hero][1] >= mp_needed:
        heroes[hero][1] -= mp_needed
        print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")
    return heroes


def take_damage(heroes, hero, damage, attacker):
    hero = hero.strip()
    attacker = attacker.strip()
    heroes[hero][0] -= damage
    if heroes[hero][0] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]
    return heroes


def recharge(heroes, hero, amount):
    hero = hero.strip()
    heroes[hero][1] += amount
    recharged = MAX_MP - (heroes[hero][1] - amount)
    if heroes[hero][1] >= MAX_MP:
        heroes[hero][1] = MAX_MP
        print(f"{hero} recharged for {recharged} MP!")
    else:
        print(f"{hero} recharged for {amount} MP!")
    return heroes


def heal(heroes, hero, amount):
    hero = hero.strip()
    heroes[hero][0] += amount
    healed = MAX_HP - (heroes[hero][0] - amount)
    if heroes[hero][0] > MAX_HP:
        heroes[hero][0] = MAX_HP
        print(f"{hero} healed for {healed} HP!")
    else:
        print(f"{hero} healed for {amount} HP!")
    return heroes


n_lines = int(input())

hero_stats = {}
MAX_HP = 100
MAX_MP = 200

for _ in range(n_lines):
    hero, hit_points, mana = input().split()
    hero_stats[hero] = [int(hit_points), int(mana)]

command = input()

while not command == "End":
    action = command.split()[0]

    if action == "CastSpell":
        hero_name, mana_points, spell_name = command.split("-")[1:]
        mana_points = int(mana_points)
        hero_stats = cast_spell(hero_stats, hero_name, mana_points, spell_name)

    elif action == "TakeDamage":
        hero_name, damage, attacker = command.split("-")[1:]
        damage = int(damage)
        hero_stats = take_damage(hero_stats, hero_name, damage, attacker)

    elif action == "Recharge":
        hero_name, amount = command.split("-")[1:]
        amount = int(amount)
        hero_stats = recharge(hero_stats, hero_name, amount)
    elif action == "Heal":
        hero_name, amount = command.split("-")[1:]
        amount = int(amount)
        hero_stats = heal(hero_stats, hero_name, amount)

    command = input()

hero_stats = dict(sorted(hero_stats.items(), key=lambda x: (-x[1][0], x)))

for hero in hero_stats:
    print(hero)
    print(f"  HP: {hero_stats[hero][0]}")
    print(f"  MP: {hero_stats[hero][1]}")