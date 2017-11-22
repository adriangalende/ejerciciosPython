def whoLikesIt(list):
    whoLikesResult = ''
    if (len(list) > 0):
        if len(list) == 1 :
            whoLikesResult += list[0] + " likes this"
        elif len(list) == 2:
            whoLikesResult += list[0] + " and " + list[1] + " like this"
        elif len(list) == 3:
            whoLikesResult += list[0] + ", " + list[1] + " and " + list[2] + " like this"
        else:
            whoLikesResult += list[0] + ", " + list[1] + " and " + str(len(list) - 2) + " others like this"
    else:
        whoLikesResult = "no one likes this"

    return whoLikesResult

#likes=[] => no one likes this
likes=["Alex", "Jacob", "Mark", "Max","Adri","David"]
print(whoLikesIt(likes))
