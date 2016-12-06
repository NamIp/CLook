# :computer: CLook - Application to look up the best MOOC

### Table of Contents
1. [About](#about)
2. [How does it work?](#how-does-it-work)
3. [Built With](#built-with)
4. [Demo](#demo)
5. [Contributing](#contributing)
6. [License](#license)

## About

CLook is an application which answers one of the most asked question of ‘where to do a MOOC from?’. Every tech student has wondered where to start learning Python and wondered whether Coursera or Udacity is the best choice for him/her. Each CS student has spent hours poring over numerous open courseware sites, instead of actually spending that time on learning something. CLook solves this problem and spares students the time and effort of scouring websites for the course of their choice, so that he/she can utilise their time most efficiently and productively in learning something new. CLook is a Web and Android-based application which lists out MOOCs based on your subject and university preference. The application compiles the complete course catalog from popular sites such as Coursera, Udemy, Udacity, edX and MIT OCW. The user can also set a reminder for the next session of their favourite course. The application also gathers information from the user’s Facebook/Gmail contact list and specifies how many of their contacts have taken the course previously. This way, the user need not ask their friends for course recommendations, as CLook does it for them! 

This application was built during Hack'ItGirls Hackathon, Delhi and is currently under development.

## How does it work?

CLook queries the APIs of six major courseware sites and saves them into its own database. For lesser-known sites, Web scraping is used.

When the user enters the subject preference, the application sorts all courses based on the ratings and reviews of users who’ve previously taken that course. All the major open courseware sites follow a system of feedback based on ratings from 0 to 5 stars. Based on this uniform criteria of rating, the best result is displayed.

Following this, users can also filter on the basis of university, instructor, start date etc.

##Built With

* Python 2.7
* MySQL5.7
* MySQL-Python Connector 6.0.2
* JavaScript
* CSS3, HTML5
* jQuery

## Demo


##Contributing

See [CONTRIBUTING.md](https://github.com/Namrata96/CLook/blob/master/CONTRIBUTING.md) for more details. Or feel free to reach out to us via mail.

[Namrata Mukhija](mailto:namratamukhija@gmail.com)
[Ipshita Chatterjee](mailto:chatterjeei08@gmail.com)

##License

CLook is licensed under Apache 2.0 license. See [LICENSE.md](https://github.com/Namrata96/CLook/blob/master/LICENSE.md) for more details.
