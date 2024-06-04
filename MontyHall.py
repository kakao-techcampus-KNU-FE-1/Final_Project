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
  
def other_one(x, arr):
  if x == arr[0]:
    return arr[1]
  elif x == arr[1]:
    return arr[0]
  else:
    return 'Input Not Valid'


def monty_hall():
  # car, goat1, goat2 중에서 무작위로 하나의 요소 선택 (인자로 리스트만 줬음 = 디폴트로 1개만 추출)
  original = np.random.choice(doors)

  # 선택한 문이 염소라면
  if is_goat(original):
    # [염소, 나머지 염소, 자동차]
    return [original, other_one(original, goats),'Car']

  else:
    # goat1, goat2 중에서 무작위로 하나의 염소 선택
    throw_out = np.random.choice(goats)
  return [original, throw_out, other_one(throw_out, goats)]

# 만번의 시뮬레이션
N = 10000

# 참가자의 처음 선택한 문, 호스트가 열어야 하는 문, 남는 문
original = []
throw_out = []
remains = []

for i in np.arange(N):
  result = monty_hall() # 매번 게임 실행

  # 각 게임 결과를 알맞은 배열에 추가
  original = np.append(original, result[0])
  throw_out = np.append(throw_out, result[1])
  remains = np.append(remains, result[2])

df = pd.DataFrame({
    '<Original Door Choice>': original,
    '<Monty Throws Out>': throw_out,
    '<Remaining Door>': remains
})
print(df)

