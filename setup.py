import setuptools

# used for pypi.org
setuptools.setup(
    name="GoodUSB",
    version="1.1",
    description="Prevent BadUSB attacks",
    license="MIT",
    author="TINYT1ME",
    long_description=open("README.md", "r", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TINYT1ME/GoodUSB",
    packages=["GoodUSB"],
    install_requires=["pythoncom", "keyboard"],
)
