from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()

setup(
    name="uxml",
    version="0.3.0",
    py_modules=["uparallel"],
    url="http://github.com/bobuk/uparallel",
    author="Grigory Bakunov",
    author_email="thebobuk@ya.ru",
    description="uparallel - oversimplified helper for easy parallel functions execution ",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
