from __future__ import annotations

from setuptools import setup


def get_readme():
    with open("README.md") as f:
        return f.read()


def get_license():
    with open("LICENSE") as f:
        return f.read()


CLASSIFIERS = """\
License :: OSI Approved
Programming Language :: Python :: 3.8 :: 3.9
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

DISTNAME = "snips"
AUTHOR = "Mario Conrad"
AUTHOR_EMAIL = "mario.conrad@gmail.com"
DESCRIPTION = "Simple snips with all sorts of libs"
LICENSE = get_license()
README = get_readme()

VERSION = '1.0.0'
ISRELEASED = True

PYTHON_MIN_VERSION = "3.8"
PYTHON_MAX_VERSION = "3.9"
REQUESTS_VERSION = "2.25.0"

INSTALL_REQUIRES = [
    "requests=={}".format(REQUESTS_VERSION),
]

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=["snips", "test"],
    python_requires=">={}, <={}".format(
        PYTHON_MIN_VERSION, PYTHON_MAX_VERSION),
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
