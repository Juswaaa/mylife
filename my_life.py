def write_multiple_lines_to_file(output_file):
    with open(output_file, 'w') as file:
        while True:
            line = input("Enter line: ")
            file.write(line + "\n")

            more_lines = input("Are there more lines? (y/n): ").lower()
            if more_lines != 'y':
                break

def main():
    output_file = "my_life.txt"
    write_multiple_lines_to_file(output_file)

if __name__ == "__main__":
    main()
