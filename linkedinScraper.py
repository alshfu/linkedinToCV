import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json
import codecs


class Person:
    def __init__(self, login_name=None, pwd=None, url=None):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.get_person_page()
        self.login = login_name
        self.password = pwd

    def get_person_page(self):
        self.driver.get(self.url)

    def do_login(self):
        sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@class="authwall-join-form__form-toggle form-toggle"]').click()
            self.driver.find_element(By.ID, 'session_key').send_keys(self.login)
            self.driver.find_element(By.ID, 'session_password').send_keys(self.password)
            self.driver.find_elements(By.CLASS_NAME, 'sign-in-form__submit-button')[0].click()
        except selenium.common.exceptions.NoSuchElementException:
            self.driver.find_elements(By.CLASS_NAME, 'form-toggle')[1].click()
            self.driver.find_element(By.ID, 'login-email').send_keys(self.login)
            self.driver.find_element(By.ID, 'login-password').send_keys(self.password)
            self.driver.find_element(By.ID, 'login-submit').click()
        sleep(5)
        edit_public = self.driver.find_element(By.XPATH, '//*[@class="relative display-flex justify-space-between"]')
        url = edit_public.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
        self.url = url
        self.get_person_page()

    def get_name(self) -> str:
        try:
            name = self.driver.find_elements(By.CLASS_NAME, 'top-card-layout__title')[0].text
            print('name: ' + name)
            return name
        except IndexError:
            self.do_login()
            sleep(5)
            name = self.driver.find_elements(By.CLASS_NAME, 'top-card-layout__title')[0].text
            print('name: ' + name)
            return name

    def get_headline(self) -> str:
        headline = self.driver.find_elements(By.CLASS_NAME, 'top-card-layout__headline')[0].text
        print('headline: ' + headline)
        return headline

    def get_about_info(self) -> str:
        # core-section-container__content
        about = self.driver.find_elements(By.CLASS_NAME, 'core-section-container__content')[1].text
        print('about: ' + about)
        return about

    def get_experiences(self) -> []:
        experiences_data = []
        try:
            experience__list = self.driver.find_element(By.CLASS_NAME, 'experience__list')
            experiences_items = experience__list.find_elements(By.CLASS_NAME, 'experience-item')
            for experiences_item in experiences_items:
                organisations_name = experiences_item.find_element_by_class_name('profile-section-card__subtitle').text
                title = experiences_item.find_element_by_class_name('profile-section-card__title').text
                date_r = experiences_item.find_element_by_class_name('date-range')
                time_1 = date_r.find_elements_by_tag_name('time')[0].text
                try:
                    time_2 = date_r.find_elements_by_tag_name('time')[1].text
                except IndexError:
                    time_2 = 'Present'
                data_range = time_1 + ' - ' + time_2
                try:
                    description = experiences_item.find_elements(By.CLASS_NAME, 'experience-item__description')[0].text
                except IndexError:
                    description = ''
                location = experiences_item.find_element_by_class_name('experience-item__location').text
                experiences_data.append({
                    "organisations_name": organisations_name,
                    "title": title,
                    "date range": data_range,
                    "description": description,
                    "location": location})
        except IndexError:
            pass
        return experiences_data

    @property
    def get_education(self) -> []:
        education_data = []
        try:
            education_list = self.driver.find_elements(By.CLASS_NAME, 'education__list')[0]
            education_list_items = education_list.find_elements(By.CLASS_NAME, 'education__list-item')
            for education_list_item in education_list_items:
                school_name = education_list_item.find_elements(By.CLASS_NAME, 'screen-reader-text')[0].text
                education_title = education_list_item.find_elements(By.CLASS_NAME, 'education__item--degree-info')[1].text
                date_range = education_list_item.find_elements(By.CLASS_NAME, 'date-range')[0].text
                education_data.append({
                    "school_name": school_name,
                    "education_title": education_title,
                    "date_range": date_range
                })
        except IndexError:
            pass
        return education_data

    def get_certifications(self) -> []:
        certifications_data = []
        try:
            certifications_list = self.driver.find_elements(By.CLASS_NAME, 'certifications__list')[0]
            certifications_list_items = certifications_list.find_elements(By.CLASS_NAME, 'profile-section-card ')
            for certifications_list_item in certifications_list_items:
                title = certifications_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__title')[0].text
                subtitle = certifications_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__subtitle')[0].text
                date_range = certifications_list_item.find_elements(By.CLASS_NAME, 'certifications__date-range')[0].text
                certifications_data.append({
                    "title": title,
                    "subtitle": subtitle,
                    "date_range": date_range
                })
        except IndexError:
            pass
        return certifications_data

    def get_courses(self) -> []:
        courses_data = []
        try:
            courses_list = self.driver.find_elements(By.CLASS_NAME, 'courses__list')[0]
            courses_list_items = courses_list.find_elements(By.CLASS_NAME, 'profile-section-card')
            for courses_list_item in courses_list_items:
                titel = courses_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__title')[0].text
                subtitle = courses_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__subtitle')[0].text
                courses_data.append({
                    "titel": titel,
                    "subtitle": subtitle
                })
        except IndexError:
            pass
        return courses_data

    def get_projects(self) -> []:
        projects_data = []
        try:
            projects__list = self.driver.find_elements(By.CLASS_NAME, 'projects__list')[0]
            projects__list_items = projects__list.find_elements(By.CLASS_NAME, 'personal-project')
            for projects__list_item in projects__list_items:
                title = projects__list_item.find_elements(By.CLASS_NAME, 'profile-section-card__title')[0].text
                subtitle = projects__list_item.find_elements(By.CLASS_NAME, 'profile-section-card__subtitle')[0].text
                info = projects__list_item.find_elements(By.CLASS_NAME, 'profile-section-card__meta')[0].text
                projects_data.append({
                    "title": title,
                    "subtitle": subtitle,
                    "info": info
                })
        except IndexError:
            pass
        return projects_data

    def get_profile_image(self):
        img = self.driver.find_elements(By.CLASS_NAME, 'top-card__profile-image-container')[0]
        img = img.find_elements_by_tag_name('img')[0].get_attribute('src')
        return img

    def get_languages(self) -> []:
        languages_data = []
        try:
            languages_list = self.driver.find_elements(By.CLASS_NAME, 'languages__list')[0]
            languages_list_items = languages_list.find_elements(By.CLASS_NAME, 'profile-section-card ')
            for languages_list_item in languages_list_items:
                title = languages_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__title')[0].text
                subtitle = languages_list_item.find_elements(By.CLASS_NAME, 'profile-section-card__subtitle')[0].text
                languages_data.append({
                    "title": title,
                    "subtitle": subtitle
                })
        except IndexError:
            pass
        return languages_data

    def get_all_data(self) -> {}:
        data = {
            "img_url": self.get_profile_image(),
            "github": "https://github.com/alshfu",
            "url": "https://www.linkedin.com/in/alshfu/",
            "phone": "0736960561",
            "email": self.login,
            "name": self.get_name(),
            "headline": self.get_headline(),
            "about_info": self.get_about_info(),
            "experiences": self.get_experiences(),
            "education": self.get_education,
            "certifications": self.get_certifications(),
            "courses": self.get_courses(),
            "projects": self.get_projects(),
            "languages": self.get_languages(),
        }
        return data

    def create_json_file(self):
        file_name = 'cv_data.json'
        with codecs.open(file_name, encoding='utf-8', mode='w') as outfile:
            json.dump(self.get_all_data(), outfile, ensure_ascii=False)

    def driver_close(self):
        self.driver.close()


if __name__ == '__main__':
    login = ''
    password = ''
    url_page = ''
    person = Person(login_name=login, pwd=password, url=url_page)
    person.create_json_file()
    person.driver_close()
