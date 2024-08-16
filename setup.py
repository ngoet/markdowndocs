from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="markdowndocs",
    version="0.1.1",
    author="ngoet",
    author_email="ndgoet@gmail.com",
    description="A light-weight markdown code documentation generator",
    install_requires=[
        "tabulate>=0.8.7",
        "pandas>=1.1.2",
        "typer>=0.3.2",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngoet/MarkdownDocs",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["markdowndocs = markdowndocs.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
