import random
l1=[random.randint(1,50) for i in range(10)]
print(l1)
l2=[random.randint(1,50) for i in range(15)]
print(l2)
overlap_elements = set([i for i in l1 if i in l2])
list_overlap = list(overlap_elements)
print(list_overlap)