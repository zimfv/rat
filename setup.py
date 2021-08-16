from setuptools import setup, find_packages


setup(name='rat', 
      version='0.1', 
      url='https://github.com/zimfv/rat',
      author='Fedor Zimin', 
      author_email='zimfv@yandex.ru', 
      description='RAT - Restoring Aggregated Tables',
      packages=find_packages(include=['rat']),
      long_description=open('README.md').read(), 
      setup_requires=['numpy>=1.20.1', 'pandas>=1.2.1', 'cvxpy>=1.1.13']
)