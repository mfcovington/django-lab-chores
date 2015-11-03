import os
import sys
from setuptools import setup

if sys.version_info < (3, 2):
    print("Sorry, django-lab-chores currently requires Python 3.2+.")
    sys.exit(1)

# From: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django>=1.7",
    "django-lab-members>=0.2.5",
]

setup(
    name='django-lab-chores',
    version='0.0.0',
    packages=['lab_chores'],
    include_package_data=True,
    license='BSD License',
    keywords='lab chores jobs science',
    description='A Django app for assigning and tracking lab chores for scientists in a lab',
    long_description=(read('README.rst')),
    url='https://github.com/mfcovington/django-lab-chores',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)
