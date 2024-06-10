import multiprocessing
import requests

def downloadFile(url, name):
    response = requests.get(url)
    print(f"Started downloading file{name}.jpg")
    
    file_path = f"day98\\files2\\file{name}.jpg"
    with open(file_path, "wb") as file:
        file.write(response.content)
    
    print(f"Finished downloading file{name}.jpg")

urls = [
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GIS6YiV3hvbS7sVi_1rpYAHaEK%26pid%3DApi%26h%3D160&f=1&ipt=b87e7e23ba37c4d3f76867de2a45373b5bd2fc5c86a533e7d10ff2e26c3c795e&ipo=images",
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.fP1SP-meOSrVBMQ57wIKXAHaEo%26pid%3DApi%26h%3D160&f=1&ipt=afc454c1441b9f6b7aaebf4e9987d91c751cd1b176592a625fae4fe6d544aeb0&ipo=images",
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.YmjM3GWFvAkqpYcTWYPf7gHaE7%26pid%3DApi%26h%3D160&f=1&ipt=d1b52a42da93258a486c7f13fbdddb9a6d6a0bf3b1d932cad173c1ebe989df48&ipo=images"
]

if __name__ == "__main__":
    processes = []
    
    # Start processes to download files concurrently
    for i, url in enumerate(urls):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        processes.append(p)
    
    # Ensure all processes complete
    for p in processes:
        p.join()
        
        
        
        
        
#  using concurrent. futures 

from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def task(n):
    print(f" Task {n} started")
    time.sleep(3)
    return f"Task {n} completed "

#  Creating a ProcessPollEcecutor with 3 processes
with ProcessPoolExecutor(max_workers=3) as executor:
    #  submit tasks to the executor 
    futures=[executor.submit(task,i) for i in range(5)]
    
    #  wait For the taskd to be completed and get their results
    for future in as_completed(futures):
        print(futures.results)