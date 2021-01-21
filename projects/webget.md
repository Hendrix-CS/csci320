---
layout: work
type: Project
num: 5
worktitle: Webget
---

Write a command-line program called `webget` that downloads web pages and prints 
them out on the command line. Its command-line interface is as follows:

```
Usage: webget [url] [-host=hostaddr] [-file=filepath] [-http] [-https]
  A url parameter results in an immediate request.
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
GET csci320/projects/webget.html HTTP/1.1                                                                               
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
GET csci320/projects/webget.html HTTP/1.1                                                                               
Host: hendrix-cs.github.io                                                                                              

GET csci320/projects/webget.html HTTP/1.1                                                                               
Host: hendrix-cs.github.io                                                                                              
Connection: Close

```



## Submissions
* Create a **private** GitHub repository for your webget program.
* [Submit the repository URL](https://docs.google.com/forms/d/e/1FAIpQLSeCE51hAA4VV1jN_E4pVH1FDB3G6x7-GrIg5_MAP_qqMd6fAg/viewform?usp=sf_link).

## Assessment
* **Partial**: 
* **Complete**: 

------------------------------------------------------------------------
