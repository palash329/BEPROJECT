import json
import jsonschema
 
schema = open("schema.json").read()
#print schema
filename = raw_input('Enter a filename: ') 
data = open(filename).read()
#print data
 
try:
    jsonschema.validate(json.loads(data), json.loads(schema))
except jsonschema.ValidationError as e:
    print e.message
except jsonschema.SchemaError as e:
    print e
