print("""=================================
      ELECTION SYSTEM
=================================\n""")

candidates = {}
voters = {}

while True:
    print("""1. Candidate Portal
2. Voter Portal
3. View Results
4. Exit\n""")

    try:
        a = int(input("Enter Choice: "))

        if a == 1:
            while True:
                print("========== CANDIDATE PORTAL ==========\n")
                print("""1. Register Candidate
2. Candidate Login
3. Back\n""")
                b = int(input("Enter Choice: "))

                if b == 1:
                    cand_id = input("Enter Candidate ID: ").strip()
                    cand_name = input("Enter Candidate Name: ").strip()
                    cand_party_name = input("Enter Party Name: ").strip()

                    if len(cand_id) != 0 and len(cand_name) != 0 and len(cand_party_name) != 0:
                        if cand_id in candidates:
                            print("Candidate ID Already Exists")
                        else:
                            candidates[cand_id] = {
                                "Candidate Name": cand_name,
                                "Candidate Party Name": cand_party_name,
                                "Votes": 0
                            }
                            print("Candidate Registered Successfully!")
                    else:
                        print("Provided Candidate's information is Invalid")

                elif b == 2:
                    login = input("Enter Candidate ID: ").strip()

                    if login in candidates:
                        while True:
                            print("""1. View My Details
2. View My Vote Count
3. Logout\n""")
                            c = int(input("Enter Choice: "))

                            if c == 1:
                                print("Candidate ID: ", login)
                                print("Name: ", candidates[login]["Candidate Name"])
                                print("Party: ", candidates[login]["Candidate Party Name"])

                            elif c == 2:
                                print("Total Votes: ", candidates[login]["Votes"])

                            elif c == 3:
                                print("Successfully Logged Out")
                                break

                            else:
                                print("Invalid Choice")
                    else:
                        print("Invalid Candidate ID!")

                elif b == 3:
                    print("Candidate Portal exited by User")
                    break

                else:
                    print("Invalid Choice")

        elif a == 2:
            while True:
                print("========== VOTER PORTAL ==========\n")

                print("""1. Register Voter
2. Cast Vote
3. Back\n""")

                d = int(input("Enter Choice: "))

                if d == 1:
                    vot_id = input("Enter Voter ID: ").strip()
                    vot_name = input("Enter Name: ").strip()

                    if len(vot_id) != 0 and len(vot_name) != 0:
                        if vot_id in voters:
                            print("Voter ID Already Exists")
                        else:
                            voters[vot_id] = {
                                "Voter Name": vot_name,
                                "Voted": False
                            }
                            print("Voter Registered Successfully!")
                    else:
                        print("Invalid Information Provided")

                elif d == 2:
                    check = input("Enter Voter ID: ").strip()

                    if check in voters:
                        print("Voter Found")

                        if voters[check]["Voted"] == True:
                            print("You Have Already Voted!")
                        else:
                            if len(candidates) == 0:
                                print("No Candidates Registered Yet!")
                            else:
                                print("========== CANDIDATES ==========\n")

                                cand_list = list(candidates.items())

                                n = 1
                                for cand_key, cand_value in cand_list:
                                    print(f"{n}. {cand_value['Candidate Name']} ( {cand_value['Candidate Party Name']} )")
                                    n += 1

                                slt_cand = int(input("Enter Candidate Number: "))

                                if 1 <= slt_cand <= len(cand_list):
                                    chosen_id, chosen_data = cand_list[slt_cand - 1]
                                    print("Vote Cast Successfully!")
                                    voters[check]["Voted"] = True
                                    candidates[chosen_id]["Votes"] += 1
                                else:
                                    print("Invalid Candidate Selection!")
                    else:
                        print("Invalid Voter ID!")

                elif d == 3:
                    print("Voter's Portal exited by User")
                    break

                else:
                    print("Invalid Choice")

        elif a == 3:
            print("========== ELECTION RESULTS ==========\n")

            if len(candidates) == 0:
                print("No Candidates Registered Yet!")
            else:
                x = 1
                for cand_id, cand_data in candidates.items():
                    print(f"{x}. {cand_data['Candidate Name']} ( {cand_data['Candidate Party Name']} ) : {cand_data['Votes']} Votes")
                    x += 1

                max_votes = max(candidates[c]["Votes"] for c in candidates)

                winners = []
                for cand_id, cand_data in candidates.items():
                    if cand_data["Votes"] == max_votes:
                        winners.append(cand_data["Candidate Name"])

                if len(winners) == 1:
                    print("Winner: ", winners[0])
                    print("Votes: ", max_votes)
                else:
                    print("Winner: Tie Between", ", ".join(winners))
                    print("Votes: ", max_votes)

        elif a == 4:
            print("System exited by user")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input")