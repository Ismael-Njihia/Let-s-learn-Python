# Create variables to store the number of votes for each candidate
votes_A = 0
votes_B = 0
votes_C = 0

# Create a variable to store the total number of votes
total_votes = 0

# Allow voters to enter their votes
while True:
    # Prompt the voter to enter their vote
    vote = input("Enter your vote (A, B, or C): ")

    # Check if the voter entered a valid vote
    if vote.upper() == "A":
        # Increment the number of votes for candidate A
        votes_A += 1
    elif vote.upper() == "B":
        # Increment the number of votes for candidate B
        votes_B += 1
    elif vote.upper() == "C":
        # Increment the number of votes for candidate C
        votes_C += 1
    elif vote.upper() == "END":
        # End the voting process
        break
    else:
        # The voter entered an invalid vote
        print("Invalid vote. Please try again.")

    # Increment the total number of votes
    total_votes += 1

# Print the number of votes for each candidate
print("Number of votes for A:", votes_A)
print("Number of votes for B:", votes_B)
print("Number of votes for C:", votes_C)

# Print the total number of votes
print("Total number of votes:", total_votes)
