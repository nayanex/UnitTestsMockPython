import unittest
import platform
import shutil
import os
from mock import MagicMock
from mock import Mock
from mock import patch
from mock import create_autospec
from osfilesystem import OsFileSystem

class OsFileSystemTest(unittest.TestCase):
    osfilesys = OsFileSystem()

    @unittest.skip("WIP")
    @patch.object(platform, 'system')
    def test_returns_bat_on_windows(self, system_method): 
        system_method.return_value = 'Windows'   
        self.assertEquals(self.osfilesys.system_script_extension(), '.bat')
        self.assertEquals(self.osfilesys.system_script_extension('Windows'), '.bat')

    @unittest.skip("WIP")
    @patch.object(platform, 'system')
    def test_returns_command_on_darwin(self, system_method):
        system_method.return_value = 'Darwin' #the Mac kernel
        self.assertEquals(self.osfilesys.system_script_extension(), '.command')
        self.assertEquals(self.osfilesys.system_script_extension('Darwin'), '.command')
    
    @unittest.skip("WIP")
    @patch.object(platform, 'system')
    def test_returns_sh_on_linux(self, system_method):
        system_method.return_value = 'Linux'
        self.assertEquals(self.osfilesys.system_script_extension(), '.sh')
        self.assertEquals(self.osfilesys.system_script_extension('Linux'), '.sh')

    @unittest.skip("WIP")
    @patch.object(platform, 'system')
    def test_returns_sh_by_default(self, system_method):
        system_method.return_value = 'Random OS'
        self.assertEquals(self.osfilesys.system_script_extension(), '.sh')
        self.assertEquals(self.osfilesys.system_script_extension('Random OS'), '.sh')

class SystemSpecificUnzippingTests(unittest.TestCase):
    osfilesys = OsFileSystem()
    dest_dir = os.path.join(os.path.dirname(__file__), 'extract_dir')

    def tearDown(self):
        shutil.rmtree(self.dest_dir, ignore_errors=True)

    def test_raises_exception_on_invalid_zipfile(self):
        self.assertRaises(Exception, self.osfilesys.system_specific_unzipping, __file__, self.dest_dir)

    # We can chain multiple patch.objects for one test. They follow a LIFO sequence: the top patch.object corresponds to the last parameter, 
    # the second topmost corresponds to the second to the last parameter etc.    
    @patch.object(os, 'mkdir')
    @patch.object(os.path, 'exists')
    def test_if_dest_dir_created(self, exists_method, mkdir_method):
        exists_method.return_value = False
        try:
            self.osfilesys.system_specific_unzipping('nonexistent.zip', self.dest_dir)
        except:
            pass
        mkdir_method.assert_called_once_with(self.dest_dir)




