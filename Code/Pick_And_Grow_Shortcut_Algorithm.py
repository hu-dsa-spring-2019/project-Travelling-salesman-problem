import math

def circular_route_tsp(cities):
    global distance, n, route, complexity
    min_len=-1
    min_route=[]
    p=len(cities)
    complexity = complexity + (p-2)*(p-1)//2
    for i in range(2,len(cities)):
        for j in range(1,i):
            iroute = one_way_tsp(cities[j], cities[i], cities[1:j] + cities[j+1:i] + cities[i+1:])
            iroute[0] = iroute[0] + distance[pair(cities[0], cities[i])] + distance[pair(cities[0], cities[j])]
            iroute[1].append(cities[0])
            if iroute[0] < min_len or min_len == -1:
                min_len = iroute[0]
                min_route = iroute[1]
    return [min_len, min_route]
            

def one_way_tsp(start, end, cities, ipath = -1):
    global distance, route, complexity
    if len(cities) == 1:
        return [distance[pair(start, cities[0])] + distance[pair(cities[0], end)],
                [start, cities[0], end], -1]
    if ipath == -1:
        ipath = path_index(start, end, cities)
    if ipath in route.keys():
        return [route[ipath][0], route[ipath][1], ipath]
    min_len = -1
    complexity = complexity + len(cities)
    for i in range(len(cities)):
        index = path_index(start, cities[i], cities[:i] + cities[i+1:])
        if index in route.keys():
            ilen = route[index][0] + distance[pair(cities[i], end)]
            if ilen < min_len or min_len == -1:
                min_len = ilen
                if route[index][1][0] == start:
                    min_route = route[index][1].copy()
                    min_route.append(end)
                else:
                    min_route=[end] + route[index][1]
        else:
            recursive_call = one_way_tsp(start, cities[i], cities[:i] + cities[i+1:], index)
            ilen = recursive_call[0] + distance[pair(cities[i], end)]
            if ilen < min_len or min_len == -1:
                min_len = ilen
                if recursive_call[1][0] == start:
                    min_route = recursive_call[1].copy()
                    min_route.append(end)
                else:
                    min_route = [end] + recursive_call[1]
    route[ipath] = [min_len, min_route]
    '''if min_route[0] == start:
        for i in range(1,len(min_route)-4):
            for j in range(i+4,len(min_route)):
                route[path_index(min_route[i],min_route[j],min_route[i+1:j])] = [sum([distance[pair(min_route[k],min_route[k+1])] for k in range(len(min_route[i:j+1])-1)]), min_route[i:j+1]]
    else:
        for i in range(len(min_route)-5):
            for j in range(i+4,len(min_route)-1):
                route[path_index(min_route[i],min_route[j],min_route[i+1:j])] = [sum([distance[pair(min_route[k],min_route[k+1])] for k in range(len(min_route[i:j+1])-1)]), min_route[i:j+1]]
    '''
    return [min_len, min_route, ipath]

def get_shortcuts(cities):
    global distance, n, route, complexity
    min_len=-1
    min_route=[]
    p=len(cities)
    complexity = complexity + p*(p-1)*(p-2)//2
    for i in range(1,len(cities)):
        for j in range(i):
            end = cities[i]
            start = cities[j]
            mid_cities =  [k for k in cities if k != end and k != start]
            if start in mid_cities or end in mid_cities:
                print(mid_cities,cities,end,start,i,j)
            iroute = one_way_tsp(start, end, mid_cities,-1)
            min_len = iroute[0]
            min_route = iroute[1]
            mid_cities = min_route[1:len(min_route)-1]
            ipath = iroute[2]
            if end == min_route[0]:
                for a in range(len(cities)-5):
                    for b in range(a+4,len(cities)-1):
                        index = path_index(min_route[a], min_route[b], min_route[a+1:b])
                        if index not in route.keys():
                            route[index] = [0,0]
                            route[index][1] = min_route[a:b+1]
                            route[index][0] = sum([distance[pair(route[index][1][p],route[index][1][p+1])] for p in range(len(route[index][1])-1)])#route[ipath][0] - route[path_index(start,min_route[b], min_route[b+1:len(min_route)-1])][0]
            else:
                for b in range(len(cities)-1,4,-1):
                    for a in range(1,b-3):
                        index = path_index(min_route[a], min_route[b], min_route[a+1:b])
                        if index not in route.keys():
                            route[index] = [0,0]
                            route[index][1] = min_route[a:b+1]
                            route[index][0] = sum([distance[pair(route[index][1][p],route[index][1][p+1])] for p in range(len(route[index][1])-1)])#route[ipath][0] - route[path_index(start,min_route[b], min_route[b+1:len(min_route)-1])][0]
    return len(route.keys())

def path_index(start,end,cities):
    global n, complexity
    if len(cities) < 2:
        return -1
    #complexity = complexity + len(cities)
    cities.sort()
    node = [start,end,cities[0],cities[1]]
    node.sort()
    if start > end:
        start, end = end, start
    count=0
    for i in cities[2:]:
        if i > node[3]:
            count = count + 2**(i-5)
        elif i > node[2]:
            count = count + 2**(i-4)
        elif i > node[1]:
            count = count + 2**(i-3)
        elif i > node[0]:   
            count = count + 2**(i-2)
        else:
            count = count + 2**(i-1)
    return (start-1+(end-1)*(end-2)//2,cities[0]-1+(cities[1]-1)*(cities[1]-2)//2,count)

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
    complexity = 2 * (n-2) * (n-3) * (n-4) // 6
    iset = complexity
    for i in range(4, n-1):# i len sets are counted
        iset = (n-i-1) * iset // fac(i-1)
        complexity = complexity + iset#(i-1) * fac(n-2) // (fac(i-2) * fac(n-i-2))
    complexity = complexity + 2 * n - 4
    print('for n =', n, 'Overall complexity:', complexity,
          '\nComplexity of main One_way func:', (n-2)*(n-3)*2**(n-4)+n-2 )

points = eval(input())# [(200, 296), (281, 309), (296, 356), (322, 343), (392, 403), (409, 293), (435, 245), (435, 172)]#, (418, 108), (354, 198), (346, 149), (275, 85), (239, 5), (198, 109), (236, 126), (236, 155), (234, 173), (213, 215), (188, 228), (180, 199), (180, 179), (151, 91), (125, 41), (61, 90), (11, 55), (20, 83), (11, 210), (83, 246), (90, 333), (112, 356), (79, 368), (35, 362), (95, 401), (217, 399), (228, 368)]#[(418, 108), (354, 198), (346, 149), (275, 85), (239, 5), (198, 109), (236, 126)]

distance, n, route, complexity = all_dis(points), len(points), {}, 0

#print(get_shortcuts(list(range(1, 1+len(points)))),'shortcuts computed')
#print(one_way_tsp(1,len(points),[i for i in range(2,len(points))]))
print(circular_route_tsp(list(range(1, 1+len(points)))))
print('memory complexity:',len(route.keys()))
print('time complexity:',complexity)
#complexity_function(7)
