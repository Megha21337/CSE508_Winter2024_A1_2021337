import os
def user_input(N):
  for i in range(1,N+1):
    query=input()
    filename=f"input{i}.txt"
    with open(filename,'w') as file:
      file.write(query+'\n')

N=int(input())
os.chdir("Part3_user_input")
user_input(N)