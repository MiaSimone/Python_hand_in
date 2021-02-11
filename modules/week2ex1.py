import csv

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()
    for line in content[:20]:
        print(line.strip().split(','))


def write_list_to_file(output_file, lst):
    with open(output_file, 'a+', newline='') as output_file:
        output_writer = csv.writer(output_file)
        if (output_writer.writerow(lst)):
            print('New line added!')
        #output_writer.writerow(['2015', '1', '0', '5104', '2,3'])

def write_arb_to_file(output_file, *arbs):
    with open(output_file, 'a+', newline='') as output_file:
        output_writer = csv.writer(output_file)
        for arb in arbs:
            if (output_writer.writerow(arb)):
                print('New line added!')
        #output_writer.writerow(['2015', '1', '0', '5104', '2,3'])


def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
        print(lines)
    #for line in lines:
        #print(line.rstrip())



