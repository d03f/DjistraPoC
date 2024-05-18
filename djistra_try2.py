from time import sleep

class Point():
    def __init__(self, name, x ,y):
        self.name = name
        self.x = x; self.y = y
        
        self.connections = []
        self.routeDist = None
        self.routePoints = []
        
        
    
    def addConnection(self, point, distancePoint):
        if [point, distancePoint] not in self.connections:
            self.connections.append([point, distancePoint])
            return True
        else:
            return False
            
    def updateRoute(self, routeDist, routePoints):


        if self.routeDist == None:
            self.routeDist = routeDist
            self.routePoints = routePoints
            return True
        
        else:
            if routeDist < self.routeDist:
                self.routeDist = routeDist
                self.routePoints = routePoints
                return True
            else:
                return False
        
    def nextPoints(self):
        updatedPoints = []
        
        routePointsUpdated = self.routePoints.copy()
        routePointsUpdated.append(self)
        
        for point, distance in self.connections:
            
            currentDist = self.routeDist
            
            if currentDist == None:
                currentDist = 0 
            
            if point.updateRoute(currentDist + distance, routePointsUpdated):
                updatedPoints.append(point)
            else:
                pass
        return updatedPoints
    
    
    def getRouteNames(self):
        routeList = []
        for point in self.routePoints:
            routeList.append(point.name)
        routeList.append(self.name)
        return routeList
                

a = Point("a", 0, 0)
b = Point("b", 10, 0)
c = Point("c", 15, 0)
d = Point("d", 15, 0)
e = Point("e", 15, 0)
f = Point("f", 15, 0)
g = Point("g", 15, 0)


a.addConnection(b, 8)
a.addConnection(c, 1)

b.addConnection(c, 4)
b.addConnection(f, 4)

c.addConnection(b, 5)
c.addConnection(d, 2)
c.addConnection(e, 5)

d.addConnection(b, 1)
d.addConnection(e, 2)

e.addConnection(f, 2)
e.addConnection(g, 5)

f.addConnection(g, 1)

posibleRoutes = []


def nextIteration(nextPoints):
    global posibleRoutes

    if len(nextPoints) == 0:
        return
    
    ###Visual###
    for point in nextPoints:

        print(point.name.upper() + ": ", end="")
        for i in point.routePoints:
            print(i.name, end="")
        
        print("\n")
    print("------------------------------")
    ############



    for i in nextPoints:            
        if i == g:
            print(f"ROUTE ENDED: {i.getRouteNames()} -> {i.routeDist}")
            print("------------------------------")
            posibleRoutes.append([i.routeDist, i.getRouteNames()])
            break
        nextIterationPoints = i.nextPoints()
        nextIteration(nextIterationPoints)
        
    
nextPoints = a.nextPoints()

nextIteration(nextPoints)

shortestRoute = posibleRoutes[0]

for distance, route in posibleRoutes:
    if distance <= shortestRoute[0]:
        shortestRoute = [distance, route]

print(f"\n\nShortest Route:\n    Route: {shortestRoute[1]}\n    Distance: {shortestRoute[0]}")