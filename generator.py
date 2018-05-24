import argparse
parser = argparse.ArgumentParser(description='Fake Data Generator')
parser.add_argument("-t","--template",required=True,help="Template Path")
args = parser.parse_args()
print(args)