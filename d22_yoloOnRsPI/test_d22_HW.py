import os
import argparse
import imghdr
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('NAME')
    parser.add_argument('ID')
    args = parser.parse_args()
    name = args.NAME
    id = args.ID
    print('my name is' + str(name) + ' and my id is' + str(id))    

    else:
        print('some error or Blah Blah Blah')
