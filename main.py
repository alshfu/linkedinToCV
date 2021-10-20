from linkedinScraper import Person


if __name__ == '__main__':
    login = 'llkljl'
    password = ''
    url_page = ''
    person = Person(login_name=login, pwd=password, url=url_page)
    # person.get_profile_image()
    person.create_json_file()
    person.driver_close()
