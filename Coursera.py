# import urllib2
# coursera_cs="https://www.coursera.org/browse/computer-science?_facet_changed_=true"
# page = urllib2.urlopen(coursera_cs)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page, "html5lib")
# soup = soup.encode("utf-8")
# print soup.prettify()
#print (soup.encode("utf-8"))
# all_links=soup.find_all("a")
# for links in all_links:
import requests
import collections 
import mysql.connector
from mysql.connector import errorcode

#creating a connection with the database
def create_connection():
    try:
        cnx = mysql.connector.connect(user='root', password='Namrata1', host = 'localhost',port='3306',
                                database='coursera')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx  

# http://stackoverflow.com/questions/1254454/fastest-way-to-convert-a-dicts-keys-values-from-unicode-to-str
def convert(data):
    if isinstance(data, basestring):
        return data.encode('utf-8')
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


def display(data):
    if type(data) is list:
        output = ""
        for idx,item in enumerate(data):
            output += display(item)
            if idx < len(data)-1:
                output += ","
        return output
    elif type(data) is dict:
        return str(convert(data))
    else:
        return unicode(data).encode('utf-8')

def get_instructor_details(id):
    # make api call to get name and return it
    fields = ['id', 'Photo', 'department','firstName', 'middleName', 'lastName', 'fullName', 'shortName']
    request_url = "https://api.coursera.org/api/instructors.v1/"+ str(id) + "?fields=" +str(",".join(fields))
    print "Sending request to URL: " + str(request_url)
    resp = requests.get(request_url)
    if resp.status_code != 200:
            # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))    #for idx, instructor in enumerate(resp.json()['elements']):
        # print('{} - ID: {} Name: {}'.format(idx, course['id'], course['name'].encode('ascii', 'xmlcharrefreplace')))
        # print('instructorIds: {} partnerIds:{} photoUrl: {} partnerLogo: {}\n description: {} certificates: {} domainTypes: {}'.format(course['instructorIds'], course['partnerIds'], course['photoUrl'], course['partnerLogo'], course['description'].encode('ascii', 'xmlcharrefreplace'), course['certificates'], course['domainTypes'])) 
        # print "-------------------------\n"
    instructor = str(resp.json()['elements'])
        #print "Instructor "+str(idx)+":"
    # for field in fields:
    #     if field not in instructor:
    #         instructor[field] = "none"
    #     # if field == 'instructorIds'
        #     instructor_names = get_instructor_names(course[field])
        # print "printing field: "+str(field)

        #print field+": " + str(display(instructor[field]))
        #returns a list which contains a dictionary
    return instructor       
        #print "\n-------------------------\n"
def get_instructors_details(ids):
    instructors_details = []
    for id in ids:
        instructors_details.append(get_instructor_details(id))
    print str(display(instructors_details))

def get_partner_details(id):
    # make api call to get name and return it
    fields = ['id', 'name', 'shortName', 'description', 'banner', 'courseIds', 'instructorIds', 'squareLogo', 'location']
    request_url = "https://api.coursera.org/api/partners.v1/"+ str(id) + "?fields=" +str(",".join(fields))
    print "Sending request to URL: " + str(request_url)
    resp = requests.get(request_url)
    if resp.status_code != 200:
            # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #for idx, instructor in enumerate(resp.json()['elements']):
        # print('{} - ID: {} Name: {}'.format(idx, course['id'], course['name'].encode('ascii', 'xmlcharrefreplace')))
        # print('instructorIds: {} partnerIds:{} photoUrl: {} partnerLogo: {}\n description: {} certificates: {} domainTypes: {}'.format(course['instructorIds'], course['partnerIds'], course['photoUrl'], course['partnerLogo'], course['description'].encode('ascii', 'xmlcharrefreplace'), course['certificates'], course['domainTypes'])) 
        # print "-------------------------\n"
        #print "Error"
    partner = str(resp.json()['elements'])
    #print "hello\n"
        #print "Instructor "+str(idx)+":"
    # for field in fields:
    #     if field not in instructor:
    #         instructor[field] = "none"
    #     # if field == 'instructorIds'
        #     instructor_names = get_instructor_names(course[field])
        # print "printing field: "+str(field)

        #print field+": " + str(display(instructor[field]))
        #returns a list which contains a dictionary
    return partner

def get_partners_details(ids):
    partner_details = []
    for id in ids:
        partner_details.append(get_partner_details(id))
    print str(display(partner_details))


def get_courses_details(cnx,num_pages, limit=100):
    fields = ['id', 'name', 'partnerLogo', 'photoUrl', 'description','startDate']

    for page_num in range(num_pages):
        request_url = "https://api.coursera.org/api/courses.v1?fields="+str(",".join(fields))+"&start="+str(page_num*100)+"&limit="+str(limit)
        print "Sending request to URL: " + str(request_url)
        resp = requests.get(request_url)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        for idx, course in enumerate(resp.json()['elements']):
            # print('{} - ID: {} Name: {}'.format(idx, course['id'], course['name'].encode('ascii', 'xmlcharrefreplace')))
            # print('instructorIds: {} partnerIds:{} photoUrl: {} partnerLogo: {}\n description: {} certificates: {} domainTypes: {}'.format(course['instructorIds'], course['partnerIds'], course['photoUrl'], course['partnerLogo'], course['description'].encode('ascii', 'xmlcharrefreplace'), course['certificates'], course['domainTypes'])) 
            # print "-------------------------\n"

            print "Course "+str(idx)+":"
            for field in fields:
                if field not in course:
                    course[field] = "none"
                # if field == 'instructorIds'
                #     instructor_names = get_instructor_names(course[field])
                # print "printing field: "+str(field)

                print field+": " + str(display(course[field]))
                #inserting data fetched into database
            sql = "INSERT INTO Courses(id, name, partnerLogo, photoUrl, description, startDate) VALUES ('%s', '%s', '%s', '%s', '%s',)"
                             % / (display(course['id']), display(course['name']), display(course['partnerLogo']), display(course['photoUrl']),
                        display(course['description']), NULL)
            try:
               # Execute the SQL command
               cursor.execute(sql)
               # Commit your changes in the database
               cnx.commit()
               print "Changes Committed"
            except:
               # Rollback in case there is any error
               cnx.rollback()
               print "Changes roll-back"
            print "\n-------------------------\n"

cnx=create_connection()
get_courses_details(cnx,23)
cnx.close()
#ids=['1620951','1960981','1961937']
#ids_p=['147', '176','223']
#get_instructors_details(ids)
#get_partners_details(ids_p)

