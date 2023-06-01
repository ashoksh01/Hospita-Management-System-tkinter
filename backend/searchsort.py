class sorting:
    def insertion_sort(self,list_a,index):
        for i in range(1,len(list_a)):
            new = list_a[i]
            j=i
            while j>0 and list_a[j-1][index] > new[index]:
                list_a[j] = list_a[j-1]
                j -= 1
            list_a[j] = new
        return list_a


class searchBox:
    def linear_search(self,si,source):
        for i in source:
            if si in i:
                return int(source.index(i))
        return False