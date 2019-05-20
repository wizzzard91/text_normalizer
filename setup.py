from setuptools import setup, find_packages

setup(name='text_normalizer',
      version='1.0',
      description='Normalization of different texts for text.ru',
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing',
      ],
      keywords='text normalize',
      url='https://github.com/wizzzard91/text_normalizer',
      author='Bulat Nabiullin',
      author_email='bulat.nabiullin@onetwotrip.com',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
