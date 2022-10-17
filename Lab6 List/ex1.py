lists = input("Enter a comma-separated list: ").split(",")
for a in lists:
  for b in lists:
    for c in lists:
      if a != b:
        if a != c:
          if b != c:
            print(a,b,c)