class HTTP:
    """This class is used to extract the HTTP header from TCP or UDP data."""
    def __init__(self, raw_data):
        try:
            self.data = raw_data.decode('utf-8')
        except:
            self.data = raw_data
