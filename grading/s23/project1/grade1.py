import csv

questions = [
    'Listing of all files in a directory, including "hidden" files.',
    "A long-list of files in a directory, with file sizes in the most appropriate of the following: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte",
    "The first fifteen lines of a file.",
    "The last fifteen lines of a file.",
    'Every line in a file containing the word "red".',
    'All files in a directory ending with "txt".',
    'The five most recently modified files in the current directory.',
    'The five least recently modified files in the current directory.',
    'The number of files in the current directory.',
    'All Python files in the current directory or any of its recursive subdirectories.',
    'All Python files in the current directory that import the math module. Do not include the text from the file, only the filename.',
    'All currently executing Python programs.',
    'All files in the current directory, sorted from the largest number of lines to the smallest. Include the number of lines in the output.',
    'All files in the current directory, sorted from the smallest number of lines to the largest. Include the number of lines in the output.'
]

answers = {}
with open("Part1.csv") as part1:
    lines = csv.reader(part1)
    top = True
    for line in lines:
        if top:
            top = False
        else:
            last = line[1].split()[1]
            if last not in answers:
                answers[last] = []
            answers[last].extend(line[2:])

with open("Part2.csv") as part2:
    lines = csv.reader(part2)
    top = True
    for line in lines:
        if top:
            top = False
        else:
            last = line[1].split()[1]
            if last not in answers:
                answers[last] = []
            answers[last].extend(line[2:])


with open("project1grades.csv") as spreadsheet:
    lines = csv.reader(spreadsheet)
    for line in lines:
        score = 0
        name = line[0]
        problems = []
        for i in range(len(questions)):
            grade = line[i + 1]
            works = grade == '1' or grade.startswith("Works")
            comment = grade != '1'
            if works:
                score += 1
            if comment:
                problems.append(f'"{questions[i]}"')
                problems.append(f'$ {answers[name][i]}')
                problems.append(f'* {grade}')
        with open(name, 'w') as fout:
            fout.write("""Grade is out of 14 points. 
* 0-7 points:  Not complete
* 8-13 points: Partially complete
* 14 points:   Complete\n\n""")
            if len(problems) == 0:
                fout.write(f"Excellent job! Complete.")
            else:
                if score >= 8:
                    fout.write(f"Score: {score}. Good job. Partially complete.\n\n")
                else:
                    fout.write(f"Score: {score}. Needs improvement. Not complete.\n\n")
                fout.write("""Each question with an incorrect answer is included with your solution and
a brief explanation of the problem with the submitted solution.

You may spend a token to resubmit your solutions if you wish to improve your
grade. You are invited to ask questions about your solution prior to submitting
a revision either via chat or in office hours. Resubmit by replying to this 
message with an improved solution for each problem that you wish to 
re-attempt.\n\n""")
                fout.write('\n'.join(problems))
