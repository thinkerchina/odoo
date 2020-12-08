import functools
import xmlrpclib
#import xmlrpc.client


HOST = 'localhost'
PORT = 8069
DB = 'odoo_data_work'
USER = 'odoo'
PASS = 'odoo'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
# proxy = xmlrpc.client.ServerProxy(ROOT)
# print('dir():',proxy.dir('/tmp'))

# uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Step 1：Logged in %s as %s (uid:%d)" % (ROOT,USER,uid))

'''
call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT).execute,
    DB, uid, PASS)

print("Step 2：Logged in as %s (call:%s)" % (USER,call))


# 2. Read the sessions
sessions = call('testoar.session','search_read', [], ['name','seats'])
for session in sessions:
    print("Step 3: Session %s (%s seats)" % (session['name'], session['seats']))


# 3.create a new session
session_id = call('testoar.session', 'create', {
    'name' : 'My session',
    'course_id' : 2,
})

# 3.create a new session for the "Functional" course
course_id = call('testoar.course', 'search', [('name','ilike','Functional')])[0]
session_id = call('testoar.session', 'create', {
    'name' : 'My session',
    'course_id' : course_id,
})
'''