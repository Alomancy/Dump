import urllib2
import re


CodeValues = [200, 302, 403, 406]

def wget(url):
    # Try to retrieve a web page via its url, and return its contents
    print '[*] wget()'
    # Pass the url into a file
    url_file = urllib2.urlopen(url)
    # Read the content of the webpage
    page = url_file.read()
    # Return the content of the webpage
    return page

def find_wordpress(web_page):
    print '\n[Type: /wordpress/]'
    # regex to match on wp-content
    content = re.findall(r'(wordpress)', web_page)
    content.sort()
    print '[+]', str(len(content)), 'wordpress found:'
    for found_content in content:
        print found_content


def find_wpcontent(web_page):
    print '\n[Type: /wp-content/]'
    # regex to match on wp-content
    content = re.findall(r'(/wp-content/)', web_page)
    content.sort()
    print '[+]', str(len(content)), 'wp-content found:'
    for found_content in content:
        print found_content


def find_wpinclude(web_page):
    print '\n[Type: /wp-include/]'
    content = re.findall(r'/wp-include/', web_page)
    content.sort()
    print '[+]', str(len(content)), 'wp-content found:'
    for found_content in content:
        print found_content

def find_license(url):
    print '\n[Type: License]'
    license_page = urllib2.urlopen(url + "/license.txt")
    license = license_page.read()
    content = re.findall(r'WordPress', license)
    for found_content in content:
        print found_content


def find_wpadmin(url):
    print '\n[Type: WP-Admin]'
    wpadmin = urllib2.urlopen(url + "/wp-admin/")
    if wpadmin.getcode() in CodeValues:
        print '\nlogin Screen Detected ' + str(wpadmin.getcode())


def find_wplogin(url):
    print '\n[Type: WP-Login]'
    wplogin_page = urllib2.Request(url + "/wp-login.php")
    wplogin_page.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    wplogin_code = urllib2.urlopen(wplogin_page)
    wplogin = wplogin_code.read()
    if wplogin_code.getcode() in CodeValues:
        print '\nlogin Screen Detected' + str(wplogin_code.getcode())
    wpversion = re.findall(r'(css\?ver=)(.*)', wplogin)
    wpversion.sort()
    print '[+]', str(len(wpversion)), 'WordPress Version found:'
    for found_wpversion in wpversion:
        print found_wpversion
    piVersion = re.findall(r'(.*)(js\?ver=)(.*)', wplogin)
    piVersion.sort()
    print '[+]', str(len(wpversion)), 'Plugin & Versions found:'
    for found_piVersion in piVersion:
        print found_piVersion

def find_wptrackback(url):
    print '\n[Type: wp-trackback.php]'
    wptrackback = urllib2.urlopen(url + "/wp-trackback.php")
    if wptrackback.getcode() in CodeValues:
        print '\nlogin Screen Detected' + str(wptrackback.getcode())


def get_version(url):
    print '\n[Type: Version]'
    readme_page = urllib2.urlopen(url + "/readme.html")
#    readme = readme_page.read()
    match = re.findall(r'Version ([0-9]+\.[0-9]+\.?[0-9]*)', readme_page.read())
    for matches in match:
        print matches


def meta_generator(web_page):
    print '\n[Type: Version]'
    content = re.findall(r'(generator)(.*)', web_page)
    content.sort()
    print '[+]', str(len(content)), 'Version found:'
    for found_content in content:
        print found_content



def main():
    url = 'http://www.puntocreativo.com.gt'
    web_page = wget(url)
    find_wordpress(web_page)
    find_wpcontent(web_page)
    find_wpinclude(web_page)
    find_license(url)
    find_wpadmin(url)
    find_wplogin(url)
    find_wptrackback(url)
    get_version(url)
    meta_generator(web_page)


if __name__ == '__main__':
    main()

