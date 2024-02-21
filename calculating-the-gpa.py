data_list = []
avg = 0
div = 0

while True:
    data = input()
    if data != 'exit':
        point,temp = data.split()
        point = float(point)
        temp = int(temp)
        avg = avg + point*temp
        div = div + temp
    else:
        break

avg = avg / div   
print("%.1f" %avg)     
            