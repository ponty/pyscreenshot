import logging
import subprocess

class Process():
    '''subprocess wrapper'''
    def call(self, cmd):
        '''start command and wait until it ends'''
        self.cmd = cmd
        logging.debug('starting command: %s' % str(cmd))
        self.process = subprocess.Popen(cmd,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=1
                                        )
        (self.stdout, self.stderr) = self.process.communicate()
        self.returncode = self.process.returncode
        logging.debug('process has ended, return code=' + str(self.returncode))
        logging.debug('stdout:\n' + self.stdout)
        logging.debug('stderr:\n' + self.stderr)
