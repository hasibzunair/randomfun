'''
Given a universal set and a collection of sets,
find min number of set that equal their union in universal set

Algo:
    while not all elems in U covered
        for all uncovered sets in collections
        pick the set that covers most of elems in universal


NP-complete, so no efficient soln exists
'''
# set collection
collection = {'set_1': {1, 2, 3},
              'set_2': {2, 4}, 
              'set_3': {3, 4}, 
              'set_4': {4, 5}}
#universal set
elements_not_covered = {1, 2, 3, 4, 5}

def set_cover(collection, elements_not_covered):
    sets_used = []
    while elements_not_covered:
        
        elements_covered = set()
        for set_ in collection.keys():

            if set_ in sets_used:
                continue
                
            current_set = collection[set_]
            would_cover = elements_covered.union(current_set)

            if len(would_cover) > len(elements_covered):
                elements_covered = would_cover
                sets_used.append(set_)

                elements_not_covered -= elements_covered

                #print(elements_not_covered)
                if not elements_not_covered:
                    break
    return sets_used

print(set_cover(collection, elements_not_covered))
