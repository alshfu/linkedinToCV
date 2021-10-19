import codecs
import json
import os
from random import randint

head_of_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Orbit - Bootstrap 5 Resume/CV Template for Developers</title>
    <!-- Meta -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Responsive HTML5 Resume/CV Template for Developers">
    <meta name="author" content="Xiaoying Riley at 3rd Wave Media">
    <link rel="shortcut icon" href="favicon.ico">
    <!-- Google Font -->
    <link
    href='https://fonts.googleapis.com/css?family=Roboto:400,500,400italic,300italic,300,500italic,700,700italic,900,900italic'
    rel='stylesheet' type='text/css'>
    <!-- FontAwesome JS--><script defer src="assets/fontawesome/js/all.min.js"></script><!-- Global CSS -->
    <link rel="stylesheet" href="assets/plugins/bootstrap/css/bootstrap.min.css">
    <!-- Theme CSS -->
    <link id="theme-style" rel="stylesheet" href="assets/css/orbit-1.css">
</head>
'''


def create_education_items(educations: [] = []) -> str:
    html_begin = '''<div class="education-container container-block">
                    <h2 class="container-block-title">Education</h2>'''
    education_html = ''
    simple = '''
                    <div class="item">
                        <h4 class="degree">BSc in Applied Mathematics</h4>
                        <h5 class="meta">Bristol University</h5>
                        <div class="time">2012 - 2016</div>
                    </div><!--//item-->'''
    for education in educations:
        education_html = '''<div class="item">
        <h4 class="degree">''' + education['education_title'] + '''</h4>
        <h5 class="meta">''' + education['school_name'] + '''</h5>
        <div class="time">''' + education['date_range'] + '''</div>
        </div><!--//item-->''' + education_html

    html_end = '''</div>'''
    return html_begin + education_html + html_end


def create_languages_items(languages: [] = []) -> str:
    html_begin = '''
    <div class="languages-container container-block">
        <h2 class="container-block-title">Languages</h2>
        <ul class="list-unstyled interests-list">'''
    items = ''
    for language in languages:
        items = '''
        <li>''' + language['title'] + '''
            <span class="lang-desc">(''' + language['subtitle'] + ''')</span>
        </li>''' + items

    html_end = '''
        </ul>
    </div>'''
    return html_begin + items + html_end


def create_interests_items(interests: [] = []) -> str:
    # TODO göra klar
    return '''
    <div class="interests-container container-block">
        <h2 class="container-block-title">Interests</h2>
        <ul class="list-unstyled interests-list">
            <li>Climbing</li>
            <li>Snowboarding</li>
            <li>Cooking</li>
        </ul>
    </div>'''


def create_summary_item(headline: str) -> str:
    return '''
        <h2 class="section-title"><span class="icon-holder"><i class="fas fa-user"></i></span>Career Profile</h2>
        <div class="summary">
            <p>''' + headline + '''</p>
        </div><!--//summary-->
    '''


def create_experiences_items(experiences: [] = []) -> str:
    html_begin = '''
    <h2 class="section-title"><span class="icon-holder"><i class="fas fa-briefcase"></i></span>Experiences</h2>
    '''
    items = ''
    for experience in experiences:
        items = '''
        <div class="item">
            <div class="meta">
                <div class="upper-row">
                    <h3 class="job-title">''' + experience['title'] + '''</h3>
                    <div class="time">''' + experience['date range'] + '''</div>
                </div><!--//upper-row-->
                <div class="company">''' + experience['location'] + ''', ''' + experience['organisations_name'] + '''
                </div>
            </div><!--//meta-->
            <div class="details">
                <p>''' + experience['description'] + '''</p>
           </div><!--//details-->
        </div><!--//item-->''' + items

    return html_begin + items


def create_projects_items(projects: [] = []) -> str:
    html_begin = '''
    <h2 class="section-title">
        <span class="icon-holder">
            <i class="fas fa-archive"></i>
        </span>Projects
    </h2>
    '''
    items = ''
    for project in projects:
        items = '''
        <div class="item">
            <span class="project-title">
                <a href="#">''' + project['title'] + '''</a>
            </span> - 
            <span class="project-tagline">
            ''' + project['info'] + '''
            </span>
        </div>
        ''' + items

    return html_begin + items


def create_certifications_items(certifications: [] = []) -> str:
    html_begin = '''
    <h2 class="section-title">
        <span class="icon-holder">
            <i class="fa fa-certificate"></i>
        </span>Certifications
    </h2>
    '''
    items = ''
    for certification in certifications:
        items = '''
        <div class="item">
            <span class="project-title">
                <a href="#">''' + certification['subtitle'] + '''</a>
            </span> - 
            <span class="project-tagline">
            ''' + certification['title'] + '''
            </span>
        </div>
        ''' + items

    return html_begin + items


def create_skills_items(skills: [] = []) -> str:
    html_begin = '''
        <h2 class="section-title">
            <span class="icon-holder">
                <i class="fas fa-rocket"></i>
            </span>Courses &amp; Proficiency
        </h2>
        <div class="skillset">
        '''
    items = ''''''

    for skill in skills:
        val = str(randint(80, 100))
        items = '''
        <div class="item">
            <h3 class="level-title">''' + skill['titel'] + '''</h3>
            <div class="progress level-bar">
                <div class="progress-bar theme-progress-bar" 
                     role="progressbar" 
                     style="width: ''' + val + '''%" 
                     aria-valuenow="''' + val + '''" 
                     aria-valuemin="0" 
                     aria-valuemax="100">
                </div>
            </div>
        </div>
        <!--//item-->''' + items
    return html_begin + items + '</div>'


def create_body(json_data) -> str:
    body_of_html = '''
    <body>
        <div class="wrapper">
            <div class="sidebar-wrapper">
                <div class="profile-container">
                    <img class="profile" src="''' + json_data['img_url'] + '''" alt="''' + json_data['name'] + '''" />
                    <h1 class="name">''' + json_data['name'] + '''</h1>
                    <h3 class="tagline">''' + json_data['headline'] + '''</h3>
                </div>
                <!--//profile-container-->
                <div class="contact-container container-block">
                    <ul class="list-unstyled contact-list">
                        <li class="email">
                        <i class="fas fa-envelope"></i>
                        <a href="mailto:''' + json_data['email'] + '''">''' + json_data['email'] + '''</a>
                        </li>
                        <li class="phone">
                        <i class="fas fa-phone"></i>
                        <a href="tel:''' + json_data['phone'] + '''">''' + json_data['phone'] + '''</a>
                        </li>
                        <li class="linkedin"><i class="fab fa-linkedin-in"></i>
                        <a href="''' + json_data['url'] + '''" target="_blank">''' + json_data['name'] + '''</a>
                        </li>
                        <li class="github"><i class="fab fa-github"></i>
                        <a href="''' + json_data['github'] + '''" target="_blank">
                        ''' + json_data['github'].replace('https://github.com/', '') + '''</a>
                        </li>
                    </ul>
                </div>
                <!--//contact-container-->
                ''' + create_education_items(json_data['education']) + '''
                <!--//education-container-->
                ''' + create_languages_items(json_data['languages']) + '''
                <!--//languages-->
                <!--interests--> 
                <!--//interests-->
            </div><!--//sidebar-wrapper-->
    
            <div class="main-wrapper">
                 <section class="section summary-section">
                 ''' + create_summary_item(json_data['about_info']) + '''
                 </section>
                 <!--//section-->
    
                <section class="section experiences-section">
                ''' + create_experiences_items(json_data['experiences']) + '''
                </section>
                <!--//section-->
    
                <section class="section projects-section">
                ''' + create_projects_items(json_data['projects']) + '''
                </section>
                <!--//section-->
    
                <section class="section projects-section">
                ''' + create_certifications_items(json_data['certifications']) + '''
                </section>
                <!--//section-->
    
                <section class="skills-section section">
                ''' + create_skills_items(json_data['courses']) + ''' 
                </section>
                <!--//skills-section-->
    
            </div><!--//main-body-->
        </div>
    
        <footer class="footer">
            <div class="text-center">
                <!--/* This template is free as long as you keep the footer attribution link. If you'd like to use the template without the attribution link, you can buy the commercial license via our website: themes.3rdwavemedia.com Thank you for your support. :) */-->
                <small class="copyright">Designed with <i class="fas fa-heart"></i> by <a href="http://themes.3rdwavemedia.com" target="_blank">Xiaoying Riley</a> for developers</small>
            </div><!--//container-->
        </footer><!--//footer-->
    
    </body>
    </html>
    '''
    return body_of_html


def create_index_html():
    file_location = os.path.dirname(os.path.realpath(__file__))
    file = open('cv_data.json', encoding="utf8")
    data = json.load(file)
    file_name = file_location + '\OrbitThemeMaster\Orbit-Theme-master\index.html'
    html_code = head_of_html + create_body(data)
    with codecs.open(file_name, encoding='utf-8', mode='w') as html_file:
        html_file.write(html_code)

create_index_html()
