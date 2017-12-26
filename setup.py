from setuptools import setup

requires = [
    'pyramid',
    'pyramid_mako',
    'deform',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy',
    'pytz',
    'bcrypt',
]

setup(name='service_app',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = service_app:main
    [console_scripts]
    initialize_db = service_app.initialize_db:main
    """,
)