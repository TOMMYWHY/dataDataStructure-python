# a + b + c =100 a^2+b^2=c^2

import time

start_time = time.time()

# for a in range(0, 501):
#     for b in range(0, 501):
#         for c in range(0, 501):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 # print("a,b,c:%d,%d,%d" % (a, b, c))
#                 print(f"a,b,c:{a},{b},{c}")

for a in range(0, 501):
    for b in range(0, 501):
        c = 1000-a-b
        if a ** 2 + b ** 2 == c ** 2:
            # print("a,b,c:%d,%d,%d" % (a, b, c))
            print(f"a,b,c:{a},{b},{c}")

end_time = time.time()
print(f"spending time: {end_time - start_time}")
