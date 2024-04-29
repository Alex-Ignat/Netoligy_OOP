import os


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def merge_files_and_print(dir, output_file):
    files = os.listdir(dir)
    files_content = []
    for file_name in files:
        file_path = os.path.join(dir, file_name)
        content = read_file(file_path)
        files_content.append((file_name, len(content), content))

    files_content.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_name, num_lines, content in files_content:
            outfile.write(f"{file_name}\n{num_lines}\n")
            outfile.writelines(content)
            outfile.write("\n")
    print_merged_content(output_file)


def print_merged_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print("Merged content:")
        print(file.read())


merge_files_and_print('files', 'HW_2_task_3_result.txt')