import safeurl
import sys

# Default
try:
    sc = safeurl.SafeURL()
    res = sc.execute("https://fin1te.net")
except:
    print("Unexpected error:", sys.exc_info())

# options
try:
    sc = safeurl.SafeURL()

    opt = safeurl.Options()
    opt.clearList("whitelist")
    opt.clearList("blacklist")
    opt.setList("whitelist", ["google.com", "youtube.com"], "domain")

    sc.setOptions(opt)
    res = sc.execute("http://www.youtube.com")
except:
    print("Unexpected error:", sys.exc_info())

# url
try:
    url = safeurl.Url.validateUrl("http://google.com", safeurl.Options())
except:
    print("Unexpected error:", sys.exc_info())

# redirects
try:
    sc = safeurl.SafeURL()

    opt = safeurl.Options()
    opt.enableFollowLocation().setFollowLocationLimit(10)
    sc.setOptions(opt)

    res = sc.execute("http://fin1te.net")
except:
    print("Unexpected error:", sys.exc_info())


# forbidden host
try:
    sc = safeurl.SafeURL()

    opt = safeurl.Options()
    opt.enableFollowLocation().setFollowLocationLimit(10)
    sc.setOptions(opt)

    res = sc.execute("http://localhost")
except:
    print("Error:", sys.exc_info())


# regex bug
try:
    sc = safeurl.SafeURL()

    opt = safeurl.Options()
    opt.setList("whitelist", ["exam.le"], "domain")
    sc.setOptions(opt)

    res = sc.execute("https://example.com/")

except:
    print("Error:", sys.exc_info())


# fqdn
try:
    sc = safeurl.SafeURL()

    opt = safeurl.Options()
    opt.setList("blacklist", ["example.com"], "domain")
    sc.setOptions(opt)

    res = sc.execute("https://example.com.")

except:
    print("Error:", sys.exc_info())


