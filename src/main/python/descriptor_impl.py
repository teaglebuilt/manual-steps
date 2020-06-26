#!/usr/bin/env jython

import hudson.util.FormValidation as FormValidation

def descriptor_impl():
    extension.load()

def configure(request, form_data):
    print(form_data)
    extension.french = form_data.getBoolean("french")
    extension.save()
    return extension.superConfigure(request, form_data)

def is_applicable(_class):
    return True
    
def get_display_name():
    return "Execute Manual Steps builder"

def do_check_name(value):
    print(dir(extension))
    if len(value) == 0:
        return FormValidation.error("Please set a name")
    if len(value) < 4:
        print("triggered")
        return FormValidation.warning("Isn't the name too short?")
    return FormValidation.ok()

def perform(build, launcher, listener):
    print(">>")
    if extension.getDescriptor().french:
        listener.getLogger().println("Bonjour, " + extension.name + "!")
    else:
        listener.getLogger().println("Hello, " + extension.name + "!")
    return True