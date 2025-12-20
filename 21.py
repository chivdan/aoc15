import copy

def simulate(player, boss):
    def attack(attacker, defender):
        diff = attacker["Damage"] - defender["Armor"]
        if diff <= 0:
            diff = 1
        defender["Hit Points"] -= diff

    i = 0
    while True:
        if player["Hit Points"] <= 0:
            return False
        if boss["Hit Points"] <= 0:
            return True
        if i % 2 == 0:
            attack(player, boss)
        else:
            attack(boss, player)
        i += 1
            
def solve(part1: bool):
    boss = {}
    for line in open("input.txt"):
        k, v = line.strip().split(": ")
        boss[k] = int(v)

    weapons = {8: {"Damage": 4},
               10: {"Damage": 5},
               25: {"Damage": 6},
               40: {"Damage": 7},
               74: {"Damage": 8}
               }

    armor = {0: {"Armor": 0},
             13: {"Armor": 1},
             31: {"Armor": 2},
             53: {"Armor": 3},
             75: {"Armor": 4},
             102: {"Armor": 5}
             }

    rings = {0: {"Damage": 0, "Armor": 0},
             25: {"Damage": 1, "Armor": 0},
             50: {"Damage": 2, "Armor": 0},
             100: {"Damage": 3, "Armor": 0},
             20: {"Damage": 0, "Armor": 1},
             40: {"Damage": 0, "Armor": 2},
             80: {"Damage": 0, "Armor": 3},
             }
    
    min_gold = 1e10
    max_gold = 0
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r1 == r2 and r1 != 0 and r2 != 0:
                        continue
                    player = {"Hit Points": 100, "Damage": 0, "Armor": 0}
                    gold = w
                    # weapon
                    player["Damage"] = weapons[w]["Damage"]
                    #armor
                    gold += a
                    player["Armor"] = armor[a]["Armor"]
                    gold += r1
                    player["Damage"] += rings[r1]["Damage"]
                    player["Armor"] += rings[r1]["Armor"]

                    gold += r2
                    player["Damage"] += rings[r2]["Damage"]
                    player["Armor"] += rings[r2]["Armor"]
                    b = copy.copy(boss)
                    won = simulate(player, b)
                    if part1 and won:
                        min_gold = min(min_gold, gold)
                    elif not part1 and not won:
                        max_gold = max(max_gold, gold)
    if part1:
        print(min_gold)
    else:
        print(max_gold)


if __name__ == '__main__':
    solve(True)
    solve(False)
