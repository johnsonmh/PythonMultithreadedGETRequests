import urllib.request as urllib
import threading
import time

# Spins off a thread for every URL passed in and performs the requests in parallel
# Returns a python dictionary object where the key is the URL and the value is the GET response
def get_urls(urls):
	responses = {}
	threads = []

	#Create threads
	for url in urls:
		request_thread = threading.Thread(target=get_url, args=(url, responses, ))
		threads.append(request_thread)

	# Start then join threads
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()

	return responses

# Method for each thread of getting a single URL, enters 
def get_url(url, responses):
	try:
		response = urllib.urlopen(url)
		get_response = response.read()
		response.close()
		responses[url] = get_response
	except: # If HTTP error encountered, fill None into response
		responses[url] = None

# Method that iteratively runs through all the URLs in sequence
# Returns a python dictionary object where the key is the URL and the value is the GET response
def get_urls_iteratively(urls):
	responses = {}

	for url in urls:
		try:
			response = urllib.urlopen(url)
			get_response = response.read()
			response.close()
			responses[url] = get_response
		except: # If HTTP error encountered, fill None into response
			responses[url] = None

	return responses

def main():
	file_name = input('Enter file name of URLs to test: ')
	infile = open(file_name, 'r')
	urls = []

	for line in infile:
		urls.append("http://" + line)

	# Time multithreaded GETs
	start_time = time.time()
	responses = get_urls(urls)
	finish_time = time.time()

	print("Multithreaded URL GETs took %f seconds, to get %i urls." % (finish_time - start_time, len(urls)))

	# Time Iterative GETs
	start_time = time.time()
	responses = get_urls_iteratively(urls)
	finish_time = time.time()

	print("Iterative URL GETs took %f seconds, to get %i urls." % (finish_time - start_time, len(urls)))

# If called from the command line, call main method
if __name__ == '__main__':
    main()