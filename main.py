import random 

def main():
    heads = ["round","square"]
    hair = ["Blond","Brown"]
    shirt =["red","green","blue"]

    target = gettarget(heads,hair,shirt)
    print(f"Your target has a {target["head"]} head, They have {target["hair"]} hair and they are wearing a {target["shirt"]} shirt")
 
def gettarget(head,hair,shirt):
    target = {"head":head[random.randrange(0,len(head))], "hair": hair[random.randrange(0,len(hair))],"shirt": shirt[random.randrange(0,len(shirt))]}
    return target 
main()