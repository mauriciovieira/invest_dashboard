from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

setup(
    name='invest_dashboard',
    version='0.1.0',
    description="An investment dashbaord",
    author="Mauricio Vieira",
    author_email='mauricio@mauriciovieira.net',
    url='https://github.com/mauriciovieira/invest_dashboard',
    packages=['invest_dashboard', 'invest_dashboard.images',
              'invest_dashboard.tests'],
    package_data={'invest_dashboard.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Dashboard=invest_dashboard.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='invest_dashboard',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
