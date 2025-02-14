ulogin = ["user1", "user2", "user3", "user1", "user2", "user4", "user1", "user5", "user3"]
unique = set(ulogin)
print("Total users login:",len(ulogin))
print("Unique users:",len(unique))
print("Total no of users login:")
for user in unique:
    count = 0
    for c in ulogin:
        if c==user:
            count+=1
    print(f"User {user}: {count} times")
