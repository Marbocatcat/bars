import os
import shutil
import logging

# Set logging configurations.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s \
                    - %(message)s')


logging.debug('Start of the loop.')


def print_targets():
    # Set HOME environment variable /home/bobcat.
    Home = os.getenv('HOME')
    # Put target directories in a list.
    target = ['Desktop', 'Documents'] #, 'Documents', 'Downloads', 'Projects', 'Pictures']
    # Ignore the following extensions.
    ignore = ['.py', '.pyc', '.so', '.cfg', '.h', '.exe', '.csh', '.fish',
     '.js', '.css', '.json', '.ps1', '.pyo', '.xml', '.rst', '.c', '.tmpl']

    # Loop starts.
    for targets in target:
        # Create target path by concatenating the home directory and target /
        # dirs.
        dir_path = f'{Home}/{targets}'
        for root, dir, file in os.walk(dir_path):
            for entries in file:
                if not entries.endswith(tuple(ignore)):
                    destination = f'{Home}/bars'
                    print(f'Copying {entries} to {destination}')
                # source = os.path.join(root, entries)
                # print(f'Copying {source} to {destination}')
                # logging.debug('Copying ' + shutil.copy(source, destination) + f' to {destination}')
    logging.debug('End of the loop.')


print_targets()
