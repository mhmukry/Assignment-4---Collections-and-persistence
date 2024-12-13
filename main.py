import os 

if __name__ == '__main__':
    file_path = 'resources.csv'
    if not os.path.exists(file_path):
        open(file_path, 'w').close()


