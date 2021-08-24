requires = [
    'deform',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_tm',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main =helloworld:main'
        ],
        'console_scripts': [
            'initdb = scripts.initializedb:main'
        ],
    },
)