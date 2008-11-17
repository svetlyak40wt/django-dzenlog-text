from setuptools import setup, find_packages

setup(
    name = 'dzenlog-text',
    version = '0.2.1',
    description = '''This is a simple application for textual blog, based on the '''
                  '''django-dzenlog application.''',
    keywords = 'django apps blogging dzenlog',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-dzenlog-text/',
    install_requires = ['django-dzenlog>=0.2.0'],
    dependency_links = ['http://aartemenko.com/media/packages.html'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(exclude=['example*']),
    package_data = {
        'templates': ['*.html'],
    },
    include_package_data = True,
)

