from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == '__main__':
    file = open('input.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        first_road, secend_road = the_string.split(' ')
        file_1 = open(first_road, 'r')
        file_2 = open(secend_road, 'r')
        print(similar(file_1, file_2))
        file_1.close
        file_2.close

    file.close

