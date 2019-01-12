#
# Class containing scripts to create tables in the database.
# This class is not placed among the rest in the /cgi-bin catalog because cgi framework does not allow an access from outside 
#
class dbScripts():    
    @staticmethod
    def usersTableSql():
        return """CREATE TABLE IF NOT EXISTS users (
 id integer PRIMARY KEY,
 username text NOT NULL,
 password text not null,
 firstname text,
 lastname text,
 adress text,
 email text 
);"""    
    @staticmethod
    def toolsTableSql():
        return """CREATE TABLE IF NOT EXISTS tools (
 id integer PRIMARY KEY,
 toolname text NOT NULL,
 tooldesc text not null,
 imagename text not null,
 ownerid integer not null,
 price integer not null,
 avilabile integer not null,
 dateavilabile text
);"""
    
    @staticmethod
    def invoicesTableSql():
        return """CREATE TABLE IF NOT EXISTS invoices (
 id integer PRIMARY KEY,
 userid integer NOT NULL,
 toolid integer not null,
 toolname text not null,
 price integer not null,
 dateofrent text
);"""
    @staticmethod
    def booked_toolsTableSql():
        return """CREATE TABLE IF NOT EXISTS booked_tools(
 id integer PRIMARY KEY,
 userid integer NOT NULL,
 toolid integer not null,
 startdate text not null,
 enddate text not null,
 returned integer default 0
);"""
    @staticmethod
    def returned_toolsTableSql():
        return """CREATE TABLE IF NOT EXISTS returned_tools(
 id integer PRIMARY KEY,
 ownerid integer not null,
 userid integer NOT NULL,
 toolid integer not null,
 picname text not null,
 condition text not null
);"""