---
layout: work
type: Project
num: 6
worktitle: Web Server Part 1
---

Write a command-line program called `webserver`. This program will listen for `http` requests
on port 8888. To achieve this, set up a 
[TcpListener](https://doc.rust-lang.org/std/net/struct.TcpListener.html) that is bound to 
`localhost:8888`. 

## Step 1: Listen

When your server receives a connection, it should print the IP address of the peer that 
contacted it. Test it using your [webget]({{site.baseurl}}/projects/webget) program as follows:

```
webget http://localhost:8888/test
```

Since `webget` is running on the same machine, you can send the message to `localhost` and it
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

## Submissions
* Create a **private** GitHub repository for your webserver program.
* [Submit the repository URL](https://docs.google.com/forms/d/e/1FAIpQLSffhU9tDv0VnoRcVtzLG_afhpMdQX1oijR8nb_Hab6Vhbbcvg/viewform?usp=sf_link)

## Assessment
* **Partial**: Steps 1-4 complete.
* **Complete**: All six steps complete.

## Acknowledgement

This assignment was adapted from [materials](http://rust-class.org/pages/ps1.html) developed by 
[David Evans](http://www.cs.virginia.edu/~evans/) at the 
[University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

------------------------------------------------------------------------
