from my_library import person
def read_names_from_files(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]
def write_greetings_to_file(filename, greetings ):
    with open( filename, "w") as file:
        for greeting in greetings:
            file.write(greeting+ "\n")
def main():
    #read names from the file 'people.txt'
    names = read_names_from_files('people,txt')
    #create person objects and generate greeting
    greetings= {person(name).greeting() for name in names}
    #write greeting to the output file
    write_greetings_to_file('greetings.txt', greetings)

if __name__== "__main__":
    main()
