'''
3)It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18

'''

# Function to get team details
def get_team_details(team_number):
    print(f"Team {team_number}:")
    team_name = input("Team Name:\n").strip()
    score = input("Score:\n").strip()
    overs_played = input("Overs played:\n").strip()
    
    return {
        'name': team_name,
        'score': score,
        'overs': overs_played
    }

# Function to display match details
def display_match_details(team1, team2):
    print("Match Details:")
    print(f"Team 1:")
    print(f"Name: {team1['name']}")
    print(f"Score: {team1['score']}")
    print(f"Overs played: {team1['overs']}")
    print(f"Team 2:")
    print(f"Name: {team2['name']}")
    print(f"Score: {team2['score']}")
    print(f"Overs played: {team2['overs']}")

# Main program
if __name__ == "__main__":
    team1 = get_team_details(1)
    team2 = get_team_details(2)
    
    display_match_details(team1, team2)
