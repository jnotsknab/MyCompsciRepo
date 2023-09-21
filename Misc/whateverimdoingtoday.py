def sickCount(days):
  n1, n2, n3 = 1, 5, 17
  count = 3
  if days <= 0:
    return "Invalid day"
  elif days == 1:
    return n1
  elif days == 2:
    return n2
  elif days == 3:
    return n3
  else:
    while count < days:
        nth = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = nth
        count += 1
    return nth

print("OUTBREAK!")
n = int(input("What day do you want a sick count for?: "))
ans = sickCount(n)
if ans != "Invalid day":
  print(f"Total people with flu: {ans}")
else:
  print("Invalid day")
  