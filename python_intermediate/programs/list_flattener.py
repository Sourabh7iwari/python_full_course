import itertools

list_of_lists= [[1,2,3],['a','b','c'],['!','@','#']]


flattened_list = list(itertools.chain(*list_of_lists))
print(flattened_list)                                