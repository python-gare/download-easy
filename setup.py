from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='Download Easy',
    version='0.0.2',
    author="Manickam R",
    description="Download Big or Small files without worry!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/python-gare/download-easy",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'Click',
        'tqdm',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        download-easy=download_easy.main:cli
    ''',
)
