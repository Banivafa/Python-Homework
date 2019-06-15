
import os
import csv


Election_Data = os.path.join('Pypoll.csv')

with open(Election_Data, newline="") as csvfile:
 csvreader= csv.reader(csvfile, delimiter = ",")
 print(csvreader)

 csv_header=next(csvreader)
 print(f"CSV Header:{csv_header}")


#declaring dictionary
 Candidate= dict()
#declaring items
 Candidate_count= 0
 winCandidate = ""
 winVotes = 0

 for row in csvreader:
  Candidate_count+= 1
  Cand = row[2]
  Candidate[Cand] = Candidate.get(Cand, 0) +1


#print

CandidateList = list(Candidate.keys())
NumberCandidates = len(CandidateList)
output = list()
output.append("Election Results")
output.append("-----------------")
output.append("Total Votes" + str(Candidate_count))
output.append("-----------------")

for cand in CandidateList:
 numberVotes = Candidate[cand]
 CandPercentage = round(100* numberVotes / Candidate_count, 3)
 output.append(cand + ": " + str(CandPercentage) + "% (" +str(numberVotes) + ")")

 if numberVotes > winVotes:
    winVotes = numberVotes
    winCandidate = cand

output.append("-----------------")
output.append("Winner: " + winCandidate)
output.append("-----------------")

for out in output:
 print(out)

outputFile = ("PyPoll.txt", "w")
for out in output:
  outputFile.write(out + "\n")


