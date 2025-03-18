# Specify the input and output file paths
input_file_path = 'input.txt'
output_file_path = 'output.txt'

unic_line = set()
try:
    # Open the input file for reading and the output file for writing
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Read each line from the input file
        for line in input_file:
            line = line.rstrip('\n')
            print(unic_line)
            if line not in unic_line: 
                # Write the line to the output file
                unic_line.add(line)
                output_file.write(line + '\n')
    print(f"Content successfully written to {output_file_path}")
except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")