---
layout: work
type: Project
num: 6
worktitle: Web Server Part 1
---

Write a command-line program called `webserver`. This program will listen for `https` requests
on port 8888. To achieve this, set up a 
[TcpListener](https://doc.rust-lang.org/std/net/struct.TcpListener.html) that is bound to 
`localhost:8888`. 

## Step 1: Listen

When your server receives a connection, it should print the IP address of the peer that 
contacted it. Test it using your [webget]({{site.baseurl}}/projects/webget) program as follows:

```
webget -host=localhost -port=8888 -file=test -http
```

Since `webget` is running on the same machine, you can send the message to `localhost` and it
will look for a server on the local machine. Since the server is not actually going to send
any data, the filename doesn't matter. Using `http` avoids a panic when it does not receive 
a TLS secured connection.

## Step 2: Display Message

Refine your program as follows:
* Whenever it receives a connection, the program should [spawn a new thread](https://doc.rust-lang.org/std/thread/)
  to handle the connection.
* In this new thread, it should await a message from the client. I recommend using 
  [read()](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read) with a 500-byte buffer. 
  Using read_to_end() and read_to_string() can result in a hanging connection when dealing with certain clients.
* It should then print the message it received.

In the above example, it would print somemthing akin to the following:

```
client IP address: 127.0.0.1:60632                                                                                      
Read 54 bytes from 127.0.0.1:60632                       
GET /test HTTP/1.1                                     
Host: localhost                                                                                                         
Connection: Close

```

## Step 3: Respond
  
Once the client message is received, the server should reply to the client with the following:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
<body>
<h1>Message received</h1>
Client address: [Insert client address here]<br>
Requested file: [Insert file request element of the GET here]<br>
</body>
</html>
```

In our example from earlier, the response would be:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
<body>
<h1>Message received</h1>
Client address: 127.0.0.1:60632<br>
Requested file: /test<br>
</body>
</html>
```

## Step 4: Validate File Requests

In principle, a web server can send any file on the machine it is running to anyone on the Internet. 
To prevent this, we need to **validate** the file requests. The requested file will be assumed to be 
relative to the current working directory for the executing server. The server should determine the 
**absolute path** of the resulting file and **guarantee** that it is subordinate to the server's current 
working directory.  

If a request is valid add the message `Request Valid` to the reply from the previous tep. If not, send a
message with the header `HTTP/1.1 403 Forbidden` Instead of `HTTP/1.1 200 OK`.

## Step 5: Counter

## Step 6: Send files

## Step 7: Transport Layer Security

Setting up Transport Layer Security requires two key elements:
* A private key
* An authentication certificate

To generate the private key at the Unix command line:
```
openssl genrsa 2048 > key.pem
```

Once the private key is generated, generate a test certificate. (A real certificate would be issued by a 
third-party authority that guarantees that the web server is running at the site it claims.)
```
openssl req -x509 -days 1000 -new -key key.pem -out certs.pem
```

Once you have generated these files, you can set up TLS when accepting connections as 
[described in the documentation](https://docs.rs/openssl/0.10.16/openssl/ssl/index.html).

## Submissions
* Create a **private** GitHub repository for your webserver program.
* [Submit the repository URL]()

## Assessment
* **Partial**: Steps 1-5 complete.
* **Complete**: All seven steps complete.

------------------------------------------------------------------------
