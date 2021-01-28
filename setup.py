from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='downloadEasy',
    version='0.0.1',
    author="Manickam R",
    description="Download Big or Small files without worry!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'tqdm',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        downloadEasy=download_easy.main:cli
    ''',
)
