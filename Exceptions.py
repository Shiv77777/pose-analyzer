class CustomException(Exception):
    def __init__(self,code,message, *args: object):
        super().__init__(*args)
        self.code=code
        self.message=message