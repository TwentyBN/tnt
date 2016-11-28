import sys
import os
from distutils.core import setup
import pip


class UnsupportedPlatformException(Exception):
    pass


def install_tensorflow():
    python_version = pythonversion()
    print(python_version)
    has_gpu = hasgpu()
    platform_name = platform()
    install_url = build_url("0.11.0",
                            python_version,
                            "gpu" if has_gpu else "cpu",
                            platform_name,
                            )
    pip.main(['install', '-U', install_url])


def pythonversion():
    return sys.version_info[:2]


def hasgpu():
    return not os.system('which nvidia-smi > /dev/null')


def platform():
    platform_name = sys.platform
    if platform_name.startswith('linux'):
        return 'linux'
    elif platform_name.startswith('darwin'):
        return 'mac'
    else:
        raise UnsupportedPlatformException(
            'Only linux and mac are supported, but you are on "{}"'
            .format(platform_name))


def create_wheeltags(platform_name, python_version):
    if platform_name == 'mac':
        return 'py{}-none-any'.format(python_version[0])
    elif platform_name == 'linux':
        cpstring = '{}{}'.format(python_version[0], python_version[1])
        if cpstring == '27':
            return 'cp27-none-linux_x86_64'
        else:
            return 'cp{}-cp{}m-linux_x86_64'.format(cpstring, cpstring)


def build_url(tf_version, python_version, processing_unit, platform_name):
    kwargs = {
        'platform_name': platform_name,
        'processing_unit': processing_unit,
        'tf_version': tf_version,
        'wheeltags': create_wheeltags(platform_name, python_version)
    }
    return ('https://storage.googleapis.com/tensorflow/'
            '{platform_name}/{processing_unit}/'
            'tensorflow-{tf_version}-{wheeltags}.whl'
            .format(**kwargs))


if __name__ == '__main__':
    install_tensorflow()

    setup(
        name='tnt',
        version='0.0.0',
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
