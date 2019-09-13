import os
import csv
import sys

election_data_csv = os.path.join("Resources","election_data.csv")
sys.stdout = open("main.txt", "w")

with open(election_data_csv, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    next(csvReader)

    breakLine = "-------------------------"
    totalVotes = 0
    candidates = []
    KhanVotes = 0
    CorreyVotes = 0
    LiVotes = 0
    OTooleyVotes = 0
    results = []
    
    for row in csvReader:
#   * The total number of votes cast
        totalVotes += 1
#   * A complete list of candidates who received votes
        candidates.append(row[2])

    uniqueCandidates = []
    for x in candidates:
        if x not in uniqueCandidates:
            uniqueCandidates.append(x)
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
    for vote in candidates:
        if vote == "Khan":
            KhanVotes += 1
        elif vote == "Correy":
            CorreyVotes += 1
        elif vote == "Li":
            LiVotes += 1
        elif vote == "O'Tooley":
            OTooleyVotes += 1

        KhanPercent = (KhanVotes / totalVotes) * 100
        CorreyPercent = (CorreyVotes / totalVotes) * 100
        LiPercent = (LiVotes / totalVotes) * 100
        OTooleyPercent = (OTooleyVotes / totalVotes) * 100
#   * The winner of the election based on popular vote.
    results.append(KhanVotes)
    results.append(CorreyVotes) 
    results.append(LiVotes)
    results.append(OTooleyVotes)
    mostVotes = max(results)
    winner = uniqueCandidates[results.index(mostVotes)]

#   * As an example, your analysis should look similar to the one below:

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
print(f'Election Results \n{breakLine}')
print(f'Total Votes: {totalVotes} \n{breakLine}')
print(f'Khan: {round(float(KhanPercent), 3)}% ({KhanVotes})')
print(f'Correy: {round(float(CorreyPercent), 3)}% ({CorreyVotes})')
print(f'Li: {round(float(LiPercent), 3)}% ({LiVotes})')
print(f"O'Tooley: {round(float(OTooleyPercent), 3)}% ({OTooleyVotes}) \n{breakLine}")
print(f'Winner: {winner} \n{breakLine}')

