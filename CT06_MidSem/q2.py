# ============================================================
# Step 1: Ask for Starting Amount
# ============================================================
start = input("what is your starting amount: ")


# ============================================================
# Step 2: Ask for Number of Days
# ============================================================

days = input("how many days: ")

# ============================================================
# Step 3: Use a for loop to simulate savings
# ============================================================
for i in range(1,int(int(days) + 1)):
    total = (int(start)
              + (i))
    print(str(("Day 1: ") + str(total)))
# - Update and print the total each day
#   Day <X>: $<Y>
# ============================================================



# ============================================================
# Step 4: Print Final Total
# ============================================================
# - Print the final amount in this format:
#   Total amount saved = $<Z>
# ================================