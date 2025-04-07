for i in range(2, 10) :
    print(f"#  {i}단  #", end=" ")
for i in range(1, 10) :
    print()
    for j in range(2, 10) :
        print(f"{j}X {i:2d}= {i*j:2d}", end=" ")