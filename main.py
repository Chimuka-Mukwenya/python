print("fhbh")
password = 23 

i=0
while i<100:
    print(i)
    i = i +1
if i == int(password):
   print(password +"got it")
else:
   print("nop ")


iterable_value = 'Programming Hero'

iterable_obj = iter(iterable_value)
 
while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break
