from setuptools import setup

setup(
    name='tfidf-vectoriser',
    version='0.1',
    packages=[ ],
    url='',
    license='',
    author='aniftos',
    author_email='aniftos@google.com',
    description='',

    install_requires=[
        'scikit-learn>=0.15.0',
        'scipy>=0.14',
        'pandas>=0.11.0',
        'numpy>=1.6.1',
        'google-cloud-storage',
        'gcsfs', 'mock'],

    #test_suite='nose.collector',
    tests_require=['pytest', 'mock', 'nose', 'coverage'],


    setup_requires=['nose>=1.0'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    #extras_require={  # Optional
    #    'dev': ['check-manifest', 'coverage'],
    #    'test': ['coverage'],
    #},
)
