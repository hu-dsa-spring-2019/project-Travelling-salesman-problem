import math
import time


def TSP():  #  (n-1)^2.2^(n-2)+3*(n-1)
    ti = time.time()
    global distances, n, complexity
    unvisited = {0:2,n:0}
    for i in range(2,n):
        unvisited[i] = i+1
    route_list = [0, {(1,0): [0,0,unvisited]} ]
    for i in range(2,n+1):
        route_list.append(dict())
        dic_data = dict()
        for key, val in route_list[i-1].items():
            j = 0
            to_be_visited = val[2]
            while to_be_visited[j] != 0:
                complexity = complexity + 1
                pre_j = j
                j = to_be_visited[j]
                
                n_index = key[1]+2**(j-2)
                key2 = (j, n_index)
                if (j, n_index) not in route_list[i].keys():
                    val2 = [float('inf'),0,0]
                else:
                    val2 = route_list[i][(j, n_index)]
                n_len=val[0]+distance[pair(j,key[0])]
                if n_len < val2[0]:
                    unattendees = {j:n_index}
                    dic_data[(j, n_index)] = [pre_j, j, to_be_visited, unattendees]
                    route_list[i][(j, n_index)] = [n_len, key, unattendees]
        for dic_work in dic_data.values():
            pre_j = dic_work[0]
            j = dic_work[1]
            to_be_visited = dic_work[2]
            unattendees = dic_work[3]
            k=0
            while k != pre_j:
                unattendees[k] = to_be_visited[k]
                k = to_be_visited[k]
            k = to_be_visited[j]
            unattendees[pre_j] = k
            while k != 0:
                unattendees[k] = to_be_visited[k]
                k = to_be_visited[k]
            complexity = complexity + len(unattendees.keys()) - 1
        del dic_data
    min_dis = -1
    min_route = -1
    for key, val in  route_list[n].items():
        complexity += 1
        route_dis = val[0] + distance[pair(1,key[0])]
        if route_dis < min_dis or min_dis == -1:
            min_dis = route_dis
            min_route = key
            my_route = [key[0]]
    for i in range(n,1,-1):
        complexity += 1
        min_route = route_list[i][min_route][1]
        my_route.append(min_route[0])
    print(time.time()-ti)
    return [min_dis,my_route]
            
def all_dis(lst):
    ans=[]
    for i in range(1,len(lst)):
        for j in range(i):
            ans.append(math.sqrt((lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2))
    return ans

def pair(a,b):
    if b>a:
        return (b-1)*(b-2)//2+a-1
    return (a-1)*(a-2)//2+b-1

def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

def complexity_function(n): # Note: there is no worst case or best case as the num of iterations is fixed for n
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
          ' Space complexity:', m_complexity,
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
#n=20

distance, n, route, complexity, check = all_dis(points), len(points), dict(), 0, set()

print(TSP())

print('time complexity:',complexity)
complexity_function(len(points))
