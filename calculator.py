def main():
  try:
    j = input("Enter operator:\n")
    i = float(input("Enter first number:\n"))
    k = float(input("Enter second number:\n"))
    if (j == 'q'):
      exit(0)
    elif (j == "/"):
      print(i/k)
    elif (j == "*"):
      print(i*k)
    elif (j == "+"):
      print(i+k)
    elif (j == "-"):
      print(i-k)
    else:
      print("Invalid operator")
  except Exception:
    print("\nError")

while True: 
  main()