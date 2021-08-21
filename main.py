# This is the main python file to work with the week 3 homework
import os
import csv

# Part 1: PyBank:

pybank_csv = os.path.join("Resources", "budget_data.csv")
# Open and read csv file-->budget_data.scv
with open(pybank_csv) as csv_file_pybank:
    csv_reader_pybank = csv.reader(csv_file_pybank, delimiter=",")
    # read the header row
    csv_header_pybank = next(csv_reader_pybank)

    # Define few variables to hold counts/ total amounts/ average changes/maximum and minimum values
    # initially set the month counter to 0 for further adding up
    month_count = 0
    total_amount = 0
    change_value = 0
    # hard coding to insert the first value for the profit/loss
    # not sure is there better way to get first row value
    pre_value = 867884
    sum_change_value = 0
    average_change = 0
    max_change = 0
    max_change_date = ""
    min_change = 0
    min_change_date = ""

    # Get the data from each row after the header
    for row1 in csv_reader_pybank:
        # to run through each row in csv file, add one to the month counter
        month_count += 1
        # get the second column's data in excel (profit/loss) and add into total amount
        total_amount += int(row1[1])
        # the change value is the second month's profit/loss - first month's
        change_value = int(row1[1]) - pre_value
        # to reset the previous month's value as this row's value
        pre_value = int(row1[1])
        # sum up all the change values of profit/ loss
        sum_change_value += change_value

        # To compare the change value of profit/ loss with pre-defined value which is 0
        if change_value > max_change:
            # if the new change value is larger than origin one, then replace the value and record the date
            max_change = change_value
            max_change_date = row1[0]

        if change_value < min_change:
            min_change = change_value
            min_change_date = row1[0]
    # To calculate the average change of profit/ loss, the -1 is to minus the first date's
    average_change = round(sum_change_value / (month_count - 1), 2)

    # print the results
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_amount}")
    print(f"Average  Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n\n\n")

    # export the pybank analysis results into text file
    output_path = os.path.join("analysis", "analysis_results.txt")
    analysis_result = open(output_path, "w", newline="")
    analysis_result.write(f"Financial Analysis\n")
    analysis_result.write(f"----------------------------\n")
    analysis_result.write(f"Total Months: {month_count}\n")
    analysis_result.write(f"Total: ${total_amount}\n")
    analysis_result.write(f"Average  Change: ${average_change}\n")
    analysis_result.write(f"Greatest Increase in Profits: {max_change_date} (${max_change})\n")
    analysis_result.write(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n\n\n\n\n")


# Part 2: PyPoll:
pypoll_csv = os.path.join("Resources", "election_data.csv")
# Open and read csv file-->election_data.scv
with open(pypoll_csv) as csv_file_pypoll:
    csv_reader_pypoll = csv.reader(csv_file_pypoll, delimiter=",")
    # read the header row
    csv_header_pypoll = next(csv_reader_pypoll)

    total_vote_count = 0
    candi_list = []
    # Again, here what if I don't know the number of candidates?
    # Is there anyway else I can use to replace this hard coding with this known number list?
    vote_list = [0, 0, 0, 0]
    rate_list = [0, 0, 0, 0]
    winner_vote = 0
    winner = ""

    for row in csv_reader_pypoll:
        # to count the votes for all candidates
        total_vote_count += 1
        # if the candidate's name not exist in the candidate list, add the name in
        if str(row[2]) not in candi_list:
            candi_list.append(str(row[2]))
            candi_index = candi_list.index(str(row[2]))
            vote_list[candi_index] += 1
        # if the candidate's name already exist, add the vote to the candidate's name
        # by matching the candidate index in the candidate list
        else:
            candi_index = candi_list.index(str(row[2]))
            vote_list[candi_index] += 1

    # print the results
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_vote_count}")
    print(f"-------------------------")
    # Use a for loop here to repeat the calculation of vote percentage for each candidate
    for i in range(len(candi_list)):
        rate_list[i] = (int(vote_list[i])/total_vote_count)*100
        # compare the votes for each candidate and select the highest vote one
        if int(vote_list[i]) > winner_vote:
            winner = candi_list[i]
            winner_vote = int(vote_list[i])
        print("{}: {:.3f}% ({})".format(str(candi_list[i]), float(str(rate_list[i])), int(vote_list[i])))
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

    # export the pypoll analysis results into text file
    analysis_result.write(f"Election Results\n")
    analysis_result.write(f"----------------------------------------\n")
    analysis_result.write(f"Total Votes: {total_vote_count}\n")
    analysis_result.write(f"----------------------------------------\n")
    for j in range(len(candi_list)):
        rate_list[j] = (int(vote_list[j])/total_vote_count)*100
        # compare the votes for each candidate and select the highest vote one
        if int(vote_list[j]) > winner_vote:
            winner = candi_list[j]
            winner_vote = int(vote_list[j])
        analysis_result.write("{}: {:.3f}% ({})\n".format(str(candi_list[j]), float(str(rate_list[j])), int(vote_list[j])))
    analysis_result.write(f"----------------------------------------\n")
    analysis_result.write(f"Winner: {winner}\n")
    analysis_result.write(f"----------------------------------------\n")

