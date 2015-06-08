import sys
import json
import string

def main():
	dfile = open(sys.argv[1])
	bus=dfile.readlines()
	for i in bus:
		busdata=json.loads(i)
		print busdata["business_id"]+","+str(busdata["review_count"])+","+str(busdata["stars"])



if __name__ == '__main__':
    main()
