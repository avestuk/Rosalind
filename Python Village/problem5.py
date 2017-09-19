from datasetImporter import create_filepath


def import_even_lines():
    with open(create_filepath()) as file:
        line_count = 0
        even_line_contents = ''
        for line in file:
            line_count += 1
            if line_count % 2 == 0:
                even_line_contents += line
        return even_line_contents


print(import_even_lines())
