import os
from distutils.core import setup
import pip


def install_tensorflow():
    install_target = 'tensorflow'
    if hasgpu():
        install_target += '-gpu'
    pip.main(['install', '-U', install_target])


def hasgpu():
    return not os.system('which nvidia-smi > /dev/null')

if __name__ == '__main__':
    install_tensorflow()

    setup(
        name='tnt',
        version='0.12.0.7',
        description='tnt is not tensorflow',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'License :: OSI Approved :: MIT License',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        license='MIT',
        url='https://github.com/TwentyBN/tnt',
        author='Ingo Fruend, Valentin Haenel',
        author_email='ingo.fruend@twentybn.com, valentin@haenel.co',
    )
