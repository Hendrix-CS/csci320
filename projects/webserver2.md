---
layout: work
type: Project
num: 7
worktitle: Web Server Part 2
---

In this project, you will seek to improve the performance of your 
[webserver](https://hendrix-cs.github.io/csci320/projects/webserver1) program.

## Creating Benchmarks

Use [locust.io](https://locust.io/) to test the performance of your server. This program 
allows you to [write Python scripts to describe workload tests](https://docs.locust.io/en/stable/quickstart.html). 
It will then spawn as many test users as you would like. Install it on the command line on a machine with 
Python3 installed:

```
python3 -m pip install locust
```

**Windows Subsystem for Linux only**: If that command yields an error message, try the following first (in `bash`):
```
sudo apt update
sudo apt install python3-pip
```

(You can also install it [directly from PyCharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html),
but the `locust` command-line program will not be readily invocable.)

Once it is installed, you can write a Python program as a configuration file. For example:

```
from locust import HttpUser, task

class WebsiteUser(HttpUser):
    @task(2)
    def f100(self):
        self.client.get("/file100.html")

    @task
    def f1000(self):
        self.client.get("/file1000.html")
```

This program issues GET requests for the files `file100.html` and `file1000.html`. It issues requests 
for `file100.html` twice as often as requests for `file1000.html`.  

To run a test using the above program (named `benchmark1.py`), 
assuming a server running on your own machine and listening to port 8888, type:

```
locust -f benchmark1.py --host=http://localhost:8888
```

When you execute this, the UI for the program will be viewable through your web browser at 
`http://localhost:8089/`. From there, you specify the number of users to simulate and the number 
of users created per second. The test will continue indefinitely until you stop it. It will give 
you a nice summary of the test results.

Devise at least three different performance workloads using [locust.io](https://locust.io/). Feel free
to use these [files of varying sizes]({{site.baseurl}}/projects/workloads.zip) in creating your 
performance workloads.

Note that, in general, it is best to run your tests on a different machine than that which is running your 
server. Each of your workloads should represent a different type of stress on the server.

## Baseline

Measure the performance of `webserver` as it stands, without modifications.

## Streaming Files

The most straightforward implementation of a web server is to read the entire requested file into 
RAM from the disk, then send the file over the socket. For large files, this can be undesirable for
several reasons:
* It increases the amount of RAM the server uses.
* The client must wait until the entire file arrives before it can begin to process it.

Modify your server so that it reads a fixed number of bytes from the disk at a time, then sends
those same bytes to the client. Add a command-line flag (`-s`) to switch streaming on. In the absence
of the flag, it should read the entire file into RAM and then send it.

## Caching

As reading from disk is time consuming, potential speedup gains may be had by caching frequently
requested files in RAM. There are some significant tradeoffs involved:
* Caching files can greatly increase the amount of RAM the server uses.
* Caching popular files tends to have a larger payoff.
* It is possible that a cached file will have changed on disk, making the results out-of-date.

Modify your server so that it stores up to `n` files in a RAM cache. The value `n` is selected at the 
command line; add a command line flag (`-c=n`) to specify that value. For example, `c=3` would allow
the cache to store up to three files. If the `-c` flag is not employed, caching will not be activated.

Track the number of requests for each file. The `n` most popular files will be kept in the cache.

## Submissions
* Push your enhancements to the same GitHub repository you used for `webserver` in the previous assignment.
* Include a PDF file in your repository describing the following:
  * What were your three benchmark workloads? Include the Python source code of your `locust` jobs.
  * What was the performance of your basic implementation?
  * What was the performance impact of streaming?
  * What was the performance impact of caching?
  * What conclusions do you draw from your experiments?

## Assessment
* **Partial**: Created benchmark workloads. Implemented either caching or streaming. Described workloads and performance in the paper.
* **Complete**:  Implemented both caching and streaming. Analysis is complete and comprehensive.

## Acknowledgement

This assignment was adapted from [materials](http://rust-class.org/pages/ps3.html) developed by 
[David Evans](http://www.cs.virginia.edu/~evans/) at the 
[University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

------------------------------------------------------------------------
