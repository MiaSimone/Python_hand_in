import csv

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()
    for line in content:
        print(line.strip().split(','))


def write_list_to_file(output_file, lst):
    with open(output_file, 'a+') as output_file:
        for item in lst:
            for element in item:
                if (output_file.write(str(element) + '\n')):
                    print('New line added!')

def write_arb_to_file(output_file, *arbs):
    with open(output_file, 'a+', newline='') as output_file:
        for arb in arbs:
            if (output_file.write(str(arb) + '\n')):
                print('New line added!')
        #output_writer.writerow(['2015', '1', '0', '5104', '2,3'])


def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
    data = []    
    for line in lines:
        data.append(line)

    print(data)    

if __name__ == '__main__':
    args = sys.argv
    input = args[len(args)-1]
    lis = read_csv(input)

    if(args.__contains__("--file")):

        file = args[args.index("--file") +1]
        write_list_to_file(file, lis)
    else:
        print(lis)




