#creating list
#- in built
lst= list()

score = [42, 27, 37, 14, 48]
print("score", score)

list=['okay', 250, True, 3.14, {'country': 'india'}]
print("list", list)
third_element = list[3]
print(third_element)
does_exist= "okay" in list
print(does_exist)
list.append("new element")
print(list)

score.insert(2, 'new score')
print(score)

#removing element
score.remove('new score')
print(score)

#removing using pop
lst=['item1', 'item2']
lst.pop()
#removes last element, follow stack
list2=['item1', 'item2', 'item3']
list2.pop(1)
print(list2)

lst1 = ['item1', 'item2']
del lst1[0] # only a single item
del lst1        # to delete the list completely

score.clear() # to clear the list but not delete it
print(score)

list3=lst1+list
print(list3)

# syntax
lst = ['item1', 'item2']
lst.reverse()
print(lst)


# syntax
lst = ['item1', 'item2', 'item3', 'item4']
lst.sort()                # ascending
print(lst)
lst.sort(reverse=True)    # descending
print(lst)
