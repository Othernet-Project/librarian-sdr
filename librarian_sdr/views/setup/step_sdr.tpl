<%inherit file='/setup/setup_base.tpl'/>

<%namespace name="forms" file="/ui/forms.tpl"/>

<%block name="step_title">
    <span class"icon icon-radio"></span>
    ## Translators, used as step title during setup wizard, in demodulator 
    ## installation step
    ${_('Demodulator Installation')}
</%block>

<%block name="step_desc">
    ## Translators, used as a prompt to the user during setup wizard, in 
    ## demodulator installation step
    <p>${_('Please select the demodulator executable.')}</p>
</%block>

<%block name="step">
## Translators, used during demodulator installation step in setup wizard, to 
## inform the user why they have to supply the executable
<p class="o-field-help-message"> ${_('The software demodulator must be installed separately. Please upload the demodulator executable.')} </p>

<div id="sdr-form">
    ${forms.form_errors([message]) if message else ''}
    ${forms.field(form.sdr_binary)}
    <button type="submit">
        ${_('Upload')}
    </button>
</div>
</%block>
