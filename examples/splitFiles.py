def split_file(input_filename, output_prefix, lines_per_file):
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()
    print(len(lines))
    total_files = len(lines) // lines_per_file + (len(lines) % lines_per_file > 0)
    for i in range(total_files):
        start_line = i * lines_per_file
        end_line = min((i+1) * lines_per_file, len(lines))
        output_filename = f"{output_prefix}_{i+1}.txt"
        with open(output_filename, 'w') as outfile:
            outfile.writelines(lines[start_line:end_line])

# Example usage
split_file('/logs/example/audit.log', 'output', 5)
