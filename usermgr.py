""" User Management Module

This module reads the 'users.conf' file and gets all users's logging info.

user_info_index = ['account', 'password', 'device','macaddr']
"""

__all__ = ["usermgr"]

import ConfigParser

class usermgr:
    def __init__(self):
        self.users_config_file = '/etc/config/oh3c' 
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.users_config_file)
       
    def get_user_number(self):
        return len(self.cf.sections())

    def get_users_info(self):
        users_info = []
        for account in self.cf.sections():
            dev = self.cf.get(account, 'dev')
	    macaddr = self.cf.get(account, 'macaddr')
            users_info.append((account, dev,macaddr))
        return users_info
    
    def delete_user(self, user_name):
        self.cf.remove_section(user_name)
        self.save_config()
    
    def create_user(self, user_info):
        self.cf.add_section(user_info[0])
        self.update_user_info(user_info)

    def update_user_info(self, user_info):
        self.cf.set(user_info[0], 'password', user_info[1])
        self.cf.set(user_info[0], 'dev', user_info[2])
        self.cf.set(user_info[0], 'macaddr', user_info[3])
        self.save_config()
        
    def save_config(self):
        users_config = open(self.users_config_file, 'w')
        self.cf.write(users_config)
        users_config.close()

    def get_user_info(self, idx):
        account = self.cf.sections()[idx]
        password = self.cf.get(account,'password')
        dev = self.cf.get(account,'dev')
        macaddr = self.cf.get(account,'macaddr')
        return (account,password,dev,macaddr)
         