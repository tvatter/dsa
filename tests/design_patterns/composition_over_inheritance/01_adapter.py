import os
import socket
import sys
import syslog

if os.isatty(sys.stdout.fileno()):
  dirname = os.getcwd() + '/tests/design_patterns/composition_over_inheritance'
else:
  dirname = os.path.dirname(__file__)
sys.path.append(dirname)

from logger import FilteredLogger


class FileLikeSocket:
  def __init__(self, sock):
    self.sock = sock

  def write(self, message_and_newline):
    self.sock.sendall(message_and_newline.encode('ascii'))

  def flush(self):
    pass


class FileLikeSyslog:
  def __init__(self, priority):
    self.priority = priority

  def write(self, message_and_newline):
    message = message_and_newline.rstrip('\n')
    syslog.syslog(self.priority, message)

  def flush(self):
    pass


if __name__ == 'main':
  sock1, sock2 = socket.socketpair()

  fs = FileLikeSocket(sock1)
  logger = FilteredLogger('Error', fs)
  logger.log('Warning: message number one')
  logger.log('Error: message number two')

  print('The socket received: %r' % sock2.recv(512))
