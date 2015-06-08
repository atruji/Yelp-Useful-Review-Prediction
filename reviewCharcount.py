import sys
import json
import string

def main():
dfile = open(sys.argv[1])
data=dfile.readlines()
for i in data:
	review=json.loads(i)
	encoded_string=review["text"].encode('utf-8')
	n=encoded_string.translate(string.maketrans("",""),string.punctuation)
	print ([review["review_id"],review["business_id"],review["votes"]["useful"],len("".join(n.split())),review['stars']])

















if __name__ == '__main__':
    main()
