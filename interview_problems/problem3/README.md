# magnificent

A new challenger appears!

## Installation

 1. Install Python
 2. pip install twisted
 3. python server.py
 4. Okay, now you're running magnificent!
 5. Visit http://localhost:12345 in a web browser or something.
 6. It should throw a verbose error, or return "Magnificent!".

## Now it's your turn.

Magnificent fails 25% of the time. We want to write a service to monitor the health of Magnificent Server.

Your user is a busy cloud system administrator. She doesn't want to run your app and look at it all the time.
She wants it to run in the background.

She has tools to monitor log files, so that is one method you can use to get her attention.

### Requirements

* This is a daemon, or a "service", if you prefer calling it that. Once started,
  it should run forever.
* It should check Magnificent Server frequently - at least several times a minute.
* The service has to indicate how healthy Magnificent Server has been, over the last little while.
* The service should also tell our system administrator if Magnificent Server has not been responding at all.
* This should go without saying, but you can't use anyone else's code, unless it's under [an open-source license](http://opensource.org/licenses).
  If you need to copy a snippet from Stack Overflow or some similar site, that's okay. But you should 
  be the primary author of, and understand, all the code you submit.

### Platform

Sauce Labs' services are usually written in Python running on Linux.

But please use the language and environment where you are the strongest.
For instance, you could use any of these:

    Java
    Node.JS               Android
    Objective-C           iOS
    Perl                  Linux
    PHP                   Mac OS X
    Python
    Ruby
    Shell scripts

Please do not use any of these, as we do not have the expertise to
evaluate solutions in these environments:

    x86 Assembly
    Intercal
    Plan 9 from Bell Labs
    Coldfusion
    Malbolge
    Turbo Pascal
    NeXTSTEP
    Visual Basic for Applications


## Judging

This is what we look for.

* **Correctness**. Does it do what we asked?
* **Simplicity.** Does the design match the task?
* **Clarity.** Can any competent programmer easily understand what's going on?
* **Generality.** It shouldn't be all hardcoded, but don't make it too abstract either.
* **Tests and testability.** It would be really great if you have tests. If not, it should be
  at least possible to test this.
* **Documentation:**
  * Can any competent programmer get this running?
  * Is there *just enough* documentation, to tell us *why* the program works this way?
