"""Platform Specific Code"""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character string."""
        return msvcrt.getch()

# for mac and Linux
except ImportError:
    import sys
    import tty
    import termios

    def getKey():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys = stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

    # if either of Unix-specific tty or termios are not found,
    # we allow the import error to propogate from here.
