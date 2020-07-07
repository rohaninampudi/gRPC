import argparse
import smtplib
import os
import json
import redis
import pickle

parser = argparse.ArgumentParser(description="Threshold Value")
parser.add_argument('threshold', type=float, help='threshold value')
args = parser.parse_args()


def parsefile(filename):
    with open(filename) as f:
        list = []
        for line in f:
            if 'chrony' in line:
                for line in f:
                    list.append(
                        line.split(' '))  # Return a list of the words in the string, using sep as the delimiter string.

    # print(list)
    for item in list:
        item[:] = [x for x in item if x != '' and x != '--' and x != '\n' and x != '+-']
        item[:] = item[:4]

    return list


def checkWhichUsersExceed(list, threshold):
    # print(list)
    returnList = []
    for user in list:
        # print(user)
        if not user:  # check if user is empty
            # print("empty list")
            break
        elif float(user[3]) == 0:  # make sure no divide by 0 when storage = 0
            # limitCalc = float(user[1]) / float(user[3])
            print("user: ", user[0], "exceeds the storage limit. There is 0 storage")
            returnList.append([user[0], user[1], user[3], 0.0])
            # store to redis
            # sendEmail(user[0], user[1], user[3], 0.0)
        else:
            limitCalc = float(user[1]) / float(user[3])
            if limitCalc > threshold:
                print("user: ", user[0], "exceeds the storage limit. You have used", limitCalc * 100, "%")
                returnList.append([user[0], user[1], user[3], limitCalc])
                # sendEmail(user[0], user[1], user[3], limitCalc)
            # print(limitCalc)

    return returnList


def storeToRedis(list):
    obj = list
    r = redis.Redis(host='localhost', port=6379, db=0)
    # unpacked = json.loads(r.get(obj).decode('utf-8')) #no
    # packed = unpacked #no
    pickled_object = pickle.dumps(obj)
    r.set('all_data', pickled_object)
    unpacked_object = pickle.loads(r.get('all_data'))
    obj == unpacked_object
    return


def sendEmail(listOfUsersExceeded):
    sender_email = "rohan.inampudi@gmail.com"
    rec_email = "rohan.inampudi@gmail.com"
    password = input(str("Please enter your password: "))  # grvz tmjy clvc ujah
    content = 'email some stuff'

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()  # everything after this is encrypted
    server.login(sender_email, password)
    print("login success")

    '''
    #loop through exceeded members
    for user in listOfUsersExceeded:
        userid = user[0]
        storageUsed = user[3]
        
        emailid = os.system("id -p [%s]" % userid) #gets username given user id
        
        content = "ADD CONTENT OF EMAIL HERE"
        rec_email = emailid + "@deepvision.io"
        
        server.sendmail(sender_email, rec_email, content)
    '''

    server.sendmail(sender_email, rec_email, content)
    print("email has been sent to ", rec_email)
    server.close()

    return


if __name__ == "__main__":
    list = parsefile("quota.txt")
    # print(list)

    usersExceed = checkWhichUsersExceed(list, args.threshold)
    print("LIST", usersExceed)
    # sendEmail(usersExceed)

    storeToRedis(list)
    print("stored data to redis. ")
    # arg parser for threshold value, how often you send each email keep counter,
