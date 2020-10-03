n = int(input())
r_string = input().split(" ")
radiuses = []
for i in r_string:
    radiuses.append(int(i))

for j in range(n-1):
        common_factors = []
        for i in range(1, radiuses[j+1]+1):
            if (radiuses[0] % i == 0) & (radiuses[j+1] % i == 0):
                common_factors.append(i)
        gcf = max(common_factors)
        num = int(radiuses[0] / gcf)
        den = int(radiuses[j+1] / gcf)
        print("{}/{}".format(num, den))
