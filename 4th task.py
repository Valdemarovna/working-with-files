# Решение 3й задачи
all_files_set = []

with open('1.txt') as f:
    set_lines_1 = f.readlines()
    len_1 = [len(set_lines_1)]
    name_file_1 = ['1.txt']
    first_file_set = name_file_1 + len_1 + set_lines_1
    all_files_set.append(first_file_set)

with open('2.txt') as f:
    set_lines_2 = f.readlines()
    len_2 = [len(set_lines_2)]
    name_file_2 = ['2.txt']
    second_file_set = name_file_2 + len_2 + set_lines_2
    all_files_set.append(second_file_set)

with open('3.txt') as f:
    set_lines_3 = f.readlines()
    len_3 = [len(set_lines_3)]
    name_file_3 = ['3.txt']
    third_file_set = name_file_3 + len_3 + set_lines_3
    all_files_set.append(third_file_set)

s_all_files_set = (sorted(all_files_set, key=len))

f_result = open('result.txt', 'w')
for index in s_all_files_set:
    for i in index:
        f_result.write(str(i).strip() + '\n')
f.close()
