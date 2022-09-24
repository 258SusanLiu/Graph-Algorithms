

def minEffort(puzzle):

  m=len(puzzle)
  n=len(puzzle[0])
  
  path=[[1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]]

  def depthFirstSearch(distLimit, i, j):
    route.add((i, j)) 
    for dx, dy in path:
      
      if 0 <= dy+j < n and 0 <= dx+i < m and (dx+i, dy+j) not in route:
        result=abs(puzzle[dx+i][dy+j]-puzzle[i][j])
        
        if result <= distLimit:
          depthFirstSearch(distLimit, dx+i, dy+j)
  
  
  total_effort=max(max(puzzle, key=max))
  effort=-1
  
  while(total_effort > effort+1):
  
      between = (effort+total_effort)//2
      route = set()
      
      
      depthFirstSearch(between,0,0)
  
      if (m-1, n-1) in route:
          total_effort = between
      else:
          effort = between
          
  return total_effort
  


    
if __name__ == '__main__':
  puzzle=[[1, 3, 5],
          [2, 8, 3],
          [3, 4, 5]] 
  print("The min effort is: ", minEffort(puzzle))