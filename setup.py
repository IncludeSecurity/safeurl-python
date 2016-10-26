from distutils.core import setup

with open("README.md") as readme_fh:
    long_description = readme_fh.read()

setup(
    name="SafeURL",
    url="https://github.com/IncludeSecurity/safeurl-python",
    version="1.1",
    license="MIT License",
    requires=[
        "pycurl>=7.19.3",
    ],
    long_description=long_description,
)
