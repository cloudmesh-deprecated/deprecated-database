from mongoengine import Document, StringField
from cloudmesh_database.dbconn import get_mongo_db, get_mongo_dbname_from_collection, DBConnFactory


class ExampleRecord(Document):
    '''
    an example mongonengine docoment class
    The class name has to be unique within one db where it stores
    '''
    # define fields first
    city = StringField(required=True)
    country = StringField(required=True)
    description = StringField(max_length=50)
    #
    # 'example' is one of the collection names defined in the cloudmesh_database.yaml file
    # This will give the dbname, as well as the named alias of the connection for objects
    # from this document class.
    dbname = get_mongo_dbname_from_collection("example")
    #
    # by default using named alias instead of the 'default' db
    if dbname:
        meta = {'db_alias': dbname}
    
def main():
    #
    # this returns a mongoengine connection to the db of the 'experiment' collection (from yaml config)
    # The db has to exist and be initiated before connection
    #
    get_mongo_db("example", DBConnFactory.TYPE_MONGOENGINE)
    
    # delete all entries. Use with cautious
    ExampleRecord.objects().delete()
    
    # sample data to populate
    citycountry = [{'city':'New York', 'country':'US'},
                   {'city':'Beijing', 'country':'China'},
                   {'city':'Los Angeles', 'country':'US'},
                   {'city':'London', 'country':'UK'},
                   {'city':'Shanghai', 'country':'China'}]
    # populate the db               
    for entry in citycountry:
        arecord = ExampleRecord(city=entry['city'], country=entry['country'], description='a city with so many people')
        # this saves the record
        arecord.save()
    # query all records in the db that are 'ExampleRecord' object
    allrecords = ExampleRecord.objects()
    print "\nAll records in db"
    print "-"*80
    for arecord in allrecords:
        print 'city:%s\t|country:%s' % (arecord.city, arecord.country)
        print '\tdescription:%s' % arecord.description
    
    # query with condition
    somerecords = ExampleRecord.objects(country='US')
    print "\nUS cities in db"
    print "-"*80
    for arecord in somerecords:
        print 'city:%s\t|country:%s' % (arecord.city, arecord.country)
        print '\tdescription:%s' % arecord.description

if __name__ == '__main__':
    main()
