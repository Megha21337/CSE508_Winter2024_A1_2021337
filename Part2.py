import os
def user_input(N):
  for i in range(1,N+1):
    query=input()
    operations=input()

    filename=f"input{i}.txt"
    with open(filename,'w') as file:
      file.write(query+'\n')
      file.write(operations)

N=int(input())
os.chdir("Part2_user_input")
user_input(N)