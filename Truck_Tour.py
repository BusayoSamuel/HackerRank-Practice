"""
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N-1) (both inclusive). You have 
two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that particular petrol pump will give, 
and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the 
first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. 
The truck will move one kilometer for each litre of the petrol.

Sample Input
1 5
10 3
3 4

Sample Output
1

Explanation
We can start the tour from the second petrol pump.
"""
def truckTour(petrolpumps):  #My Answer
    rows = len(petrolpumps)
    
    tank = 0    
    for row in range(rows):
        tank += petrolpumps[row][0]
        tank = tank - petrolpumps[row][1]
        
        if tank < 0:
            tank = 0
            continue
            
        for i in range(row+1, rows):
            tank += petrolpumps[i][0]
            tank = tank - petrolpumps[i][1]
            
            if tank < 0:
                break
                
        for i in range(0, row-1):
            if tank < 0:
                break

            tank += petrolpumps[i][0]
            tank = tank - petrolpumps[i][1]
            
            if tank < 0:
                break

        if tank < 0:
            tank = 0
            continue

        return row

#Alternatives
def truckTour2(p):
    fuel=0
    ll=len(p)
    l=0
    i=l
    while i<ll:
        fuel=fuel+p[i][0]-p[i][1]
        if fuel<0:
            l=l+1
            i=l
            fuel=0
        else:
            i+=1
    return l



