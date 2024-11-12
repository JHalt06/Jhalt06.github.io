import random

def quick_sort(a_list):
    if len(a_list) <= 1: # 1 element:    Stops recursion.
        return a_list
    else:
        pivot = a_list[-1]
        # pivot = a_list[len(a_list)//2]
        #pivot = a_list[random.randrange]
        less, same,  more = partition(pivot, a_list) # calling the function three times to define each variable. 
        sorted_less = quick_sort(less)
        sorted_more = quick_sort(more)
        return sorted_less + same + sorted_more
            
def partition(pivot, a_list):
    less = []
    same = []
    more = []
    for element in a_list:
        if element < pivot:
            less.append()
        elif element == pivot:
            same.append()
        elif element > pivot:
            more.append()
    return(less, same, more) # comment out after.




def main():
    a_list = [3,1,3,5,4,0]
    x = quick_sort(a_list) # Time Complexity: 
    print(x)
main()
