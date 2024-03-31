def game(terra, power):
    for sublist in terra:
        for energy_value in sublist:
            if energy_value <= power:
                power = power + energy_value
            else:
                break
    return power

total_energy = game([[1,2,5], [2,3,10]], 3)
print(total_energy)

    