import urllib, re

def wget(url):
    ''' Try to retrieve a webpage via its url, and return its contents'''
    print '[*] wget()'
    # Pass the url into a file
    url_file = urllib.urlopen(url)
    # Read the content of the webpage
    page = url_file.read()
    # Return the content of the webpage
    return page

def find_emailAddr(web_page):
    '''find and print email-addresses on a webpage'''
    print '\n[Type: Emails]'
    # regex to match on email addresses
    emails = re.findall(r'([\d\w\.-_]+@[\w\d\.-_]+\.\w+)', web_page)
    # sort and print the phone numbers
    emails.sort()
    print '[+]', str(len(emails)), 'Emails found:'
    for found_emails in emails:
        print found_emails

def find_phoneNum(web_page):
    '''find and print phone numbers on a webpage'''
    print "\n[Type: Phone Numbers]"
    # regex to match on phone numbers
    phoneNumbers = re.findall(r'^(?:\b07\d{9}\b)|(?:\b07\d{3}.\d{6}\b)|(\+44\d{10}$)|(\+44\d{4}.\d{6}$)|(?:\b07\d{2}.\d{3}.\d{4}\b)|(\+44\d{3}.\d{3}.\d{4}$)', web_page, re.MULTILINE)
    # sort and print the phone numbers
    phoneNumbers.sort()
    print '[+]', str(len(phoneNumbers)), 'Phone Numbers found:'
    for found_number in phoneNumbers:
        print found_number


def main():
    web_page = wget('https://fakenumber.org/generator/mobile')
    find_emailAddr(web_page)
    find_phoneNum(web_page)


if __name__ == '__main__':
    main()

