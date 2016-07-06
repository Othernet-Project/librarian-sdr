import os
import stat
import logging


def save_sdr(sdr, path):
    """
    Saves a file-like obj `sdr` at location `path` and sets file permissions.
    """
    if os.path.exists(path):
        logging.info('Replacing existing sdr binary')
        os.remove(path)
    logging.debug('Saving sdr binary at path %s', path)
    sdr.save(path)
    # Set the executable to be world executable
    # 755 => rwxr-xr-x
    mode = (stat.S_IRWXU |
            stat.S_IRGRP |
            stat.S_IXGRP |
            stat.S_IROTH |
            stat.S_IXOTH)
    os.chmod(path, mode)
