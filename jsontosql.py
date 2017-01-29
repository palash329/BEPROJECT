#Created the DB
import sqlite3
import jsonschema
import json
import urllib2
path ="/home/ash/Project_January/prac/"
conn = sqlite3.connect(path+'Twitter.db')
c = conn.cursor()
print "Opened database successfully";
#Created the table for the tweets
c.execute("CREATE TABLE IF NOT EXISTS Tweet(id BLOB PRIMARY KEY,time BLOB,text_tweet BLOB,location BLOB,device BLOB,user_followers BLOB, \
        user_favorite BLOB,use_timezone BLOB,geo BLOB,cordinates BLOB,place BLOB,retweeted_time BLOB, retweeted_id BLOB,\
             retweeted_device BLOB,retweeted_user_location BLOB,retweeted_user_followers BLOB, \
             retweeted_user_timezone BLOB,retweeted_geo BLOB,retweeted_coordinates BLOB,retweeted_place BLOB, \
             retweeted_retweet_count BLOB,timestamp BLOB)")

#Read file and print a line

a = open(path+"sampledb.json").read().split("\n")
data = list()
t=""
for i in a:
        try:
                data.append(json.loads(i))
        except:
                pass
for j in data:
        print ('\n')
        try:
                query = "INSERT INTO Tweet VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\");".format( j.get('id'),j.get('created_at'),j.get('text'),j.get('location'),
                        "",j.get('user').get('followers_count'),j.get('user').get('favorite_count'),
                        j.get('user').get('time_zone'),j.get('geo'),j.get('coordinates'),j.get('place'),
                        j.get('retweeted_status').get('created_at'),j.get('retweeted_status').get('id'),
                        j.get('retweeted_status').get('text'),"",
                        j.get('retweeted_status').get('user').get('location'),
                        j.get('retweeted_status').get('user').get('followers_count'),
                        j.get('retweeted_status').get('user').get('timezone'),
                        j.get('retweeted_status').get('geo'),j.get('retweeted_status').get('coordinates'),
                        j.get('retweeted_status').get('place'),j.get('retweeted_status').get('retweet_count'), 
                        "", "")
                
                conn.execute(query);
                print "Tweet Inserted into DB"
        except:
                print query
                
        t =conn.execute("select * from Tweet").fetchall()        
c.close()

conn.commit()
conn.close()
