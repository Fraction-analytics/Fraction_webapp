import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)
# Day1 hash for 24 hours
# Key , Field , Value
r.hset("10-10-21" ,  "12am" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video1.mp4" ),
r.hset("10-10-21" ,  "1am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video2.mp4" ),
r.hset("10-10-21" ,  "2am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video3.mp4" ),
r.hset("10-10-21" ,  "3am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video4.mp4" ),
r.hset("10-10-21" ,  "4am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video5.mp4" ),
r.hset("10-10-21" ,  "5am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video6.mp4" ),
r.hset("10-10-21" ,  "6am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video7.mp4" ),
r.hset("10-10-21" ,  "7am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video8.mp4" ),
r.hset("10-10-21" ,  "8am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video9.mp4" ),
r.hset("10-10-21" ,  "9am"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video10.mp4" ),
r.hset("10-10-21" ,  "10am" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video11.mp4" ),
r.hset("10-10-21" ,  "11am" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video12.mp4" ),
r.hset("10-10-21" ,  "12pm" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video13.mp4" ),
r.hset("10-10-21" ,  "1pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video14.mp4" ),
r.hset("10-10-21" ,  "2pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video15.mp4" ),
r.hset("10-10-21" ,  "3pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video16.mp4" ),
r.hset("10-10-21" ,  "4pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video17.mp4" ),
r.hset("10-10-21" ,  "5pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video18.mp4" ),
r.hset("10-10-21" ,  "6pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video19.mp4" ),
r.hset("10-10-21" ,  "7pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video20.mp4" ),
r.hset("10-10-21" ,  "8pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video21.mp4" ),
r.hset("10-10-21" ,  "9pm"  ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video22.mp4" ),
r.hset("10-10-21" ,  "10pm" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video23.mp4" ),
r.hset("10-10-21" ,  "11pm" ,  "/http://localhost:3000/videos/Fraction_webapp/backend/videos/video24.mp4" )
# creating hash for 31 days using above hash method


# adding the above hashes into single set
r.sadd("date", "01/8/21")
r.sadd("date", "02/8/21")
r.sadd("date", "03/8/21")
r.sadd("date", "04/8/21")
r.sadd("date", "05/8/21")
r.sadd("date", "06/8/21")
r.sadd("date", "07/8/21")
r.sadd("date", "08/8/21")
r.sadd("date", "09/8/21")
r.sadd("date", "10/8/21")
r.sadd("date", "11/8/21")
r.sadd("date", "12/8/21")
r.sadd("date", "13/8/21")
r.sadd("date", "14/8/21")
r.sadd("date", "15/8/21")
r.sadd("date", "16/8/21")
r.sadd("date", "17/8/21")
r.sadd("date", "18/8/21")
r.sadd("date", "19/8/21")
r.sadd("date", "20/8/21")
r.sadd("date", "21/8/21")
r.sadd("date", "22/8/21")
r.sadd("date", "23/8/21")
r.sadd("date", "24/8/21")
r.sadd("date", "25/8/21")
r.sadd("date", "26/8/21")
r.sadd("date", "27/8/21")
r.sadd("date", "28/8/21")
r.sadd("date", "29/8/21")
r.sadd("date", "30/8/21")
r.sadd("date", "31/8/21")
r.save


my = r.sort("date", 24, 31, alpha=True)
# print(my)

# for i in my:
#     print(r.hvals(i))


# Retrieve the value for a specific key

getting_Video1 = r.hget("31/8/21", "12am")  # byte


# Need to decode every single video
decoding_vid = getting_Video1.decode('utf-8', 'ignore')  # \
# print(decoding_vid)
# print(type(decoding_vid))  # string


# print("Value for the key 3 is")
# print(r.hget("31/8/21", "2am"))


# print("The keys present in the Redis hash:")
# print(r.hkeys("31/8/21"))


# print("The values present in the Redis hash:")
# print(r.hvals("31/8/21"))


# print("The keys and values present in the Redis hash are:")
# print(r.hgetall("31/8/21"))
