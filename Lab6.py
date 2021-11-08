# Member: Lingling Wang, Ruixin Li, Xiaohan Zhao
# Program 6

def findCheapestPrice(n, flights, src, dst, k):
    if k == 0: #deals with k = 0 and check the src and dst
        for o in range(0,n):
            if int(flights[o][0]) == src and int(flights[o][1]) == dst:
                print(flights[o][2])
                
    elif k == 1: #deals with k = 1 and check the src and dst
        for o in range(0,n):
            for p in range(0, n):
                if int(flights[o][0]) == src and int(flights[o][1]) != dst:
                    if int(flights[p][0]) != src and int(flights[p][1]) == dst:
                        print(int(flights[o][2]) + int(flights[p][2]))

def fcp(n, flights, src, dst, k): #deals with k > 1 and check the src and dst
    integer = 0
    for o in range(0,n):
        for p in range(0,n):
            if int(flights[o][0]) == src and int(flights[o][1]) != dst and int(flights[p][0]) != src and int(flights[p][1]) == dst:
                for q in range(0,n):
                    if int(flights[q][0]) != src and int(flights[q][1]) != dst:
                        a = int(flights[q][2])
                        integer = integer + a
                print(int(flights[o][2]) + int(flights[p][2]) + integer)
                           
if __name__ == "__main__":
    try:
        n = int(input("n: "))
        if n <= 1 or n > 100:
            print("Error! Wrong N Number! ")
        elif 1 < n <= 100:
            flights = []
            for i in range(0, n):
                flight = input("Flights(srs, dst, p): ").split(",")
                flights.append(flight)
            print(flights)
            src = int(input("src: "))
            dst = int(input("dst: "))
            k = int(input("k: "))
            if k == 0 or k == 1:
                findCheapestPrice(n, flights, src, dst, k)
            elif 1 < k < n-1:
                fcp(n, flights, src, dst, k)
            else:
                print("Error! Wrong K Number! ")
    except ValueError:
        print("Error! Try Again!")
        pass
