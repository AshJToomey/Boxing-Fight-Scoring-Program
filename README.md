# Boxing Fight Scoring Program

A simple Python console application that lets you score a boxing match round-by-round between two fighters. The program tracks scores, handles knockouts, and announces the winner or a draw.

---

## Features

- Input fighter names  
- Set the number of rounds (e.g., 12 rounds)  
- Enter scores for each fighter per round (scores range from 0 to 10)  
- Option to declare a Knockout (KO) winner during any round  
- Calculates and displays the final total scores and announces the winner or a draw  
- Input validation for scores and rounds

---

## How to Use

1. Run the Python script:
   ```bash
   python boxing_score.py ```

2. Enter the names of Fighter 1 and Fighter 2 when prompted.

3. Enter the number of rounds.

4. For each round, enter the scores for each fighter (typically 10 for the round winner, 9 or less for the other).

5. Indicate if there was a knockout during the round, and if yes, specify the winner.

6. After all rounds (or a knockout), the program displays the final scores and declares the winner or a draw.

## Requirements
- Python 3.x

No external libraries required.

## Example Usage

Boxing Fight Scoring Program

Enter Fighter 1's name: Tyson
Enter Fighter 2's name: Ali
Enter number of rounds (e.g., 12): 3

Enter scores for each round:

--- Round 1 ---
Enter Tyson's score for Round 1 (usually 10 for winner, 9 or less for loser): 10
Enter Ali's score for Round 1 (usually 10 for winner, 9 or less for loser): 9
Was there a Knockout in this round? (yes/no): no

--- Round 2 ---
Enter Tyson's score for Round 2 (usually 10 for winner, 9 or less for loser): 9
Enter Ali's score for Round 2 (usually 10 for winner, 9 or less for loser): 10
Was there a Knockout in this round? (yes/no): no

--- Round 3 ---
Enter Tyson's score for Round 3 (usually 10 for winner, 9 or less for loser): 10
Enter Ali's score for Round 3 (usually 10 for winner, 9 or less for loser): 8
Was there a Knockout in this round? (yes/no): no

=== Final Score ===
Tyson: 29
Ali: 27

Winner: Tyson
--- Fight Completed! ---

## License
This project is open-source and free to use under the MIT License.
