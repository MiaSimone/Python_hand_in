import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')

    print(parser.parse_args())

# python python_handin_template/modules/cliExercise.py /home/jovyan/python_handin_template/modules/test.csv