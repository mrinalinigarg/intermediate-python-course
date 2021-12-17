import random

def main():
  dice_rolls=2
  sum=0
  for i in range(0, dice_rolls):
    roll=random.randint(1,6)
    if(roll==1):
      print(f'You rolled a {roll}! Critical failure')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
    
    sum+=roll


  print(f'You have rolled a total of {sum}')

if __name__== "__main__":
  main()