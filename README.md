# Automated_EmailSender

## Summary
This program lets you send a designed email message along with a list of attachments to every client inside a email list.

## Usage
Cd into the repo
- Save any email attachment files into `./attachments`.
- Save any email message files into `./content`.
- Goto https://developers.google.com/gmail/api/quickstart/python/ and click on `Enable the Gmail API` to generate a copy of your `credentials.json`. Save the file generated under `./credentials`.
- Add all your clients into the client list in `client_list.csv`.
- Execute `./src/automate.py` and follow the instructions shown in console.