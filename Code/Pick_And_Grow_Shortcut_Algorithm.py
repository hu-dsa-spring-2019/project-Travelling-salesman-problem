import math
import time

def list_representation_route(mid_index):
    global route, n, complexity
    complexity = complexity + 2*(n-4)
    trace_ref = [mid_index]
    while type(route[trace_ref[-1]][1]) is dict:
        trace_ref.append(route[trace_ref[-1]][1]['sub_path_ref'])
    min_route = route[trace_ref[-1]][1]
    trace_ref.pop()
    while trace_ref != []:
        connection = route[trace_ref[-1]][1]['connection']
        if connection[0] == 'append':
            min_route.append(connection[1])
        else:
            min_route = [connection[1]] + min_route
        trace_ref.pop(-1)
    return min_route

def element_routes(cities):
    global distance, complexity
    ans = dict()
    k = cities['start']
    i = cities[k]
    while i != 'finish':
        cities[k] = cities[i]
        l = 'start'
        j = cities[l]
        while j != cities[i]:
            cities[l] = cities[j]
            q = cities['start']
            while q != 'finish':
                complexity = complexity + 1
                ans[(pair(i,j),q)] = [distance[pair(i,q)]+distance[pair(j,q)], [i,q,j], -1]
                q = cities[q]
            cities[l] = j
            l = j
            j = cities[l]
        cities[k] = i
        k = i
        i = cities[k]
    return ans

def circular_route_tsp(cities):
    start = time.time()
    global distance, n, route, complexity
    min_len=-1
    min_route=[]
    mid = cities.copy()
    ref_city = cities['start']
    cities['start'] = cities[cities['start']]
    k = cities['start']
    i = cities[k]
    mid_index = -1
    while i != 'finish':
        cities[k] = cities[i]
        l = 'start'
        j = cities[l]
        while j != cities[i]:
            cities[l] = cities[j]
            iroute = one_way_tsp(j, i, cities)
            iroute[0] = iroute[0] + distance[pair(ref_city, i)] + distance[pair(ref_city, j)]
            if iroute[0] < min_len or min_len == -1:
                min_len = iroute[0]
                min_route = iroute[1]
                mid_index = iroute[2]
            cities[l] = j
            l = j
            j = cities[l]
        cities[k] = i
        k = i
        i = cities[k]
    print('time taken:',time.time()-start)
    min_route = [ref_city]+list_representation_route(mid_index)
    return [min_len, min_route]            

def one_way_tsp(start, end, cities, ipath = -1):
    global distance, route, complexity, len3_routes
    if cities[cities['start']]=='finish':
        complexity = complexity + 1
        return len3_routes[(pair(start,end), cities['start'])]
    if ipath == -1:
        ipath = path_index(start, end, cities)
    if ipath in route.keys(): # has complexity O(1)
        complexity = complexity + 1
        return [route[ipath][0], route[ipath][1], ipath]
    min_len = -1
    p=0
    i='start'
    while cities[i]!='finish':
        p=p+1
        i = cities[i]
    i = cities['start']
    j = 'start'
    while i != 'finish':
        cities[j] = cities[i]
        index = path_index(start, i, cities)
        if index in route.keys():
            complexity = complexity + 1
            ilen = route[index][0] + distance[pair(i, end)]
            if ilen < min_len or min_len == -1:
                min_len = ilen
                if p == 2:
                    if route[index][1][0] == start:
                        min_route = route[index][1].copy()
                        min_route.append(end)
                    else:
                        min_route=[end] + route[index][1]
                elif p == 3:
                    if route[index][1][0] == start:
                        min_route = {'sub_path_ref':index,'connection':('append',end),'start':start,'end':end}
                    else:
                        min_route = {'sub_path_ref':index,'connection':('header',end),'start':end,'end':start}
                else:
                    if route[index][1]['start'] == start:
                        min_route = {'sub_path_ref':index,'connection':('append',end),'start':start,'end':end}
                    else:
                        min_route = {'sub_path_ref':index,'connection':('header',end),'start':end,'end':start}
        else:
            recursive_call = one_way_tsp(start, i, cities, index)
            ilen = recursive_call[0] + distance[pair(i, end)]
            if ilen < min_len or min_len == -1:
                min_len = ilen
                if p == 2:
                    if recursive_call[1][0] == start:
                        min_route = recursive_call[1].copy()
                        min_route.append(end)
                    else:
                        min_route = [end] + recursive_call[1]
                elif p == 3:
                    if recursive_call[1][0] == start:
                        min_route = {'sub_path_ref':index,'connection':('append',end),'start':start,'end':end}
                    else:
                        min_route = {'sub_path_ref':index,'connection':('header',end),'start':end,'end':start}
                else:
                    if recursive_call[1]['start'] == start:
                        min_route = {'sub_path_ref':index,'connection':('append',end),'start':start,'end':end}
                    else:
                        min_route = {'sub_path_ref':index,'connection':('header',end),'start':end,'end':start}
        cities[j] = i
        j = i
        i = cities[i]
    route[ipath] = [min_len, min_route]
    return [min_len, min_route, ipath]

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
    m_complexity = 0
    iset = (n-3)*(n-2) # no of len 3 min routes
    for i in range(3, n):
        iset = iset // (i-1) * (n-i-1) # no of i+1 len min routes
        m_complexity = m_complexity + iset
        t_complexity = t_complexity + iset*(i-1)
    m_complexity = m_complexity + 1
    t_complexity = t_complexity + (n-2)
    print('for n =', n,
          ' Memory complexity:', m_complexity, # (n-2)*2**(n-3) - (n-3)*(n-1)
          ' Time complexity:', t_complexity )   # (O(n^2.2^n), O(n^3.2^n))                     (n-2){(n-3)*2**(n-4)-(n-4)}
    
points = eval(input())
'''
Nodes     Time in sec
13        0.95
14        2.39
15        5.95
16        15.8
17        33.4
18        82.2
19        205.4
20        448.9
'''
distance, n, route, complexity, check = all_dis(points), len(points), dict(), 0, set()
nodes = {'start':1,len(points):'finish'}
for i in range(1,len(points)):
    nodes[i] = i+1
len3_routes = element_routes(nodes)
print(circular_route_tsp(nodes))
print('space complexity:',len(route.keys()))
print('time complexity:',complexity)

def path_index(start,end,cities):
    global n, complexity
    if len(cities) < 2:
        return -1
    #complexity = complexity + len(cities) - 2
    cities.sort()
    node = [start,end,cities[0],cities[1]]
    node.sort()
    if start > end:
        start, end = end, start
    count=0
    j = 0
    flag_j = False
    for i in cities[2:]:
        if flag_j:
            while i > node[j]:
                j = j + 1
            flag_j = j != 4
        count = count + 2**(i-j-1)
            
        
    '''for i in cities[2:]:
        if i > node[3]:
            count = count + 2**(i-5)
        elif i > node[2]:
            count = count + 2**(i-4)
        elif i > node[1]:
            count = count + 2**(i-3)
        elif i > node[0]:   
            count = count + 2**(i-2)
        else:
            count = count + 2**(i-1)'''
    return (start-1+(end-1)*(end-2)//2,cities[0]-1+(cities[1]-1)*(cities[1]-2)//2,count)
