import unittest
from lenticular_cloud.model import User
from lenticular_cloud import model
from ldap3 import Server, Connection, MOCK_SYNC

class TestBasicModelFunction(unittest.TestCase):

    def setUp(self):
        server = Server.from_definition('my_fake_server', 'mokup/info.json', 'mokup/schema.json')
        model.ldap_conn = Connection(server, user='cn=admin,dc=example,dc=org', password='123456', client_strategy=MOCK_SYNC)
        model.ldap_conn.strategy.entries_from_json('mokup/entries.json')
        model.ldap_conn.strategy.add_entry('cn=admin,dc=example,dc=org', {'userPassword': '123456', 'sn': 'admin'})

        model.ldap_conn.bind()
        model.base_dn = 'dc=example,dc=org'

    def test_create(self):
        user = User(uid='test', sn='test',cn='test')
        user.email='test@example.com'
        print(user)
        user.commit()
        print(User.query().by_username('test'))
        print(User.query().all())





