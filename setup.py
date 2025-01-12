import subprocess
from os import path
from setuptools import setup
from setuptools.command.install import install


here = path.abspath(path.dirname(__file__))

with open('README.rst') as f:
    readme = f.read()


class MyInstall(install):
    def run(self):
        try:
            subprocess.call(['/bin/bash', 'prepare.sh'], cwd=here)
            subprocess.call(['python', 'prepare.py'], cwd=here)
        except Exception as e:
            print(e)
            print("Error compiling openssl.")
            exit(1)
        else:
            install.run(self)


bbclib_requires = [
    'pyOpenSSL>=16.2.0',
    'cryptography>=2.1.4',
    'pytest<=3.2.*,>=3.0.5',
    'msgpack-python>=0.4.8',
    'bson'
]

bbclib_packages = ['bbc1', 'bbc1.libs', 'bbc1.compat']

bbclib_commands = []

bbclib_classifiers = [
                    'Development Status :: 4 - Beta',
                    'Programming Language :: Python :: 3.5',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Topic :: Software Development']

setup(
    name='py-bbclib',
    version='1.3',
    description='The library of BBc-1 transaction data structure definition',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/beyond-blockchain/py-bbclib',
    author='beyond-blockchain.org',
    author_email='bbc1-dev@beyond-blockchain.org',
    license='Apache License 2.0',
    classifiers=bbclib_classifiers,
    cmdclass={'install': MyInstall},
    packages=bbclib_packages,
    scripts=bbclib_commands,
    install_requires=bbclib_requires,
    zip_safe=False)

