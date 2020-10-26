from Completer.Completer import Completer


class SuiteCompleter(Completer):
    choices = ["acceptance", "api", "integration",
               "api/Analytics", "api/Organization", "api/TeamOrganization", "api/UserCreateFinancialAid",
               "api/LearningContent", "api/Student", "api/UserAvailability", "api/UserExpectedBenefits",
               "api/UserSupport", "api/Offers", "api/TeamInvitations", "api/UserBirthInformation",
               "api/UserOrganization", "acceptance/Mentorship/", "acceptance/Partnerships/", "acceptance/visual/"]

    def __init__(self):
        super().__init__()