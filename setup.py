from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid-ipython',
    'waitress',
    'sqlalchemy',
    'psycopg2-binary',
    'pyramid_tm',
    'transaction',
    'zope.sqlalchemy'
]

setup(
    name='helloworld',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = helloworld:main',
            'initdb = helloworld.scripts.initializedb:main'
        ],
    	'console_scripts': [
            #'initdb = helloworld.scripts.initializedb:main',
        ],
    },
)