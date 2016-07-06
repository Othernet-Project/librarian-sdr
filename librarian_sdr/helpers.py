import os
import stat
import logging
import subprocess

from librarian.core.exts import ext_container as exts


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


def bootup_sdr():
    exts.tasks.schedule(start_sdr,
                        args=(exts.config['sdr.sdr_restart_command'],
                              exts.config['sdr.ondd_restart_command']))


def start_sdr(sdr_command, ondd_command):
    ondd_alive = exts.ondd.ping()
    if not ondd_alive:
        # ONDD needs to be up before sdr100, because sdr100 does not connect
        # with ONDD correctly otherwise
        logging.info('Could not connect to ONDD. Starting ONDD')
        run_command(ondd_command)
    logging.info('Restarting sdr100')
    run_command(sdr_command)


def run_command(command):
    try:
        exit_code = subprocess.call(command, shell=True)
        if exit_code:
            logging.debug("'%s' returned %s", command, exit_code)
        return exit_code
    except Exception:
        logging.exception("Exception while running '%s'", command)
        raise
