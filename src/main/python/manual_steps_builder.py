#!/usr/bin/env jython

def perform(build, launcher, listener):

    file = build.getLogFile()
    log_file = open(str(file), "r")
    text = log_file.read()
    log_file.close()

    if extension.getDescriptor().french:
        listener.getLogger().println("Bonjour, " + extension.name + "!")
    else:
        listener.getLogger().println("Hello, " + extension.name + "!")
    return True
