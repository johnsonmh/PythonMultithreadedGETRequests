# Batch GET
## Python Multithreaded GET Requests

This Python library allows python programmers to perform many HTTP GET requests on different URLs, in parallel. 

## Example usage:
Let's say you have a list of URLs and want your program to go to the web and retrieve those URLs.

```
import batch_get
urls = ['http://google.com','http://apple.com','http://microsoft.com','http://apple.com']

responses = batch_get.get_urls(urls)
```

The ```responses``` variable is now a python dictionary that contains all of the urls as the keys, and all of the HTTP GET respones as the values. So now, you can iterate over all your responses and sift through the HTML response.

```
for url in responses:
  do_something(responses[url])
```

Or you can get a specific response with:

```
print("Google's web page looks like: " + responses['http://google.com'])
```

## Multithreaded
The best part is that it spins of a thread for every URL, and performs the requests in parallel. 
No need to spin of threads on your own.

If you run the program from the command line, using ```python batch_get.py```, it prompts you to enter the name of a text file to test the program with. I have a list of 36 urls. It then runs through the URLs, getting their sources from the internet and storing them into python dictionaries. It does it first using the multithreaded batch_get, and then it runs through them iteratively. It times both of them, showing how much faster the multithreaded example.
```
Multithreaded URL GETs took 3.252121 seconds, to get 36 web pages.
Iterative URL GETs took 20.445654 seconds, to get 36 web pages.
```
