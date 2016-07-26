from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()

setup(name='proxapy',
      version='0.1.5',
      description='Simple API proxy that uses Flask/requests/gunicorn.',
      long_description=long_description,
      install_requires=[
          'flask',
          'gunicorn',
          'requests'
      ],
      url='http://github.com/enricobacis/proxapy',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['proxapy'],
      zip_safe=False,
      scripts=['scripts/proxapy'],
      keywords='api proxy server flask requests gunicorn')
