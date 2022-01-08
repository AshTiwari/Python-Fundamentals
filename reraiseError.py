"""Re-raise an error in Exception-Handling."""

import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    # allow us to gracefully handle an exception.
    except (ValueError, TypeError) as e:
        # stderr outputs the message in form of an error.
        print(f"Conversion Error: {str(e)}",file=sys.stderr)
        # allow us to re-raise the error currently being handled.
        raise
if __name__ == "__main__":
    convert("nine")
