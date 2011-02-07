import logging
import shlex
import subprocess

log = logging.getLogger(__name__)
#log=logging

class Process():
    '''
    :mod:`subprocess.Popen` wrapper
    '''
    
    def __init__(self, cmd=None):
        '''
        :param cmd: start call(cmd)
        '''
        self.process = None
        self.stdout = None
        self.stderr = None
        self.cmd = None
        if cmd:
            self.call(cmd)
        
    @property
    def pid(self):
        if self.process:
            return self.process.pid
        
    @property
    def return_code(self):
        if self.process:
            return self.process.returncode

    def _set_cmd(self, cmd):
        if not hasattr(cmd, '__iter__'):
            cmd = shlex.split(cmd)
            
        self.cmd = cmd
        log.debug('starting command: %s' % str(cmd))
        log.debug('" ".join(cmd)= %s' % ' '.join(cmd))
        return cmd

    def _log_output(self):
        log.debug('return code=' + str(self.return_code))
        log.debug('stdout:\n' + self.stdout)
        log.debug('stderr:\n' + self.stderr)
    
    def check(self, cmd, exception=None):
        '''similar as call
        
        Returns True if there is no error:
         - no exception
         - returncode=0
        
        :param cmd: string ('ls -l') or list of strings (['ls','-l']) 
        :param exception: raise exception by error
        :rtype: bool
        '''
        detail=None
        try:
            ret = self.call(cmd)
            ok = ret == 0
        except OSError as detail:
            log.debug('OSError exception')
            ok = False
        if not ok and exception:
            msg='check failed! \n OSError:%s \n cmd:%s \n return code:%s \n stderr:%s' % (detail, self.cmd, self.return_code, self.stderr)
            raise exception(msg)
        return ok
    
    def call(self, cmd):
        '''
        start command and wait until it ends
        
        shell is not supported (shell=False)
        
        Returns return_code.
        stdout is in self.stdout
        stderr is in self.stderr
        
        :param cmd: string ('ls -l') or list of strings (['ls','-l']) 
        :rtype: int
        '''
        
        cmd = self._set_cmd(cmd)
        
        self.process = subprocess.Popen(cmd,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        #shell=1
                                        )
        (self.stdout, self.stderr) = self.process.communicate()
        log.debug('process has ended')
        self._log_output()
        return self.return_code

    def start(self, cmd):
        '''
        start command and does not wait for it
        
        :param cmd: string ('ls -l') or list of strings (['ls','-l']) 
        '''

        cmd = self._set_cmd(cmd)

        self.process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              #shell=1,
                              )
        log.debug('process was started (pid:%s)' % (str(self.process.pid),))


    def is_alive(self):
        if self.process:
            return self.process.poll() is None
        else:
            return False
        
    def wait(self):
        if self.process:
            self.process.wait()
            log.debug('process has ended')
            self.stdout = self.process.stdout.read()
            self.stderr = self.process.stderr.read()
            self._log_output()
            
    def stop(self):
        '''
        kill process by sending SIGTERM

        does not work with shell=True
        '''
        
        
        log.debug('stopping process (pid:%s cmd:"%s")' % (str(self.pid), self.cmd))
        if self.process:
            if self.is_alive():
                log.debug('process is active -> sending SIGTERM')
                #os.kill(self.process.pid, signal.SIGKILL)
                self.process.terminate()
            else:
                log.debug('process was already stopped')
            self.wait()
        else:
            log.debug('process was not started')
            
        return self.return_code
    
