from tkinter.messagebox import showinfo


def identify_separator(line):
    commas = line.count(',')
    semicolons = line.count(';')

    if commas > semicolons:
        return ","  # type: str
    else:
        return ";"


def split_input_to_array_of_lines(input):
    lines = []

    for line in input:
        line_separator = identify_separator(line)
        lines.append(line.split(line_separator))

    return lines


def convert_report_to_string(report):
    global str_len
    string = ""
    for row in report:
        for item in row:
            string = string + item + ";"
            str_len = len(string)
        string = string[:str_len - 1]
        string += "\n"

    print (string)
    print ("=========================================")

    return string


def convert(input, output):
    # tworzenie list konkretnych zmiennych
    global str_len
    samples = []
    unique_samples = []
    compounds = []
    unique_compounds = []
    values = []
    units = []

    lines = split_input_to_array_of_lines(input)

    input.close()

    # tworzenie listy zwierajacej same results bez naglowkow i ostatniej pustej linijki
    results = lines[1:]

    # wypelnianie list zmiennych wartosciami z pliku
    for line in results:
        sample_name, compound, value, unit = line[0], line[1], line[2], line[3]

        samples.append(sample_name)
        compounds.append(compound)
        values.append(value)
        units.append(unit)

        if sample_name not in unique_samples:
            unique_samples.append(sample_name)

        if compound not in unique_compounds:
            unique_compounds.append(compound)

    # tworzenie pierwszego wiersza do raportu wyjsciowego
    headers = ["Nr probki"] + unique_compounds

    # tworzenie raportu i dodawanie do niego pierwszego wiersza
    report = [headers]

    # dodanie wiersza (w kazdym wierszu tyle liczba miejsc = liczba unikalnych zwiazkow w pliku + 1 (nazwa samples)) dla kazdej samples.
    for sample_number in unique_samples:
        results_for_sample = ["brak"] * headers.count()

        for result in results:
            if result[0] == sample_number and results_for_sample[0] == "brak":
                results_for_sample[0] = result[0]
        report.append(results_for_sample)

    # wpisywanie values do raportu
    for result in results:
        sample_number, compound, value = result[0], result[1], result[2]

        row = report[unique_samples.index(sample_number) + 1]
        compound_position = unique_compounds.index(compound) + 1
        row[compound_position] = value

    # konwertowanie raportu do stringu do zpaisu w pliu

    string = convert_report_to_string(report)

    # zapisywanie do pliku
    output.write(string)
    output.close()

    showinfo("Wykonano", "Konwersja wykonana")
