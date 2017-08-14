print("How old are you?", end =' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

#print(f"So, you're {age} old, {height} tall and {weight} heavy.")
formatter = "So, you're {} old, {} tall and {} heavy."
print(formatter.format(age, height, weight))

