import random

def main():
  dice_rolls=2
  sum=0
  for i in range(0, dice_rolls):
    roll=random.randint(1,6)
    print(f'You rolled a {roll}')
    sum+=roll
  print(f'You have rolled a total of {sum}')

if __name__== "__main__":
  main()