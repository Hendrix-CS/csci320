---
layout: work
type: Project
num: 3
worktitle: Advanced Shell Commands Using Rust
---

Implement the following shell commands as Rust programs in the `part1` project you created [last time]({{site.baseurl}}/projects/rust1):
## `findtext`
* Output every line that contains a specified pattern. The first command-line argument is the fixed-string pattern. Remaining arguments are the names of the files to inspect.
* Source file: `src/bin/findtext.rs` in the `part1` project.

## `order`
* Works like `cat`, except the output lines must be sorted before being output. All lines from all files will be mixed together and then sorted. If the "-r" command-line argument is provided, they should be sorted in reverse order.
* Source file: `src/bin/order.rs` in the `part1` project.

## `webget`
* Downloads web pages and saves them locally.
* Source file: `src/bin/webget.rs` in the `part1` project. 
* Its command-line interface is as follows:

```
Usage: webget [url] 
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
the message is incomplete, and you will not receive a response. The `http` 
protocol requires that each line end with both a carriage return and a linefeed.
Each line in your message, then, should end with `\r\n`, and the last four characters
in your message as a whole should be `\r\n\r\n`. 
 

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

You will need to extract the HTML file from the returned characters. To do so:
* Until you encounter a blank line, print out each header line to the command line.
* Once a blank line is encountered:
  * All lines that follow should be saved in a file.
  * The local filename should be the name of the requested file from the server.

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
use std::io;

fn send_message(host: &str, port: usize, message: &str) -> io::Result<()> {
    let tcp = TcpStream::connect(format!("{}:{}", host, port))?;
    let connector = SslConnector::builder(SslMethod::tls())?.build();
    let mut stream = connector.connect(host, tcp).unwrap();
    stream.write(message.as_bytes())?;
    
    // TODO: ****Write code here to read and process the response from the socket.****
    
    Ok(())
}
```

To read from a socket, I recommend using [BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html).


## Troubleshooting Security

You may get an error message when trying to create an SSL connection about being unable to 
open a trust certificate. This sometimes happens when an aspect of the SSL installation doesn't
give enough clues as to where certificates are stored.

If this occurs, use the [openssl-probe](https://crates.io/crates/openssl-probe) crate to fix
the problem:
* Add this line to `Cargo.toml`:
  * `openssl-probe = "0.1.5"`
* Add this line to your `main()` at the very start:
  * `openssl_probe::init_ssl_cert_env_vars();`

## Design Hints

* Separate the processing of command-line arguments from their implementation.
  * To this end, create a data structure to represent a request. It could contain:
    * The host name
	* The file to retrieve
* Write a function or method to create a string containing the `GET` message to be sent over the socket.
  * This facilitates debugging as well, as it makes it easy to print the `GET` message to the command line.
  
## Submissions
* Share the `part1` project as a **private** GitHub repository.
* Submit your GitHub URL via Teams.

## Assessment
* **Level 1**: Correctly complete any one of the three programs.
* **Level 2**: Correctly complete any two of the three programs.
* **Level 3**: All three programs correctly completed.

------------------------------------------------------------------------
