# SafeURL for Python
### Ported by [@nicolasrod](https://github.com/nicolasrod) and docs by [@momopranto](https://github.com/momopranto)

## Overview
SafeURL is a library that aids developers in protecting against a class of vulnerabilities known as [Server Side Request Forgery](http://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/). It does this by validating each part of the URL against a configurable white or black list before making an HTTP request. SafeURL is open-source and licensed under MIT.

## Installation
Clone this repository and import it into your project.

## Implementation
SafeURL serves as a replacement wrapper for [PyCurl](http://pycurl.io/) in Python.

```python
try:
  #User controlled input
  url = request.args['url']
  su = safeurl.SafeURL()
  #Execute using SafeURL
  res = su.execute(url)
except:
  print "Unexpected error:", sys.exc_info()
  #URL wasn't safe
```

## Configuration
Options such as white and black lists can be modified. For example:

```python
try:
    su = safeurl.SafeURL()
    #Create an options object
    opt = safeurl.Options()
    opt.clearList("whitelist")
    opt.clearList("blacklist")
    #Allow requests to specific domains
    opt.setList("whitelist", ["google.com", "youtube.com"], "domain")
    #Restrict urls with the ftp scheme
    opt.setList("blacklist",["ftp"],"scheme")

    su.setOptions(opt)
    res = su.execute("http://www.youtube.com")
except:
    print "Unexpected error:", sys.exc_info()
```
