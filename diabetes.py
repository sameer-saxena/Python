print("Hello")

observed = 0
while observed != 5:
#body start
    a = input("Input your observed RBS Count")
    observed = int(a)
    if observed == 5:
        print("everything's normal")
    else:
        if observed > 5:
            print("your Sugar is high")
        else:
            print("your sugar is controlled")
#body end

print("Goodbye!")
