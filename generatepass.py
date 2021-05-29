import random
import string
value = 16
# length = int(input(length))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
# symbols = string.punctuation

all = lower + upper + num
temp = random.sample(all, value)
password = "".join(temp)
print(password)
