alti=int(input("enter the altitude"))
if alti<=1000 :
    print("Safe To Land")
elif alti>1000 and alti<=5000 :
    print("Bring down to 1000")
elif alti>5000 :
    print("Turn Around ")