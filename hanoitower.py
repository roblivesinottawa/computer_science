def printmove(fr, to):
    print(f"move from {str(fr)} to {str(to)}")

def towers(n, fr, to, spare):
    if n == 1:
        printmove(fr, to)

    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)

towers(2, "towerone", "towertwo", "towerthree")