from setuptools import setup, find_packages

setup(
    name="phonepe-payment",
    version="1.0",
    author="Dev Pancholi",
    author_email="devpancholigt2004@gmail.com",
    description="A simplify way for payment integration in our website and application. Works based on api Response.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Devpancholi04/phonepe-payment",
    packages=find_packages(),
    install_requires = ['request','json','hashlib','base64','webbrowser'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)