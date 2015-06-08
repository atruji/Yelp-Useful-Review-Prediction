import sys
import json
import string
def lines(fp):
	filtReview=[]
	twats=fp.readlines()
	for i in twats:
		tweet=json.loads(i)
		if type(tweet) is dict:
			if tweet.has_key("text"):
				unicode_string=tweet["text"]
				encoded_string=unicode_string.encode('utf-8')
				ftweet=encoded_string.split(" ")
				filtReview.append(ftweet)
	return filtReview
def main():
	dfile = open(sys.argv[1])
	vocab = open(sys.argv[2])
	filtReview=lines(dfile)
	scores={}
	vocab=vocab.read()
	vocab=vocab.split("\n")
	for term in vocab:
		scores[term] = 1  

	#was
	for m in filtReview:
		sentvals=0
		prevN=""
		prevprevN=""
		for n in m:
			n=n.translate(string.maketrans("",""),string.punctuation)
			n=n.lower()
			if scores.has_key(n) and prevN!="not" and prevprevN!="not" and (prevN=="would" or prevprevN=="would"):
				sentvals=sentvals +1 
			prevprevN=prevN
			prevN=n
		print sentvals
		#if 'allsent' in locals():
		#	print True
		#	allsent.append(sentvals)
        #else:
		#	allsent=sentvals
		#	print False
	#print allsent



            


	








if __name__ == '__main__':
    main()
