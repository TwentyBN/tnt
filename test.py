import os
import tempfile
import shutil
import stat
import unittest

import setup


def remove_nvidia_smi_from_path(target_path):
    return ':'.join([directory for directory in target_path.split(':')
                     if os.path.exists(directory) and
                     'nvidia-smi' not in os.listdir(directory)])


class TestHasGPU(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix='tnt-test-')
        filename = os.path.join(self.tempdir, 'nvidia-smi')
        with open(filename, 'w') as fp:
            fp.write('mock nvidia-smi')
        new_mode = stat.S_IXUSR ^ stat.S_IRUSR ^ stat.S_IWUSR
        os.chmod(filename, new_mode)
        self.old_path = os.environ['PATH']

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        os.environ['PATH'] = self.old_path

    def test_has_gpu_succeeds(self):
        os.environ['PATH'] += ':{}'.format(self.tempdir)
        self.assertTrue(setup.hasgpu())

    def test_has_gpu_fails(self):
        os.environ['PATH'] = remove_nvidia_smi_from_path(os.environ['PATH'])
        self.assertFalse(setup.hasgpu())
