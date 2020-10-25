from Completer.ConfirmCompleter import ConfirmCompleter
from Completer.SuiteCompleter import SuiteCompleter
from functions import *

stage_number = input("what is branch number?\n > ")
integer_input(stage_number)

confirmCompleter = ConfirmCompleter()
suiteCompleter = SuiteCompleter()

question("Do you want run all tests? (y or n)\n > ", confirmCompleter)
question("Do you want run a specific suite? (acceptance, api, integration)\n > ", suiteCompleter)



