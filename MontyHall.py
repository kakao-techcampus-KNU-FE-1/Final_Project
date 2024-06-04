import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

doors = ['Car', 'Goat 1', 'Goat 2']
goats = ['Goat 1', 'Goat 2']

# 해당 문이 염소인지? => 참 / 거짓 반환
def is_goat(door_name):
  if door_name == "Goat 1":
    return True
  elif door_name == "Goat 2":
    return True
  else:
    return False

