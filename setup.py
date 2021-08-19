from setuptools import setup


def get_version():
    from pathlib import Path

    init_path = Path("rhealsf/__init__.py")

    with init_path.open() as file_:
        for line in file_.readlines():
            if line.startswith("__version__"):
                return line.split('"')[1]


setup(
    name="rhealpix-sf",
    version=get_version(),
    description="Objects for DGGS Cells and collections of Cells.",
    install_requires=['rhealpix-geo'],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    maintainer="David Habgood",
    maintainer_email="david.habgood@surroundaustralia.com",
    url="https://github.com/surroundaustralia/rhealpix-sf",
    license="BSD",
    packages=["rhealsf"],
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    test_suite="tests",
    tests_require=["pytest"],
)
