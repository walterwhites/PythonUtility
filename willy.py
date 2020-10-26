#!/usr/bin/env python

from Completer.ConfirmCompleter import ConfirmCompleter
from Completer.SuiteCompleter import SuiteCompleter
from Command.Startbuild.Startbuild import Startbuild
from Command.Startbuild.functions import *

startbuild = Startbuild()
os.system('clear')
stage_number = input("Hey mate, what is your branch number? \n"
                     "stage -> 0 \n"
                     "stage-1 -> 1 \n"
                     "stage-oc-4444 -> 4444 \n > ")
startbuild.setOption("s", integer_input(stage_number))
confirmCompleter = ConfirmCompleter()
suiteCompleter = SuiteCompleter()

suiteQs = question("Do you want run all tests? (y or n)", confirmCompleter)
if suiteQs in "n":
    suite = question("What test you wanna run? \n"
                     "ps: you can use autocompletion", suiteCompleter)
    startbuild.setOption("p", suite)


branchQs = question("Use master branch (y or n)?", confirmCompleter)
if branchQs in "n":
    branch = str(input("Which branch you wanna use? \n > "))
    startbuild.setOption("b", branch)

s = startbuild.getOption("s").getValue(startbuild.getOption("s"))
p = startbuild.getOption("p").getValue(startbuild.getOption("p"))
b = startbuild.getOption("b").getValue(startbuild.getOption("b"))

p = p if p is not None else "All"
b = b if b is not None else "master"

print(s)
print(p)
print(b)
run = question("Can you confirm ? (y or n) \n"
         "stage = " + s +
         "\ntests = " + p +
         "\nbranch = " + b, confirmCompleter)

startbuild.build()
print(startbuild.getCommand())

if run in "y":
    startbuild.launchCommand(startbuild.getCommand())