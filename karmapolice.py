from eve import Eve

def general_callback(resource, request, payload):
    print 'A GET on the "%s" endpoint was just performed!' % resource

def before_returning_items(resource, documents):
    print 'About to return items from "%s" ' % resource

app = Eve()
app.on_GET += general_callback
app.on_fetch_resource += before_returning_items
app.run()
