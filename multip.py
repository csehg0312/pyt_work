from multiprocessing import Process, Pipe, Lock

def F(l,i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

def f(conn):
    conn.send([42, None, 'hello'])
    print(type(conn))
    conn.close()

if __name__ == '__main__':
    lock = Lock()
    
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
    
    for num in range(10):
        Process(target=F, args=(lock, num)).start()