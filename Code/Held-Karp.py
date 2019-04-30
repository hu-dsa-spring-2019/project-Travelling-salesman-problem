import math
import time
# 4/25/2019
# Python 3.7.0 TSP algorithm O(n^2.2^n) by Shams Arfeen
# Note: there is no worst case or best case as the num of iterations is fixed for n

def TSP():  #  (n-1)^2.2^(n-2)+3*(n-1)
    ti = time.time()
    global distances, n, complexity
    unvisited = {0:2,n:0}
    for route_stops in range(2,n):
        unvisited[route_stops] = route_stops+1
    route_list = [0, {(1,0): [0,0,unvisited]} ]
    for route_stops in range(2,n+1):
        route_list.append(dict())
        shortest_path = dict()
        for path_index, path_inf in route_list[route_stops-1].items():
            current_node = 0
            unvisited = path_inf[2]
            while unvisited[current_node] != 0:
                complexity = complexity + 1
                pre_node = current_node
                current_node = unvisited[current_node]
                
                n_index = path_index[1]+2**(current_node-2)
                new_path_index = (current_node, n_index)
                if (current_node, n_index) not in route_list[route_stops].keys():
                    new_path_inf = [float('inf'),0,0]
                else:
                    new_path_inf = route_list[route_stops][(current_node, n_index)]
                n_len=path_inf[0]+distance[pair(current_node,path_index[0])]
                if n_len < new_path_inf[0]:
                    to_be_visited = {current_node:n_index}
                    shortest_path[(current_node, n_index)] = [pre_node, current_node, unvisited, to_be_visited]
                    route_list[route_stops][(current_node, n_index)] = [n_len, path_index, to_be_visited]
        for path_inf in shortest_path.values():
            complexity = complexity + len(to_be_visited.keys()) - 1
            pre_node = path_inf[0]
            current_node = path_inf[1]
            unvisited = path_inf[2]
            to_be_visited = path_inf[3]
            node=0
            while node != pre_node:
                to_be_visited[node] = unvisited[node]
                node = unvisited[node]
            node = unvisited[current_node]
            to_be_visited[pre_node] = node
            while node != 0:
                to_be_visited[node] = unvisited[node]
                node = unvisited[node]
        del shortest_path
    min_dis = -1
    sub_path = -1
    for path_index, path_inf in  route_list[n].items():
        complexity += 1
        route_dis = path_inf[0] + distance[pair(1,path_index[0])]
        if route_dis < min_dis or min_dis == -1:
            min_dis = route_dis
            sub_path = path_index
            min_route = [path_index[0]]
    for route_stops in range(n,1,-1):
        complexity += 1
        sub_path = route_list[route_stops][sub_path][1]
        min_route.append(sub_path[0])
    print(time.time()-ti)
    return [min_dis,min_route]
            
def all_dis(lst, s_matrix = False):
    ans=[]
    global matrix
    if s_matrix:
        for i in range(1,len(lst)):
            for j in range(i):
                ans.append(matrix[i-1][j-1])
    else:
        for i in range(1,len(lst)):
            for j in range(i):
                ans.append(math.sqrt((lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2))
                matrix[i][j] = int(ans[-1])
                matrix[j][i] = int(ans[-1])
        #for i in matrix:
        #    print(i)
    return ans

def pair(a,b):
    if b>a:
        return (b-1)*(b-2)//2+a-1
    return (a-1)*(a-2)//2+b-1

def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

def complexity_function(n):
    t_complexity = 0
    s_complexity = 0
    no_of_i_len_routes = n-1
    for i in range(2, n):
        no_of_i_len_routes = no_of_i_len_routes * (n-i) // (i-1)
        s_complexity = s_complexity + no_of_i_len_routes
        t_complexity = t_complexity + no_of_i_len_routes*(n-1)
    s_complexity = s_complexity + 1
    t_complexity = t_complexity + (n-1)**2 + 3*(n-1)
    print('for n =', n,
          ' Space complexity:', s_complexity,
          ' Time complexity:', t_complexity )
    
points = eval(input())

#n=16
'''[( 79,  113), ( 223,  116), ( 78,  257), ( 272,  217), ( 202,  315), ( 407,  256), ( 376,  165), ( 324,  298), ( 111,  237), ( 199,  173), ( 191,  237), ( 305,  148), ( 339,  218), ( 254,  282), ( 227,  211), ( 123,  173)]
9.320480346679688
[1183.9768229174088, [16, 3, 9, 11, 5, 14, 8, 6, 13, 7, 12, 4, 15, 10, 2, 1]]
time complexity: 3686415'''
#n=17
'''[( 79,  185), ( 156,  145), ( 269,  210), ( 327,  130), ( 219,  169), ( 173,  285), ( 263,  274), ( 175,  217), ( 222,  238), ( 312,  174), ( 374,  222), ( 325,  229), ( 347,  275), ( 385,  159), ( 265,  141), ( 132,  197), ( 109,  251)]
20.915740251541138
[1018.5206767905456, [16, 2, 5, 15, 10, 4, 14, 11, 13, 12, 3, 7, 9, 8, 6, 17, 1]]
time complexity: 8388624'''
#n=18
'''[( 148,  192), ( 198,  150), ( 351,  179), ( 313,  279), ( 153,  286), ( 65,  250), ( 310,  212), ( 197,  217), ( 304,  120), ( 277,  253), ( 440,  222), ( 376,  328), ( 354,  241), ( 239,  177), ( 208,  313), ( 258,  310), ( 207,  252), ( 265,  209)]
47.77088499069214
[1248.7520712918385, [8, 17, 18, 14, 2, 9, 3, 7, 13, 11, 12, 4, 10, 16, 15, 5, 6, 1]]
time complexity: 18939921'''
#n=19
'''[( 58,  176), ( 148,  139), ( 219,  205), ( 325,  102), ( 391,  161), ( 266,  180), ( 253,  134), ( 141,  192), ( 70,  278), ( 140,  284), ( 120,  243), ( 239,  264), ( 300,  220), ( 359,  240), ( 329,  167), ( 350,  201), ( 256,  226), ( 180,  224), ( 197,  180)]
110.2577760219574
[1140.806594260569, [9, 11, 10, 18, 12, 17, 13, 14, 16, 5, 15, 4, 7, 6, 3, 19, 2, 8, 1]]
time complexity: 42467346'''
matrix = [[0 for i in range(len(points))] for i in range(len(points))]
distance, n, route, complexity, check = all_dis(points), len(points), dict(), 0, set()

print(TSP())

print('time complexity:',complexity)
complexity_function(len(points))
