'''
Drawbacks of time.sleep
- the execution time will increase
- there will be unnecessary wait if the web elements are already visible before the sleep time ends

To overcome these drawbacks, we use implicitly_wait(s)
- s is the maximum wait time allowed. so browser will wait for between 0 to s seconds
- making the browser wait internally
- whenever an element is not available, this will come into the picture, and it will make the browser wait until the web element is available to interact
- as soon as the web element is available, it will perform the operation right away
'''