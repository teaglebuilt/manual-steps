# Manual Steps

### Jenkins Plugin

A plugin originally created to handle RobotFrameworks Dialogs Library.

The original use case is to enable jenkins to handle automated tests that pause to wait for user interaction / input. This is common in end to end automation with devices involved in the software / product.

This plugin would allow these automated regression tests to be deployed for remote access along with all the other benefits jenkins has to offer. The first goal of this plugin is to listen for a dialog to be triggered from the DialogsLibrary. After this has been completed. I will look into listening for an event that is not dependent on a framework.
