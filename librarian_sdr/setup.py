import os
import logging

from bottle import request
from bottle_utils.i18n import lazy_gettext as _
from librarian.core.exts import ext_container as exts

from .forms import SDRForm
from .helpers import save_sdr, bootup_sdr


def context(successful=False, form=None, message=None):
    form = form or SDRForm()
    return dict(successful=successful, form=form,
                message=message, step_multipart=True)


class SDRStep(object):
    name = 'sdr'
    index = 25
    template = 'setup/step_sdr.tpl'

    @staticmethod
    def test():
        path = exts.config['sdr.binary_path']
        return not os.path.exists(path)

    @staticmethod
    def get():
        return dict(form=SDRForm(), step_multipart=True)

    @staticmethod
    def post():
        form = SDRForm(request.files)
        valid = form.is_valid()
        if valid:
            uploaded_binary = form.processed_data['sdr_binary']
            try:
                path = exts.config['sdr.binary_path']
                save_sdr(uploaded_binary.file, path)
                bootup_sdr()
                return dict(successful=True)
            except:
                logging.exception('Exception during SDR installation')
                # Translators, shown when installation of SDR executable failed
                # during setup wizard step.
                return context(message=_('Demodulator Installation failed'))
        else:
            # Translators, shown as a prompt to user during setup wizard step.
            return context(message=_('Please select the demodulator executable'))
