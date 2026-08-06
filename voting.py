#Voting system
votes = {
    "Ruto": 0,
    "Wangari": 0,
    "Uhuru": 0,
    "Mwai": 0
}

while True:
    print("\n....Voting System....")
    print("candidates:")

    for candidate in votes:
        print(f"- {candidate}")

    print("\nType 'exit' to stop voting.")

    vote = input("Enter your vote: ").title()

    if vote == "Exit":
        break

    if vote in votes:
        votes[vote] += 1
        print(f"Thank you for voting for {vote}!")
    else:
        print("Invalid vote! Please try again.")

print("\n...Voting Results:...")

for candidate, vote_count in votes.items():
    print(f"{candidate}: {vote_count} votes")

winner = max(votes, key=votes.get)
print(f"\nThe winner is {winner} with {votes[winner]} votes!")