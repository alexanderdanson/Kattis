input = input()
inputs = input.split(" ")

e = int(inputs[0])
f = int(inputs[1])
c = int(inputs[2])

bottles_in_stock = e + f
sodas_drunk = 0

while bottles_in_stock >= c:
    bottles_not_used = int(bottles_in_stock % c)
    sodas_afforded = int((bottles_in_stock - bottles_not_used) / c)
    sodas_drunk = sodas_drunk + sodas_afforded
    bottles_in_stock = bottles_not_used + sodas_afforded

print(sodas_drunk)


