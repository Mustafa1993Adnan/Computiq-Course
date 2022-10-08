class Network:
    accessing_type = ''
    correct_ip = True

    def __init__(self, ip):
        try:
            self.full_ip = ip.split('/')
            self.ip = tuple(int(part) for part in self.full_ip[0].split('.'))
            self.prefixes = int(self.full_ip[1])
            for ip in self.ip:
                if ip < 0 or ip > 255:
                    self.correct_ip = False
        except:
            print('error')
    def class_type(self):
        try:
            if self.prefixes == 8:
                return 'Class A'
            elif self.prefixes == 16:
                return 'Class B'
            elif self.prefixes == 24:
                return 'Class C'
            else:
                return 'D or E'
        except:
            print('error')


    def ip_type(self):
        try:
            if self.correct_ip:
                if self.ip[0] == 10 or (self.ip[0] == 172 and 16 <= self.ip[1] <= 31) or self.ip[
                    0] == 192 and self.ip[1] == 168 \
                        and 0 <= self.ip[2] <= 255:
                    return 'Private'
                else:
                    return 'Public'
            else:
                return 'invalid ip'
        except:
            print("Error")
