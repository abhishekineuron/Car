import multiprocessing

def test():
    print("This is my multiprocessing prog")

if __name__ == "__main__":
    m = multiprocessing.Process(target=test)
    print("This is my main prod")
    m.start()
    m.join()
    print("Both processes have finished!")
