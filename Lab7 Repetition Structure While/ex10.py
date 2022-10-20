while True:
    x = input("Enter an integer number ('X' to exit):")
    if x == 'X':
        break
    else:
        try:
            x = int(x)
            for row in range(1,x+1):
                ans = ""
                for col in range(1,x+1):
                    if col == x + 1 - row or col == row:
                        ans += "X"
                    else:
                        ans += "."
                print(ans)
        except ValueError:
            print()
            
        