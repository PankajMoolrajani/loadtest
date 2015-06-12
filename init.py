#author - pankaj moolrajani
import argparse
import urllib2
import threading

def main():
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
	print dict_result

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n', default=1)
	parser.add_argument('--url', '-u')
	parser.add_argument('--file', '-f')
	parser.add_argument('--concurrent', '-c', default=1)

	return parser.parse_args()

def do_threading(dict_arg):
	list_thread = []
	dict_result = {}
	for url in dict_arg['u']:
		for n in range(dict_arg['n']/dict_arg['c']):
			for c in range(dict_arg['c']):
				t = threading.Thread(target=request, args=(url,))
				t.start()
				list_thread.append(t)
				res_code = str(urllib2.urlopen(url).code)
				if url not in dict_result.keys():
					dict_result[url] = {res_code: 1}
				else:
					if res_code not in dict_result[url].keys():
						dict_result[url][res_code] = 1
					else:
						dict_result[url][res_code] = dict_result[url][res_code]+1
	return dict_result


	
if __name__ == "__main__":
	main()
