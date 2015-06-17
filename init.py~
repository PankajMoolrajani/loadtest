#author - pankaj moolrajani
import argparse
import urllib2
import threading

def main():
	gloabal list_result
	lsit_result = [200]
	args = arguments()
	dict_arg = {}
	if args.number:
		dict_arg['n'] = int(args.number)
	if args.concurrent:
		dict_arg['c'] = int(args.concurrent)
	if args.url:
		dict_arg['u'] = [args.url]
	if args.file:
		dict_arg['f'] = args.file

	dict_result = do_threading(dict_arg)
	print '\n\n'


def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n', default=1)
	parser.add_argument('--url', '-u')
	parser.add_argument('--file', '-f')
	parser.add_argument('--concurrent', '-c', default=1)

	return parser.parse_args()

def do_threading(dict_arg):
    	list_threads = []
	for url in dict_arg['u']:
		for n in range(dict_arg['n']/dict_arg['c']):
			for c in range(dict_arg['c']):
                		t = threading.Thread(target=request, args=(url, list_result))
                		list_threads.append(t)
                		t.start()
				#res_code = str(urllib2.urlopen(url).code)

def request(url, list_result):
	res_code = str(urllib2.urlopen(url).code)
	list_result.append(res_code)
	print list_result

	
	
if __name__ == "__main__":
	main()
