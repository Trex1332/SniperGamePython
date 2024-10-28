import random 

def main():
    heads = ["round","square"]
    hair = ["Blond","Brown"]
    shirt =["red","green","blue"]
    shote = False 
    target = gettarget(heads,hair,shirt)
    print(f"Your target has a {target["head"]} head, They have {target["hair"]} hair and they are wearing a {target["shirt"]} shirt")
    looking = gettarget(heads,hair,shirt)
    while shote == False:
        print(f"You are looking at a person with a {looking["head"]} head, they have {looking["hair"]} hair and they are wearing a {looking["shirt"]} shirt")
        shoot = input("shoot Y/N? ")
        if shoot.lower() == "n":
            looking = gettarget(heads,hair,shirt)
        elif shoot.lower() == "y":
            shote = True 
            if target == looking:
                print("good shot")
            else:
                print("Wrong person you muppet")

            agian = input("Play Again?: Y/N ")
            if agian.lower() == "y":
                main()
            elif agian.lower() == "n":
                return 0
            else:
                print("invalid ending")
                return 0
        else:
            print("I didnt understand changing targets ")    
     
     

def gettarget(head,hair,shirt):
    target = {"head":head[random.randrange(0,len(head))], "hair": hair[random.randrange(0,len(hair))],"shirt": shirt[random.randrange(0,len(shirt))]}
    return target 
main()