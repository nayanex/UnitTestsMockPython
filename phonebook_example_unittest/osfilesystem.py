import os
import platform
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED, is_zipfile, BadZipfile

class OsFileSystem:

    def __init__(self):
        self.entries = {}
        self.SCRIPT_FILE = os.path.basename(__file__).split('.')[0]
        self.SCRIPT_PATH = os.path.dirname(__file__) 
        self.BKP_TMP_DIR = os.path.join(self.SCRIPT_PATH, "temp_dir")
        self.COMPRESSED_FILE_PATH = self.BKP_TMP_DIR + ".tgz"

    def system_script_extension(self, system=None):
        """
        The extension for the one script that could be considered "the os script" for the given system..
        """
        exts = {
            "windows": ".bat",
            "darwin": ".command",
            "linux": ".sh",
        }
        system = system or platform.system()
        return exts.get(system.lower(), ".sh")

    def is_windows(self, system=None):
        system = system or platform.system()
        return system.lower() == "windows"

    def is_osx(self, system=None):
        system = system or platform.system()
        return system.lower() in ["darwin", "macosx"]
    
    def system_specific_scripts(self, system=None):
        """
        All scripting types for that platform, that wouldn't be recognized
        on ALL other platforms.
        """
        if self.is_windows(system):
            return [".bat", ".vbs"]
        elif self.is_osx(system):
            return [".command", ".sh"]
        else:
            return [".sh"]

    def _default_callback_unzip(self, afile, fi, nfiles):
        """
        Private (default) callback function for system_specific_unzipping
        """
        if fi>0 and fi%round(nfiles/10)==0:
            pct_done = round(100. * (fi + 1.) / nfiles)
            sys.stdout.write(" %d%%" % pct_done)
            sys.stdout.flush()

        if (not self.is_windows()) and (os.path.splitext(afile)[1] in self.system_specific_scripts() or afile.endswith("manage.py")):
            sys.stdout.write("\tChanging perms on script %s\n" % afile)
    
    def system_specific_unzipping(self, zip_file, dest_dir, callback=_default_callback_unzip):
        """
        # unpack the inner zip to the destination
        """

        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)

        if not is_zipfile(zip_file):
            raise Exception("bad zip file")

        zip = ZipFile(zip_file, "r")
        nfiles = len(zip.namelist())

        for fi, afile in enumerate(zip.namelist()):
            if callback:
                callback(afile, fi, nfiles)

            zip.extract(afile, path=dest_dir)
            # If it's a unix script or manage.py, give permissions to execute
            if (not self.is_windows()) and (os.path.splitext(afile)[1] in self.system_specific_scripts() or afile.endswith("manage.py")):
                os.chmod(os.path.realpath(dest_dir + "/" + afile), 0775)

    def print_stuff(self):
        print __file__
        print os.path.join(os.path.dirname(__file__), '..')
        print os.path.dirname(os.path.realpath(__file__))
        print os.path.abspath(os.path.dirname(__file__))
        print os.path.join(self.SCRIPT_PATH, "temp_dir")
        print self.SCRIPT_FILE
        print self.BKP_TMP_DIR
        print os.path.basename(__file__)
        print self.COMPRESSED_FILE_PATH

    