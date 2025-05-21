def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = "input.txt"  # Replace with your actual file path

f = read_file_line_by_line(file_path)
print(next(f))
print(next(f))



