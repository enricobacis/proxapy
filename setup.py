from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='proxapy',
      version='0.1.2',
      description='Simple API proxy that uses Flask/requests/gunicorn.',
      long_description=long_description,
      install_requires=install_requires,
      url='http://github.com/enricobacis/proxapy',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['proxapy'],
      zip_safe=False,
      data_files=[('proxapy/config', ['proxapy/config/gunicorn'])],
      scripts=['scripts/proxapy'],
      keywords='api proxy server flask requests gunicorn')
