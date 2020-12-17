#module의 import
'''import math
 이런식으로 모두 기능 하나를 모두 불러올 수 있음
print(math.ceil(1.2))
print(math.fabs(-1.2))


'''

from math import ceil, fsum
# 위처럼 math를 import해오면 사용하지 않는 기능도 불러옴
# 그러면 낭비 - 사용할 기능만 불러오는 것이 효율적
print(ceil(1.2))
print(fsum([3,4,5,6]))

# 가져온 모듈의 이름을 그대로 사용하지 않고 이름을 정해 줄 수 도 있음
import math as haha
print(haha.fabs(-123))

# 내가 만든 다른 파일을 import해올 수 도 있음
from calculator import plus

print(plus(1,2))
