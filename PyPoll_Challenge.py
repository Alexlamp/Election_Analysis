import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
county_options = []
# Make empty dictionaries for Candidate and County.
candidate_votes = {}
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the candidate does not match any existing candidate... If statement to get unique names
        if county_name not in county_options:
            county_options.append(county_name)
            # 2. Begin tracking each candidate's vote count. To create each candidate as a keyfor the dictionary.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count as we iterate through rows.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results) 

    # Iterate through the county list. Determine % of votes per county.
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        # print each candidate's name, vote count, and percentage of votes to terminal
        county_election_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_election_results)
        # Save the candidate results to our text file.
        txt_file.write(county_election_results)
  
        # Determine winning vote count and candidate. Determine if the votes is greater than the winning count.
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            winning_county = county
    txt_file.write("\n")

    county_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(county_results, end="")
    txt_file.write(county_results)

    # Iterate through the candidate list. Determine % of votes per candidate.
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # print each candidate's name, vote count, and percentage of votes to terminal
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate. Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)   