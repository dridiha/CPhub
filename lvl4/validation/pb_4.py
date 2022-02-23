def main():
   N = int(input())
   T = [tuple(map(int, input().split())) for i in range(N)]
   m = sorted(T, key=lambda x: (x[0], -x[1]))
   h = {k: interval  for k,interval in enumerate(m)}
   n = sorted(h, key=lambda x: (-h[x][1], h[x][0]))
   max_value = max(N - i - n[i] -1 for i in range(N) )
   print(max_value)

main()