class Photo:
    def __init__(self,id,num_of_tags,tags):
        self.id = id
        self.num_of_tags = num_of_tags
        self.tags = tags

def getScore(a,b):
    inter = str(a.tags & b.tags)
    inter = inter.count('1')
    a_unique = a.num_of_tags - inter
    b_unique = b.num_of_tags - inter
    return min(inter,a_unique,b_unique)


input_file = open("C:\\Users\\Vansh Arora\\Desktop\\new\\a_example.txt")
photoList = [] # list of objects
tags = [] # list of all tags in input file
numberOfLines = int(input_file.readline())


for i in range(numberOfLines):
    tempList = (input_file.readline()).split() # convert each line to temporary list
    current_pic_tags = tempList[2:]      # list of tags in current line
    binary_string = ""      # to store tags
    
    # to add current tags in all tags list
    for tag in current_pic_tags:
        if tag not in tags:
            tags.append(tag)

    # convert tags to binary string
    for j in range(len(tags)-1,-1,-1):
        if tags[j] in current_pic_tags:
            binary_string += str(1)
        else:
            binary_string += str(0) 

    # adding each line as an object to photo list
    photoList.append(Photo(i,tempList[1],int(binary_string)))

# To Sort
def get_my_key(obj):
  return obj.num_of_tags
photoList.sort(key=get_my_key, reverse = True)

# Above this everything is fine

# To get score(under development)

k = 0
answer = [photoList[k]]
photoList[k].tags = 0
oldScore = 0
for each in photoList:
    max_score = each.num_of_tags // 2
    score = getScore(answer[k].tags,each.tags)
    if score == max_score:
        answer.append(each)
        each.tags = 0
        k += 1
        continue
        if score > oldScore:
            oldScore = score