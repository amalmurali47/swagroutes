import setuptools
import subprocess
import os


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    
def main():
    import swagroutes
    setuptools.setup(
        name="swagroutes",
        version=swagroutes.__version__,
        author="Amal Murali",
        author_email="amalmurali47@gmail.com",
        description="Command-line tool that extracts and lists API routes from Swagger files in YAML or JSON format.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/amalmurali47/swagroutes",
        packages=setuptools.find_packages(),
        package_data={"swagroutes": ["VERSION"]},
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
        entry_points={"console_scripts": ["swagroutes = swagroutes.__main__:main"]},
        install_requires=[
            "PyYAML >= 6.0",
        ]
    )
    
if __name__ == '__main__':
    main()

