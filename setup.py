import os

from setuptools import setup

setup(
    name='utcformatter',
    version='0.1.0',
    author='ChangZhuo Chen',
    author_email='czchen@czchen.org',
    packages=[
        'utcformatter',
    ],
    url='https://github.com/czchen/utcformatter',
    license='MIT',
    description='logging.Formatter with UTC timezone',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
