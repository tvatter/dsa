import sys
import syslog

# The initial class.


class Logger(object):
  def __init__(self, file):
    self.file = file

  def log(self, message):
    self.file.write(message + '\n')
    self.file.flush()


# New design direction: filtering messages.


class FilteredLogger(Logger):
  def __init__(self, pattern, file):
    self.pattern = pattern
    super().__init__(file)

  def log(self, message):
    if self.pattern in message:
      super().log(message)


# It works.
if __name__ == 'main':
  f = FilteredLogger('Error', sys.stdout)
  f.log('Ignored: this is not important')
  f.log('Error: but you want to see this')
