from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']


def main():
    """Shows basic usage of the Admin SDK Directory API.
    Prints the emails and names of the first 10 users in the domain.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('admin', 'directory_v1', credentials=creds)

    # Call the Admin SDK Directory API
    print('Getting a list of members in the test group')
    new_member = {
        # "status": "A String", # Status of member (Immutable)
        "kind": "admin#directory#member", # Kind of resource this is.
        "delivery_settings": "ALL_MAIL", # Delivery settings of member
        # "id": "A String", # The unique ID of the group member. A member id can be used as a member request URI's memberKey. Unique identifier of group (Read-only) Unique identifier of member (Read-only)
        # "etag": "A String", # ETag of the resource.
        "role": "MEMBER", # Role of member
        "type": "USER", # Type of member (Immutable)
        "email": "guerillarwolfgang@gmail.com" # Email of member (Read-only)
    }
    service.members().insert(groupKey='test@msgic.org', body=new_member).execute()
    # members = results.get('members', [])

    # if not members:
    #     print('No members in the test group.')
    # else:
    #     print('\nMembers:')
    #     for member in members:
    #         print(u'{0} ({1})'.format(member['email'],
    #                                   member['role']))


if __name__ == '__main__':
    main()