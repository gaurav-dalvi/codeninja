import re
import threading
import sys
import uuid
import os

class File_Read_Thread(threading.Thread):

    def __init__(self, threadID, file, mapList):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file = file
        self.mapList = mapList

    def run(self):
        with open(self.file) as f:
            data = f.read()

        word_list = [item.lower() for item in re.findall(r"[\w']+", data)]
        word_map = {}
        index = 0
        while index < len(word_list) - 3:
            new_word = word_list[index] + ' ' + word_list[index + 1] + ' ' + word_list[index + 2]
            if new_word in word_map.keys():
                word_map[new_word] += 1
            else:
                word_map[new_word] = 1
            index += 1

        threadLock.acquire()
        mapList.append(word_map)
        threadLock.release()

def gen_top_results(word_map_list):
    # aggregate all hash_maps
    uber_hash_map = {}
    for item in mapList:
        for k, v in item.items():
            if k in uber_hash_map.keys():
                uber_hash_map[k] = uber_hash_map[k] + v
            else:
                uber_hash_map[k] = v

    # converting map to list and then sorting it in descending fashion
    top_results = []
    for k, v in uber_hash_map.items():
        top_results.append((k, v))

    top_results = sorted(top_results, key=lambda tup: tup[1], reverse=True)

    # return top 100 most frequently occusred words
    return top_results[:100]

if __name__ == '__main__':

    threadLock = threading.Lock()
    mapList = []
    threads = []
    i = 0

    if len(sys.argv) == 1:
        file_name = str(uuid.uuid4())
        file = file_name + ".txt"
        data = ''
        for line in sys.stdin:
            data = data + line
        f = open(file, "w")
        f.write(data)
        f.close()

        thread = File_Read_Thread(i + 1, file, mapList)
        thread.start()
        threads.append(thread)
        os.remove(file)
    else:
        while i < len(sys.argv) - 1:
            thread = File_Read_Thread(i+1, sys.argv[i+1], mapList)
            thread.start()
            threads.append(thread)
            i += 1

    for t in threads:
        t.join()

    print(gen_top_results(mapList))