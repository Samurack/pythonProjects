import sys

first = float(sys.argv[1])
second = float(sys.argv[2])

result_sum = first + second
result_difference = first - second
result_product = first * second
result_quotient = first / second

print(f"{first} plus {second} equals {result_sum}")
print(f"{first} minus {second} equals {result_difference}")
print(f"{first} times {second} equals {result_product}")
print(f"{first} divided by {second} equals {result_quotient}")