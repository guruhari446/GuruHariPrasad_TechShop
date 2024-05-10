import mysql.connector as sql

class DBProperty:
    @staticmethod
    def getparameter():
        host = 'localhost'
        database = 'Assignment'
        user = 'root'
        password = 'guruhari2002#'
        return host,database,user,password


class DBConnectivity:
    @staticmethod
    def makeconnection():
        l=DBProperty.getparameter()
        print(l)

DBConnectivity.makeconnection()