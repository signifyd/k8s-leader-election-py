from distutils.core import setup
setup(
  name = 'leaderelection',
  packages = ['leaderelection'],
  version = '0.0.1',
  license='GPL3',
  description = 'Kubernetes leader election',
  author = 'Joel Damata',
  author_email = 'joel.damata94@gmail.com',
  url = 'https://github.com/jdamata',
  download_url = 'https://github.com/jdamata/k8s-leader-election-py/archive/',
  keywords = ['Kubernetes', 'Controller', 'Leader', 'Election'],
  install_requires=[
          'kubernetes',
          'python-json-logger',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL3 License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)
