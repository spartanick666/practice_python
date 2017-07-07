repeat_list = [0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12]
norepeat_list = []

def remove_dups():
    #for x in repeat_list:
        #while x > len(repeat_list):
            #why does this next line of code needed to work?
         #   norepeat_list.append(x)
    return list(set(repeat_list))

print(remove_dups())
