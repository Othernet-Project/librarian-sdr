from bottle_utils import form
from bottle_utils.i18n import lazy_gettext as _


class SDRForm(form.Form):
    sdr_binary = form.FileField(
        _("SDR Executable"),
        validators=[
            form.Required(messages={
                # Translators, shown as a prompt to user during setup wizard
                # step.
                'required': _('Please select the SDR executable')
            })
        ]
    )
