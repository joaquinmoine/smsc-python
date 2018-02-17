from setuptools import setup

setup(
    name='smsc-python',
    packages=['smsc'],
    version='1.0.1',
    description='Send SMS with https://www.smsc.com.ar/',
    author='Joaquin Moine',
    author_email='joaquinmoine@gmail.com',
    url='https://github.com/joaquinmoine/smsc-python',
    license=open('LICENSE').read(),
    keywords=['sms', 'send'],
    install_requires=['requests>=2.18.4'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
