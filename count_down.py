
def my_count_down():
  for x in range(5, 0, -1):
    print(x)
    print("final countdown!")
  print('Done!')

def whiloop():
  x=0
  while x != 5:
    x=x+1
    print (x)
    print ('up a number!')
  print ('done!')

if __name__ == "__main__":
  my_count_down()