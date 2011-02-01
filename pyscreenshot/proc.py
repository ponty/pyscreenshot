import logging
import subprocess

log=logging.getLogger(__name__)
class Process():
    '''subprocess wrapper'''
    def call(self, cmd):
        '''start command and wait until it ends'''
        self.cmd = cmd
        log.debug('starting command: %s' % str(cmd))
        self.process = subprocess.Popen(cmd,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=1
                                        )
        (self.stdout, self.stderr) = self.process.communicate()
        self.returncode = self.process.returncode
        log.debug('process has ended, return code=' + str(self.returncode))
        log.debug('stdout:\n' + self.stdout)
        log.debug('stderr:\n' + self.stderr)
        return self.returncode
    