import math
import time


def TSP():  #  (n-1)^2.2^(n-2)+3*(n-1)
    ti = time.time()
    global distances, n, complexity
    unvisited = list(range(2,n+1))
    route_list = [0, {(1,0): [0,0,unvisited]} ]
    for i in range(2,(n+3)//2+1):
        route_list.append(dict())
        dic_data = dict()
        for key, val in route_list[i-1].items():
            to_be_visited = val[2]
            for j in to_be_visited:
                complexity = complexity + 1
                n_index = key[1]+2**(j-2)
                key2 = (j, n_index)
                if key2 not in route_list[i].keys():
                    val2 = [float('inf'),0,0]
                else:
                    val2 = route_list[i][(j, n_index)]
                n_len=val[0]+distance[pair(j,key[0])]
                if n_len < val2[0]:
                    unattendees = []
                    dic_data[key2] = [j, to_be_visited, unattendees]
                    route_list[i][key2] = [n_len, key, unattendees]
        for k, dic_work in dic_data.items():
            j = dic_work[0]
            to_be_visited = dic_work[1]
            unattendees = dic_work[2]
            for k in to_be_visited:
                if k !=j:
                    unattendees.append(k)
            complexity = complexity + len(to_be_visited)
        del dic_data
    min_dis = float('inf')
    min_route = -1
    if n%2==0:
        mykeys = list(route_list[i].keys())
        while len(mykeys)!=0:
            m = mykeys.pop()
            v = route_list[i][m]
            m2 = (m[0], 2**(n-1)-1-m[1]+2**(m[0]-2))
            v2 = route_list[i][m2]
            idis = v[0] + v2[0]
            if idis < min_dis:
                min_dis = idis
                min_route = {0:[m]+v,1:[m2]+v2}
        my_route = [min_route[0][0][0]]
        ilen = i
        a = min_route[0][0]
        while a[0] != 1:
            a = route_list[ilen][a][1]
            my_route.append(a[0])
            ilen = ilen - 1
        ilen = i
        a = min_route[1][0]
        while a[0] != 1:
            a = route_list[ilen][a][1]
            my_route = [a[0]] + my_route
            ilen = ilen - 1
    else:
        mykeys = list(route_list[i].keys())
        while len(mykeys)!=0:
            m = mykeys.pop()
            v = route_list[i][m]
            m2 = (m[0], 2**(n-1)-1-m[1]+2**(m[0]-2))
            v2 = route_list[i-1][m2]
            idis = v[0] + v2[0]
            if idis < min_dis:
                min_dis = idis
                min_route = {0:[m]+v,1:[m2]+v2}
        my_route = [min_route[0][0][0]]
        ilen = i
        a = min_route[0][0]
        while a[0] != 1:
            a = route_list[ilen][a][1]
            my_route.append(a[0])
            ilen = ilen - 1
        ilen = i-1
        a = min_route[1][0]
        while a[0] != 1:
            a = route_list[ilen][a][1]
            my_route = [a[0]] + my_route
            ilen = ilen - 1
    print('time taken:',time.time()-ti)
    return [min_dis, my_route]
            
def all_dis(lst):
    ans=[]
    for i in range(1,len(lst)):
        for j in range(i):
            ans.append(math.sqrt((lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2))
    return ans

def read_matrix():
    global g_matrix, distance
    for i in range(len(g_matrix)):
        for j in range(i):
            distance.append( matrix[i][j] )
            
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
    for i in range(2, (n+3)//2):
        no_of_i_len_routes = no_of_i_len_routes * (n-i) // (i-1)
        s_complexity = s_complexity + no_of_i_len_routes
        t_complexity = t_complexity + no_of_i_len_routes*(n-1)
    s_complexity = s_complexity + 1
    t_complexity = t_complexity + (n-1)**2 + (n-1)
    print('for n =', n,
          ' Space complexity:', s_complexity,
          ' Time complexity:', t_complexity )
    
points = eval(input())
# checks if there's an edge between the current node and the next node
# If there's an edge, adds the edge weight

#n=16
'''[( 79,  113), ( 223,  116), ( 78,  257), ( 272,  217), ( 202,  315), ( 407,  256), ( 376,  165), ( 324,  298), ( 111,  237), ( 199,  173), ( 191,  237), ( 305,  148), ( 339,  218), ( 254,  282), ( 227,  211), ( 123,  173)]
time taken: 4.851215362548828
[1183.9768229174088, [1, 2, 10, 15, 4, 12, 7, 13, 6, 8, 14, 5, 11, 9, 3, 16, 1]]
total iterations: 2229315'''
#n=17
'''[( 79,  185), ( 156,  145), ( 269,  210), ( 327,  130), ( 219,  169), ( 173,  285), ( 263,  274), ( 175,  217), ( 222,  238), ( 312,  174), ( 374,  222), ( 325,  229), ( 347,  275), ( 385,  159), ( 265,  141), ( 132,  197), ( 109,  251)]
time taken: 14.349323511123657
[1018.5206767905456, [1, 17, 6, 8, 9, 7, 3, 12, 6, 11, 14, 4, 10, 15, 5, 2, 16, 1]]
total iterations: 5841680'''
#n=18
'''[( 148,  192), ( 198,  150), ( 351,  179), ( 313,  279), ( 153,  286), ( 65,  250), ( 310,  212), ( 197,  217), ( 304,  120), ( 277,  253), ( 440,  222), ( 376,  328), ( 354,  241), ( 239,  177), ( 208,  313), ( 258,  310), ( 207,  252), ( 265,  209)]
time taken: 27.16943669319153
[1248.7520712918385, [1, 8, 17, 18, 14, 2, 9, 3, 7, 13, 11, 12, 4, 10, 16, 15, 5, 6, 1]]
total iterations: 11329684'''
#n=19
'''[( 58,  176), ( 148,  139), ( 219,  205), ( 325,  102), ( 391,  161), ( 266,  180), ( 253,  134), ( 141,  192), ( 70,  278), ( 140,  284), ( 120,  243), ( 239,  264), ( 300,  220), ( 359,  240), ( 329,  167), ( 350,  201), ( 256,  226), ( 180,  224), ( 197,  180)]
time taken: 72.76848983764648
[1140.806594260569, [1, 8, 2, 19, 3, 6, 7, 4, 15, 5, 16, 14, 13, 17, 12, 18, 10, 11, 9, 1]]
total iterations: 29110122'''

distance, n, route, complexity, check = all_dis(points), len(points), dict(), 0, set()

#g_matrix = # adjacency matrix

#read_matrix()
print(TSP())

print('total iterations:',complexity)
complexity_function(len(points))
