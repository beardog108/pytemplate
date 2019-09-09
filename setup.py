from setuptools import setup, find_packages

setup(name='modulename',
      version='0.0.0',
      description='Library desc',
      author='Author Name',
      author_email='author@example.com',
      url='https://example.com/',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
      ],
     )
