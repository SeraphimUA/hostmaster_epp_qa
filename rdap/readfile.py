class Textfile:
    def __init__(self, filename):
        f = open(filename, 'r')
        entities_list = f.readlines()
        self.entities_list = []
        for d in entities_list:
            self.entities_list.append(d.strip())
        f.close()

    def print_list(self):
        print(self.entities_list)

f = Textfile('rdap\\rdap_test_host_list\\rdap_test_host_list.txt')
# f.print_list()
