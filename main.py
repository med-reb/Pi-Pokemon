# Emulate Game Boy to play Pokémon as a Pi (3.14) player

# look for a 1 billion pi online
from pyboy import PyBoy
from mpmath import mp
import time

# load rom
pyboy = PyBoy('rom.gbc')
pyboy.set_emulation_speed(0)

# Générateur infini de chiffres de Pi
mp.dps = 100000
pi_gen = (digit for digit in str(mp.pi)[2:])
controls = ["a","b","up","down","right","left","start","select"]

iteration_count = 0

while pyboy.tick():
    #print(iteration_count)
    pokemon_level_address = 0xDA22  # Address of pokemon's level
    pokemon_level = pyboy.memory[pokemon_level_address]  # read value

    # Si le Pokémon atteint le niveau 5, on arrête
    if pokemon_level >= 5:
        print("You've Got a pokemon !")
        break

    # Each digit is assign to a control
    if ((iteration_count%2) >= 0):
        digit = next(pi_gen)    
        pyboy.button(controls[int(digit)%7])

    iteration_count += 1
