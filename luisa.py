import random
def lamp():
    try:
        s=int(input("number"))
        if s <=0:
            print("enter new number")
            return
        count=0
        status=random.randint(0,1)
        print(f" first status:{"on"if status==1 else"of"}")
        for i in range(s):
            sw=random.randint(0,1)
            if sw !=status:
                count+=1
                status =sw
            print("on"if sw==1 else"off")
        print(f"changes of status{count}")
    except ValueError:
        print("enter a new second")
lamp()