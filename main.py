import sys
import AStar as algorithm
import ReadFile as input

if __name__ == '__main__':
    N, S, G, A = input.ReadFile(sys.argv[1])
    algorithm.maxHeight = N
    # map = algorithm.MapWithWeight(N,N)
    path = {}
    cost = {}
    obtacles = []
    result, obtacles = algorithm.process(N, A, path, cost, S, G)
    # print(obtacles)
    algorithm.write_file(sys.argv[2], N, S, G, result, obtacles)
