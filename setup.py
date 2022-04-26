from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

setup(
	name='starcc',
	version='0.0.5',
	description='Python implementation of StarCC',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/StarCC0/starcc-py',
	author='StarCC',
	author_email='starcc@mail.shn.hk',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Text Processing :: Linguistic',
		'Natural Language :: Chinese (Simplified)',
		'Natural Language :: Chinese (Traditional)',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
	],
	keywords='chinese nlp natural-language-processing',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	package_data={
		'StarCC': ['dict/*'],
	},
	include_package_data=True,
	python_requires='>=3.7, <4',
	install_requires=['jieba', 'pygtrie'],
	entry_points={},
	project_urls={
		'Bug Reports': 'https://github.com/StarCC0/StarCC/issues',
		'Source': 'https://github.com/StarCC0/StarCC',
	},
	zip_safe=False
)
