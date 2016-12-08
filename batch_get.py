import urllib2
import threading
import time

def get_urls(urls):
	responses = {}
	threads = []

	#Create threads
	for url in urls:
		request_thread = Thread(target=get_url, args=(url, responses, ))
		threads.append(request_thread)

	# Start then join threads
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()

	return responses

def get_url(url, responses):
	response = urllib2.urlopen(url)
	get_response = response.read()
	response.close()
	responses[url] = get_response

def get_urls_iteratively(urls):
	responses = {}

	for url in urls:
		response = urllib2.urlopen(url)
		get_response = response.read()
		response.close()
		responses[url] = get_response

	return responses

def main():
	file_name = input('Enter file name of URLs to test: ')
	infile = open(file_name, 'r')
	urls = []

	for line in infile:
		urls.append(line)

	start_time = time.time()
	get_urls(urls)
	finish_time = time.time()

	print("Multithreaded URL GETs took: %f seconds." % (finish_time - start_time))

	start_time = time.time()
	get_urls_iteratively(urls)
	finish_time = time.time()

	print("Iterative URL GETs took: %f seconds." % (finish_time - start_time))



if __name__ == '__main__':
    main()