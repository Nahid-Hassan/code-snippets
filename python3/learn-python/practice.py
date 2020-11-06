import time

start_time = time.time()










mport httplib
except:
    import http.client as httplib

    def checkInternetHttplib(url="www.google.com", timeout=3):
        conn = httplib.HTTPConnection(url, timeout=timeout)
            try:
                    conn.request("HEAD", "/")
                            conn.close()
                                    return True
                                        except Exception as e:
                                                print(e)
                                                        return False


end_time =time.time()
print(start_time - end_time)
