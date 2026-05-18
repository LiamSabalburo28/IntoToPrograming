with open("names.txt", "r") as file:

    search_name = input("Enter a name to search for: ").lower()

    found_lines = []

    for line_number, line in enumerate(file, start=1):

        cleaned_line = line.strip().lower()

        if cleaned_line == search_name:
            found_lines.append(line_number)

if found_lines:
    print(f"{search_name.title()} was found on these lines:")

    for line in found_lines:
        print(f"Line {line}")
else:
    print(f"{search_name.title()} was not found...")