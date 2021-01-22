---
layout: work
type: Project
num: 5
worktitle: Webget
---

Write a command-line program called `webget` that downloads web pages and prints 
them out on the command line. Its command-line interface is as follows:

```
Usage: webget [url] [-host=hostaddr] [-file=filepath] [-port=number] [-http] [-https]
  A url parameter results in an immediate request.
  A port parameter redirects the default port to the specified number.
  A more complex request is set up by first designating a host and files,
  then selecting whether to use the http or https protocol.
```

Web pages are retrieved using the `GET` command in the `HTTP` protocol. Here is 
the basic structure of a `GET`:

```
GET [file] HTTP/1.1
Host: [hostname]
Connection: Close

```

For example, if we wish to retrieve this web page, we might issue the following command:

```
webget https://hendrix-cs.github.io/csci320/projects/webget.html
```

Note that the protocol is `https`, the host is `hendrix-cs.github.io`, and the requested
file is `csci320/projects/webget.html`.

Given that command, `webget` would send the following `GET` message:

```
GET /csci320/projects/webget.html HTTP/1.1                                                                               
Host: hendrix-cs.github.io                                                                                              
Connection: Close

```

**Note**: There is a blank line after the `Connection: Close` line. Without this blank line,
the message is incomplete, and you will not receive a response. 

An alternative invocation of `webget` with the same effect would be:

```
webget -host=hendrix-cs.github.io -file=csci320/projects/webget -https
```

This alternative format allows us to request more than one file at a time. For example:

```
webget -host=hendrix-cs.github.io -file=csci320/projects/webget -file=csci320/projects/rush.html -https
```

Given that command, `webget` would send two `GET` messages:

```
GET /csci320/projects/webget.html HTTP/1.1                                                                               
Host: hendrix-cs.github.io                                                                                              

GET /csci320/projects/webget.html HTTP/1.1                                                                               
Host: hendrix-cs.github.io                                                                                              
Connection: Close

```

## Alternate Port Numbers

Regular `http` requests default to port 80, and regular `https` requests default to port 443. But sometimes a 
web server runs on a different port. Our program should allow the user to specify an alternative port number,
either through the URL or a command-line argument. For example:

```
webget https://hendrix-cs.github.io:8888/csci320/projects/webget.html
```

This requests the page using port 8888. The same request in the command-line format would be:

```
webget -host=hendrix-cs.github.io -file=csci320/projects/webget -port=8888 -https
```

## Responses

When a file is successfully retrieved, you will first receive an HTTP header before the file contents. 
Here is the beginning of a sample HTTP header:

```
HTTP/1.1 200 OK                                                                                                         Connection: close                                                                                                       Content-Length: 14140                                                                                                   
Server: GitHub.com                                                                                                      
Content-Type: text/html; charset=utf-8                                                                                  
Strict-Transport-Security: max-age=31556952                                                                             
last-modified: Thu, 21 Jan 2021 00:44:30 GMT
```

You will need to extract each HTML file from the returned characters. To do so:
* When you encounter a line that starts with the string `HTTP/1.1`:
  * Print out the header line.
  * Skip all following lines until a blank line is encountered.
* Once a blank line is encountered:
  * All lines that follow should be saved in a file, until either:
    * Another header line is encountered, or:
	* No lines remain.
* The first file should be named `file1.html`, the second `file2.html`, and so forth.

## Security

The original `http` protocol had no security features. Messages could easily be inspected while in transit. The 
`https` protocol superimposes the `http` protocol atop the 
[Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) protocol. TLS provides
end-to-end encryption to prevent messages from being inspected in transit.

Place the following line in the `dependencies` section of your `Cargo.toml` to use the [OpenSSL](https://crates.io/crates/openssl) crate:
```
openssl = { version = "0.10", features = ["vendored"] }
```

On Windows, you'll want to compile under Windows Subsystem for Linux to facilitate the installation. Setting up
OpenSSL is otherwise extremely annoying under Windows.

Using sockets secured by TLS is straightforward:

```
use openssl::ssl::{SslConnector, SslMethod};

let tcp = TcpStream::connect("hendrix-cs.github.io:443");
let connector = SslConnector::builder(SslMethod::tls())?.build();
let mut stream = connector.connect(host, self.get_tcp_stream(host)?).unwrap();
```

From here, you can use `stream` as if it were a regular TCP socket. The `http` protocol is otherwise unchanged.

## Design Hints

* Separate the processing of command-line arguments from their implementation.
  * To this end, create a data structure to represent a request. It could contain:
    * The host name
	* A list of files to retrieve
	* Whether it is using `http` or `https`
* Whether one encounters a URL or the other command-line arguments, build the same data structure.
* Write a function or method to create a string containing the `GET` message to be sent over the socket.
  * This facilitates debugging as well, as it makes it easy to print the `GET` message to the command line.
* Work incrementally
  * Get the program working with the simplest command-line arguments first.
  * Once the basic version works, then add multi-file downloads, security, URL parsing, and alternate port numbers.
  
## Checklist

* Downloads web pages using `http`.
* Downloads web pages securely using `https`.
* Specifies web pages using specialized command-line arguments.
* Specifies web pages using a URL.
* Saves downloaded pages onto one local file per page.
* Enables the use of alternate port numbers.
* Downloads multiple web pages from a single server.

## Submissions
* Create a **private** GitHub repository for your webget program.
* [Submit the repository URL](https://docs.google.com/forms/d/e/1FAIpQLSeCE51hAA4VV1jN_E4pVH1FDB3G6x7-GrIg5_MAP_qqMd6fAg/viewform?usp=sf_link).

## Assessment
* **Partial**: Any four items from the checklist.
* **Complete**: All items from the checklist.

------------------------------------------------------------------------
