'''
This repo converts user object to Dictionary.
'''

class UiService(object):
    def __init__(self):
        pass

    def convert_obj_to_dict(self, user_obj):
        return {'email':user_obj.get_email(),
                'name':user_obj.get_name(),
                'balance':user_obj.get_balance()}