import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination', help='The name of the file to store the url in')

    print(parser.parse_args())

# python python_handin_template/modules/cliExercise.py http://www.dr.dk -d test.csv
#python python_handin_template/modules/cliExercise.py http://www.dr.dk


