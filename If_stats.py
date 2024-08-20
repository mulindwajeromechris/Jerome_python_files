cold = True
raining = False
sunny = True
if cold and raining:
    print("I want a sweater and an umbrella")
elif not(cold) and not(raining):
    print("I only need a sweater")
elif sunny and cold and not(raining):
    print("the leopard gives birth")
elif sunny and cold:
    print("weird day")
else:
    print("I need spects")