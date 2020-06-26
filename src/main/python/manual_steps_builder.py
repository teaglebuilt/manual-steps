#!/usr/bin/env jython

def perform(build, launcher, listener):

    file = build.getLogFile()
    log_file = open(str(file), "r")
    while True:
        print(dir(log_file))
        text = log_file.read()
        line = log_file.readline()
        print(dir(text))
        print(text)
        if line.find("Finished: SUCCESS") or line.find("Finished: FAILURE"):
            print("finished")
            break


    if extension.getDescriptor().french:
        listener.getLogger().println("Bonjour, " + extension.name + "!")
    else:
        listener.getLogger().println("Hello, " + extension.name + "!")
    return True
