def insert_sort(origin_list):

    sorted_list = []
    for i in range(0, len(origin_list)):
        #print sorted_list
        if len(sorted_list) == 0:
            sorted_list.append(origin_list[i])
            continue
        #range(start,stop,step=-1)==>倒序
        for j in range(len(sorted_list) - 1, -1, -1):
            if sorted_list[j] <= origin_list[i]:
                sorted_list.insert(j + 1, origin_list[i])
                break
            if j == 0:
                sorted_list.insert(0, origin_list[i])
    origin_list[:] = sorted_list[:]

origin_list = [5, 3, 1, 7, 9, 8]
insert_sort(origin_list)
print(origin_list)
