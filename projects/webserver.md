---
layout: work
type: Project
num: 5
worktitle: Web Server 
---

Write a command-line program called `webserver`. 
* Source file: `src/bin/webserver.rs` in the `part1` project.

This program will listen for `http` requests
on port 8888. To achieve this, you will set up a 
[TcpListener](https://doc.rust-lang.org/std/net/struct.TcpListener.html) that is bound to 
`localhost:8888`. 

## Step 1: Listen

When your server receives a connection, it should print the IP address of the peer that 
contacted it. Open a second shell, then test it using 
[wget](https://www.gnu.org/software/wget/manual/wget.html) as follows:

```
wget http://localhost:8888/test
```

Since `wget` is running on the same machine, you can send the message to `localhost` and it
will look for a server on the local machine. Since the server is not actually going to send
any data, the filename doesn't matter. Using `http` avoids a panic when it does not receive 
a TLS secured connection.

Note that you can also make this request using your web browser. Just paste 
`http://localhost:8888/test` into its URL bar.

## Step 2: Display Message

Refine your program as follows:
* Whenever it receives a connection, the program should [spawn a new thread](https://doc.rust-lang.org/std/thread/)
  to handle the connection.
* In this new thread, it should await a message from the client. Create a mutable
  `String` to store the accumulated message. Then, within a loop:
  * Use [read()](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read) 
  with a 500-byte buffer. 
  * Use [`std::str::from_utf8`](https://doc.rust-lang.org/std/str/fn.from_utf8.html)
    to convert the buffer into a `&str`.
  * Use the [`push_str()`](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str)
  method to append it to the accumulated message.
  * As the client is awaiting a reply, it will not close the
  connection. Even after it finishes its transmission, the `read()` will still block,
  waiting for more data.  Since the `http` protocol specifies that a client's message ends with
  the character sequence `\r\n\r\n`, once the accumulated message 
  [contains](https://doc.rust-lang.org/std/string/struct.String.html#method.contains)
  that sequence, the loop can end. As some clients end with `\n\n`, the `http`
  specification allows servers to end with that sequence too. 
* It should then print the message it received.

In response to the `wget` command above, it would print somemthing akin to the following:

```
Client IP address: 127.0.0.1:44822
Read 133 bytes from 127.0.0.1:44822
GET /test HTTP/1.1
Host: localhost:8888
User-Agent: Wget/1.21.2
Accept: */*
Accept-Encoding: identity
Connection: Keep-Alive
```

If you use a different client, such as a web browser, the message may look very different. But it should 
unambiguously be an HTTP request.

## Step 3: Respond
  
Once the client message is received, the server should reply to the client with the following:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: [Number of bytes in HTML message]

<html>
<body>
<h1>Message received</h1>
Requested file: [Insert file request element of the GET here]<br>
</body>
</html>
```

In our example from earlier, the response would be:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 82

<html>
<body>
<h1>Message received</h1>
Requested file: /test<br>
</body>
</html>
```

I recommend testing your server at this stage using your web browser, so you can see the 
result of rendering the HTML.

## Step 4: Validate File Requests

In principle, a web server can send any file on the machine it is running to anyone on the Internet. 
To prevent this, we need to **validate** the file requests. The requested file will be assumed to be 
relative to the current working directory for the executing server. The server should determine the 
**absolute path** of the resulting file and **guarantee** that it is subordinate to the server's current 
working directory.  

The [PathBuf](https://doc.rust-lang.org/std/path/struct.PathBuf.html) data type has several 
methods that you may find helpful in validating the file request.

If the file does not exist, send a message with the header `HTTP/1.1 404 Not Found`.
If the file exists but it violates our security policy, send a message with the 
header `HTTP/1.1 403 Forbidden`.

In practice, if the file requested by the client is a directory, it will return the file
`index.html` from within that directory. For this assignment, it is acceptable to return
`HTTP/1.1 404 Not Found` if the client requests a directory.

## Step 5: Counter

Maintain two counters:
* Total number of requests.
* Total number of valid requests.

Whenever the server answers a client request, it will add one to the `total-request` counter.
If the client request is valid, it will also add one to the `valid-request` counter.

You can store these as two separate variables, or you can aggregate them into a single `struct`. 
Because each client thread will need to access them, they will need to be wrapped with an
[`Arc` and a `Mutex`](https://doc.rust-lang.org/book/ch16-03-shared-state.html).

The server should print the counts to the command line every time it receives a request.

## Step 6: Send files

If the request is valid, and the request is for a file, the server should send back the 
contents of the file. You may assume that all requested files are text files.

Constructing the header requires specifying the number of bytes in the file. The 
[`metadata()`](https://doc.rust-lang.org/std/path/struct.PathBuf.html#method.metadata)
method of `PathBuf` enables you to obtain this number.

<!---
## Step 7: Transport Layer Security

This stuff is interesting and worthwhile but not the best use of my time right now.

Key URLs:
* https://docs.rs/openssl/0.10.16/openssl/ssl/index.html
* https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/
* https://manuals.gfi.com/en/kerio/connect/content/server-configuration/ssl-certificates/adding-trusted-root-certificates-to-the-server-1605.html

Setting up Transport Layer Security requires two key elements:
* A private key
* An authentication certificate

To generate the private key at the Unix command line:
```
openssl genrsa 2048 > private_key.pem
```

Once the private key is generated, generate a public key. 
* When you run this command, it will ask you a number of authentication questions, which 
  you should answer reasonably.
* In practice, public keys are generated by a third-party authority that guarantees that the 
web server is running at the site it claims. But that is well outside the scope 
of this assignment.
```
openssl req -x509 -days 1000 -new -key private_key.pem -out public_key.pem
```

Once you have generated these files, you can set up TLS when accepting connections as 
[described in the documentation](https://docs.rs/openssl/0.10.16/openssl/ssl/index.html).
-->

## Step 7: Creating Benchmarks
Use [locust.io](https://locust.io/) to test the performance of your server. This program 
allows you to [write Python scripts to describe workload tests](https://docs.locust.io/en/stable/quickstart.html). 
It will then spawn as many test users as you would like. 

To install `locust` on **Windows Subsystem for Linux**, at the command prompt, type:
```
sudo apt install python3-locust
```

If, when you run `locust`, you get the following error:
```
[2025-03-06 13:39:05,531] 20003LPUX/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
Traceback (most recent call last):
  File "/usr/bin/locust", line 33, in <module>
    sys.exit(load_entry_point('locust==1.4.3', 'console_scripts', 'locust')())
  File "/usr/lib/python3/dist-packages/locust/main.py", line 286, in main
    web_ui = environment.create_web_ui(
  File "/usr/lib/python3/dist-packages/locust/env.py", line 165, in create_web_ui
    self.web_ui = WebUI(
  File "/usr/lib/python3/dist-packages/locust/web.py", line 102, in __init__
    app.jinja_options["extensions"].append("jinja2.ext.do")
KeyError: 'extensions'
```

Then update your installation as follows:
```
sudo apt remove locust
python3 -m pip install --upgrade locust
```

After the above, I would expect it to work.

On a Mac:
```
python3 -m pip install locust
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

### Baseline

Measure the performance of `webserver` as it stands, without modifications.

## Step 8: Streaming Files

The most straightforward implementation of a web server is to read the entire requested file into 
RAM from the disk, then send the file over the socket. For large files, this can be undesirable for
several reasons:
* It increases the amount of RAM the server uses.
* The client must wait until the entire file arrives before it can begin to process it.

Modify your server so that it reads a fixed number of bytes from the disk at a time, then sends
those same bytes to the client. Add a command-line flag (`-s`) to switch streaming on. In the absence
of the flag, it should read the entire file into RAM and then send it.

### Streaming performance

Measure the performance of `webserver` with streaming activated. In an evaluation document,
record the performance of the baseline and the streaming server. Then analyze the extent
to which streaming was (or was not) helpful.

## Step 9: Caching

As reading from disk is time consuming, potential speedup gains may be had by caching frequently
requested files in RAM. There are some significant tradeoffs involved:
* Caching files can greatly increase the amount of RAM the server uses.
* Caching popular files tends to have a larger payoff.
* It is possible that a cached file will have changed on disk, making the results out-of-date.

Modify your server so that it stores up to `n` files in a RAM cache. The value `n` is selected at the 
command line; add a command line flag (`-c=n`) to specify that value. For example, `c=3` would allow
the cache to store up to three files. If the `-c` flag is not employed, caching will not be activated.

Track the number of requests for each file. The `n` most popular files will be kept in the cache.

### Caching performance

Measure the performance of `webserver` with caching activated. In an evaluation document,
record the performance of the baseline and the caching server. Then analyze the extent
to which caching was (or was not) helpful. Be sure to try at least three different values 
of `n`.


## Submissions
* Share the `part1` project as a **private** GitHub repository.
* Submit your GitHub URL via Teams.

## Assessment
* **Level 1**: Steps 1-6 complete.
* **Level 2**: Step 7 and either Step 8 or Step 9 complete, along with an evalution document
containing a good analysis of the results.
* **Level 3**: All 9 steps complete, along with an evalution document
containing a good analysis of the results.

## Acknowledgement

This assignment was adapted from [materials](http://rust-class.org/pages/ps1.html) developed by 
[David Evans](http://www.cs.virginia.edu/~evans/) at the 
[University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

------------------------------------------------------------------------
