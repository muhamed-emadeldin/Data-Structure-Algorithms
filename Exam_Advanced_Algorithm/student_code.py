

'''
Here I will explain how I solve this problem:
1- I will create function called "heuristic" to calculate heuristic for each node and store in dict called "get_heuristic"

2- I will create a list called "openList" to store (node, fCost) as a tuple and soretd it to grap the minimum of value fCost

3- I will create a dict called g_score to calculate distance between curr and neghibour

4- I will create an empty dict called come_from to store the parent of each node
'''
import math
def shortest_path(M, start, goal):
  #-->basic variables
  get_heuristic   = {}
  openList        = [(start, 0)]
  g_score         = {node:math.inf for node in range(len(M.roads))}
  came_from       = {}

  g_score[start]  = 0

  #-->calculate heuristic for each node
  for i in range(len(M.roads)):
    get_heuristic[i] = heurisitc(M.intersections[i], M.intersections[goal])

  while len(openList) > 0:
    
    openList = sortList(openList)
    curr, fcost = openList.pop(0)

    #-->check curr == goal
    if curr == goal:
      return generatePath(came_from, curr)

    for neighbour in M.roads[curr]:

      #-->calculate distance between the current node and neighbour
      distance_curr_neighbour = g_score[curr] + heurisitc(M.intersections[curr], M.intersections[neighbour])
      
      if distance_curr_neighbour < g_score[neighbour]:
        came_from[neighbour]  = curr
        g_score[neighbour]    = distance_curr_neighbour
        f_negibour            = distance_curr_neighbour + get_heuristic[neighbour]

        openList.append((neighbour, f_negibour))

  return "We can't find the goal"


#-->implemention function calculate heuristic for each node
def heurisitc(curr, goal):
  return math.sqrt((curr[0] - goal[0]) ** 2 + (curr[1] - goal[1]) ** 2)

#-->implemention sort list
def sortList(arr):
  arr.sort(key=lambda tup: tup[1])
  return arr


#-->implementation genrate path
def generatePath(came_from, curr):
  path = [curr]
  while curr in came_from:
    curr = came_from[curr]
    path.append(curr)
  
  return path[::-1]


      