from distutils.core import setup
import setuptools

setup(
  name = 'uchu',
  packages = ['uchu'],
  version = '0.0.7',
  description = 'Sane interface to cloud services.',
  long_description = '',
  author = '',
  license = '',
  package_data={},
  url = 'https://github.com/alvations/uchu',
  keywords = [],
  classifiers = [],
  install_requires = ['boto3', 'botocore'],

)
