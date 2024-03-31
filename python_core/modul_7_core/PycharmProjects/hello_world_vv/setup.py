from setuptools import setup, find_namespace_packages

setup(name='hello_world_vv',
      version='0.0.1',  # major.minor.package version
      description='1st package',
      author='Vadim',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['greeting = hello_world_vv.main:greeting']}
      )

