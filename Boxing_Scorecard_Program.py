def get_valid_score(fighter_name, round_number):
    while True:
        try:
            score = int(input(f"Enter {fighter_name}'s score for Round {round_number} (usually 10 for winner, 9 or less for loser): "))
            if 0 <= score <= 10:
                return score
            else:
                print("Please enter a score between 0 and 10.")
        except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    print("Boxing Fight Scoring Program\n") 
    
    # fighter names
    fighter1 = input("Enter Fighter 1's name: "). strip().title()
    fighter2 = input("Enter Fighter 2's name: ").strip().title()
    
    while True:
        try:
             num_rounds = int(input("Enter number of rounds (e.g., 12): "))
             if num_rounds > 0:
                 break
             else: 
                 print("Please enter a positive number of rounds.") 
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    # Intialize scores
    fighter1_total = 0
    fighter2_total = 0

    # Round by round scoring
    print("\nEnter scores for each round: ")
    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        f1_score = get_valid_score(fighter1, round_num)
        f2_score = get_valid_score(fighter2, round_num)
    
        fighter1_total += f1_score
        fighter2_total += f2_score

        # Check for knockout
        ko_input = input("Was there a Knockout in this round? (yes/no): ").strip().lower()
        if ko_input == "yes":
            while True:
                winner_input = input(f"Who won by KO? Enter '{fighter1}' or '{fighter2}': ").strip()
                if winner_input.lower() == fighter1.lower():
                    print(f"\nKnockout! {fighter1} wins by KO in Round {round_num}!")
                    print("Fight Over!")
                    return
                elif winner_input.lower() == fighter2.lower():
                    print(f"\nKnockout! {fighter2} wins by KO in Round {round_num}!")
                    print("Fight Over!")
                    return
                else:
                    print("Invalid input. Please enter a valid fighter's name.")
    
    # total score
    print("\n=== Final Score ===")
    print(f"{fighter1}: {fighter1_total}")
    print(f"{fighter2}: {fighter2_total}")

    # The Winner
    if fighter1_total > fighter2_total:
        print(f"\nWinner: {fighter1}")
    elif fighter2_total > fighter1_total:
        print(f"\nWinner: {fighter2}")
    else:
        print("\nResult: It's a draw!")

    print("--- Fight Completed! ---")

if __name__ == "__main__":
    main()