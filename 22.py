from functools import cache

def solve(part1: bool):
    min_spell_cost = 53

    @cache
    def play(player_hp: int, armor: int, mana: int, spent_mana: int, shield: int, poison: int, recharge: int, boss_hp: int, player_move: bool):
        if not part1:
            player_hp -= 1

        if player_hp <= 0:
            return 1e10

        # apply active effects
        if shield == 6:
            armor += 7
        elif shield == 1:
            armor -= 7

        if shield > 0:
            shield -= 1

        if poison > 0:
            boss_hp -= 3
            poison -= 1

        if recharge > 0:
            mana += 101
            recharge -= 1

        if boss_hp <= 0:
            return spent_mana


        # boss move
        if not player_move:
            diff = 9 - armor
            return play(player_hp - diff, armor, mana, spent_mana, shield, poison, recharge, boss_hp, True)

        # player moves
        children = []
        if mana >= 53:
            # Magic Missile
            children.append((player_hp, armor, mana - 53, spent_mana + 53, shield, poison, recharge, boss_hp - 4, False))
        if mana >= 73:
            # Drain
            children.append((player_hp + 2, armor, mana - 73, spent_mana + 73, shield, poison, recharge, boss_hp - 2, False))
        if mana >= 113 and shield == 0:
            # Shield
            children.append((player_hp, armor, mana - 113, spent_mana + 113, 6, poison, recharge, boss_hp, False))
        if mana >= 173 and poison == 0:
            # Poison
            children.append((player_hp, armor, mana - 173, spent_mana + 173, shield, 6, recharge, boss_hp, False))
        if mana >= 229 and recharge == 0:
            # Recharge
            children.append((player_hp, armor, mana - 229, spent_mana + 229, shield, poison, 5, boss_hp, False))
        if not children:
            return 1e10
        return min(play(*c) for c in children)

    result = play(50, 0, 500, 0, 0, 0, 0, 58, True)
    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
