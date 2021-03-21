l = [1, 3, 0, 3, 4, 8, 3, 3, 2]
start, end = 0,0
max_rect = 0

rects = []
for i in range(len(l)):
  if len(rects) > 0:
    top = rects[-1][1]
  else:
    top = 0
  if len(rects) == 0 or l[i] > top:
    for j in range(top, l[i]):
      rects.append((i, j + 1))
  else:
    while len(rects) > 0 and l[i] < rects[-1][1]:
      ln = rects.pop()
      max_rect = max(max_rect, (i - ln[0]) * ln[1])
if len(rects) > 0:
    ln = rects.pop()
    max_rect = max(max_rect, (len(l) - ln[0]) * ln[1])
print(max_rect)
