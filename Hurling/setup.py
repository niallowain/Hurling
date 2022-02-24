from setuptools import setup

setup(
    name='Hurling',
    version='0.1.0',    
    description='Package to analyse hurling',
    url='https://github.com/niallowain/Hurling',
    author='Owain McCarthy',
    author_email='niallowain@protonmail.com',    
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['mpi4py>=2.0',
                      'numpy','matplotlib','pandas'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
) 
