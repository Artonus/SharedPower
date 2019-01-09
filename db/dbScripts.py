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
 owner text not null,
 price integer not null,
 avilabile integer not null,
 dateavilabile text
);"""
    pass