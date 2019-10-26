cohort_file = open("cohort_data.txt")

for line in cohort_file:
    line = line.rstrip()
    words = line.split('|')

    if words[4] == 'G':
        full_name = words[0] + ' ' + words[1]
        print(full_name)