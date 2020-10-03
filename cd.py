while True:
    N, M = [int(i) for i in input().split(" ")]
    if N == 0 & M == 0:
        break

    jack_cds = set(int(input()) for _ in range(N))
    jill_cds = set(int(input()) for _ in range(M))
    sell = jack_cds & jill_cds
    print(len(sell))
