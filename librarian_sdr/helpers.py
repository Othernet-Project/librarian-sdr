import os
import stat
import logging
import subprocess

from librarian.core.exts import ext_container as exts


ONDD_SERVICE = 'ondd'
SDR_SERVICE = 'sdr100'


def save_sdr(sdr, path):
    """
    Saves a file-like obj `sdr` at location `path` and sets file permissions.
    """
    if os.path.exists(path):
        logging.info('Replacing existing sdr binary')
        os.remove(path)
    logging.debug('Saving sdr binary at path %s', path)
    try:
        sdr.save(path)
        # Set the executable to be world executable
        # 755 => rwxr-xr-x
        mode = (stat.S_IRWXU |
                stat.S_IRGRP |
                stat.S_IXGRP |
                stat.S_IROTH |
                stat.S_IXOTH)
        os.chmod(path, mode)
    except Exception:
        logging.exception('Exception while saving SDR binary at %s', path)
        raise


def restart_tuners():
    """ Restarts SDR & ONDD by restarting the processes."""
    exts.tasks.schedule(_restart_tuners)


def _restart_tuners():
    restart_service(ONDD_SERVICE)
    restart_service(SDR_SERVICE)


def restart_service(name):
    logging.debug("Restarting service: '%s'", name)
    try:
        return subprocess.call(['service', name, 'restart'])
    except Exception:
        logging.exception("Exception while restarting service '%s'", name)
        return 1
