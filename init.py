#author - pankaj moolrajani
import argparse
import urllib2
import threading
import time

def main():
	args = arguments()
	global dict_arg
	dict_arg = {}
	if args.number:
		dict_arg['n'] = int(args.number)
	if args.concurrent:
		dict_arg['c'] = int(args.concurrent)
	if args.url:
		dict_arg['u'] = args.url
	if args.file:
		dict_arg['f'] = args.file

	do_threading(dict_arg)
	

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n', default=1)
	parser.add_argument('--url', '-u')
	parser.add_argument('--file', '-f')
	parser.add_argument('--concurrent', '-c', default=1)

	return parser.parse_args()

def do_threading(dict_arg):
    global list_result
    list_result = []
    list_threads = []
    url = dict_arg['u']
    for n in range(dict_arg['n']/dict_arg['c']):
		for c in range(dict_arg['c']):
			t = threading.Thread(target=request, args=(url, list_result))
			list_threads.append(t)
			t.start()

def request(url, list_result):
	n = dict_arg['n']
	time_start = time.time()
	try:
		res_code = str(urllib2.urlopen(url).code)
	except:
		res_code = "404"
	print "response code: "+res_code

	#print time_res
	list_result.append(res_code)
	if len(list_result) == n:
		displayResults(list_result)
		time_end = time.time()
		time_res = time_end - time_start
		print "Time: ",
		print time_res
		

def displayResults(list_result):
	set_result = set(list_result)
	for code in set_result:
		print dict_arg['u']
		print code+": "+str(list_result.count(code))
	
if __name__ == "__main__":
	main()
