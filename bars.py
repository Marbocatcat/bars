import os
import logging
from shutil import copytree, ignore_patterns

# Set logging configurations.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s \
                    - %(message)s')


# Ignore Path patterns.
def _logpath():
    ignore = ['*.py', '*.so', '*.cfg', '*.h', '*.exe', '*.csh', '*.fish',
     '*.js', '*.css', '*.json', '*.ps1', '*.pyo', '*.xml', '*.rst', '*.c', '*.tmpl']
    for patterns in ignore:
        return patterns


logging.debug('Start of the loop.')


def print_targets():
    # Set HOME environment variable /home/bobcat.
    Home = os.getenv('HOME')
    # Put target directories in a list.
    target = ['Desktop', 'Documents', 'Downloads', 'Projects', 'Pictures']

    # Loop starts.
    for targets in target:
        # Create target and destination path.
        destination = f'{Home}/bars/{targets}'
        targets = f'{Home}/{targets}'
        # Add the logging and copytree ignore patterns.
        # Main logic is here.
        logging.debug(f'Copying {copytree(targets, destination, ignore=ignore_patterns(_logpath()))}')
    else:
        # Raise this exception if error occured.
        raise Exception('An Error Occured!')


logging.debug('End of the loop.')


def main():
    try:
        print_targets()
    # Grab exception from the Raise on the print_targets loop.
    except Exception as err:
        print('An exception happend: ' + str(err))


# Run main.
main()
