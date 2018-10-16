import heapq

maxHeight = 0
class Map:
    def __init__(self,width, height):
        self.width = width  # N
        self.height = height  # N
        self.obstacles = []  # 1
    def is_valid(self, point):
        (x,y) = point
        return 0 <= x < self.width and 0 <= y < self.height

    def is_not_wall(self, point):
        return point not in self.obstacles

    def get_neighbors(self, point):
        (x,y) = point
        route = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                 (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y)]

        direction = filter(self.is_valid, route)
        direction = filter(self.is_not_wall, route)
        return direction

class MapWithWeight(Map):
    def __init__(self, width, height):
        super().__init__(width,height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1- y2)

def a_star_search(map, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        path = {}
        cost = {}
        path[start] = None
        cost[start] = 0
        while not frontier.empty():
            currentNode = frontier.get()

            if currentNode == goal:
                break
            nei = map.get_neighbors(currentNode)
            for next in nei:
                if 0 <= next[0] < maxHeight and 0 <= next[1] < maxHeight:
                    new_cost = cost[currentNode] + map.cost(currentNode, next)

                    if next not in cost or new_cost < cost[next]:
                        cost[next] = new_cost
                        priority = new_cost + heuristic(goal, next)
                        frontier.put(next, priority)
                        path[next] = currentNode
        return path, cost
def reconstruct_path(came_from, start, goal,map):
    #previous = goal
    current = goal
    path = []
    # path.append(goal)
    while current != start:
        # if 0 <= current[0] < maxHeight and 0 <= current[1] < maxHeight:
        #     direct = []
        #     direct = map.get_neighbors(previous)
            if current not in came_from:
                 return None
            # if current in direct:
            path.append(current)
            current = came_from[current]

    path.append(start) # optional
    path.reverse() # optional
    return path

def process(n,map,path,cost,start,goal):
    obtacles = [(i, j) for i in range(n) for j in range(n) if map[i][j] == 1]

    infomation = MapWithWeight(n,n)
    infomation.obstacles = obtacles

    path, cost = a_star_search(infomation,start, goal)
    path2 = reconstruct_path(path,start, goal, infomation)
    return path2, infomation.obstacles
    #print(cost)

def write_file(fo,n,start,goal,path2,obtacles):
    with open(fo, "w+") as out:
        result = [['-' for x in range(n)] for y in range(n)]

        if path2 == None:
            out.write("0")
            out.write("\nNo path for Start:({0}, {1}) and Goal:({2}, {3})".format(start[0],start[1], goal[0], goal[1]))

        else:
            out.write("%d\n" % len(path2))
            for item in path2:
                out.write("({0} {1})".format(item[0], item[1]))
                out.write(" ")
            for item2 in path2:
                if not (item2 == start or item2 == goal):
                    result[item2[0]][item2[1]] = 'x'
        out.write("\n")

        # print result
        for item in obtacles:
            result[item[0]][item[1]] = 'o'
        result[start[0]][start[1]] = 'S'
        result[goal[0]][goal[1]] = 'G'


        for i in result:
            for s in i:
                out.write(*s)
                out.write(" ")
            out.write("\n")
