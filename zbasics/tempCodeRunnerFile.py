n = int(input("Enter the size of the diamond: "))

# for row in range(1, 2*n):  # Loop for both upper and lower parts
#     for col in range(1, 2*n):
#         if (row + col == n + 1) or (col - row == n - 1) or (row - col == n - 1) or (row + col == 3*n - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()