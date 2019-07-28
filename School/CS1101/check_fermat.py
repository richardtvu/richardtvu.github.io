def check_fermat(a, b, c, n):
  left_side_equation = a**n + b**n
  right_side_equation = c**n
  if left_side_equation == right_side_equation and n > 2:
    print("Holy smokes, Fermat was wrong!")
  elif left_side_equation == right_side_equation and n <= 2:
    print("Works, as expected.")
  else:
    print("No, that doesn't work.")

check_fermat(1, 1, 2, 1)
check_fermat(2, 2, 2, 3)
