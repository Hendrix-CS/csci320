---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-single
---

# <a name="description">Overview</a>

{{ site.description }}

## <a name="goals">Learning Goals</a>

Upon completing this course, our goal is for you to be able to:

* Describe how an operating system mediates interaction with:
  * CPU and RAM through the **process** abstraction
  * Hard disk and Flash memory through the **file system** abstraction.
  * The Internet through the **TCP socket** abstraction.
* Write useful programs that:
  * Deliver operating system services to a user.
  * Interact directly with the CPU, keyboard, monitor, and RAM.
  * Operate concurrently without errors.
* Empirically analyze the performance of operating system components.
* Address cybersecurity issues that arise in these contexts.

## <a name="resources">Resources</a>

{% include resources.html content=site.resources %}

<hr>

# <a name="calendar">Calendar</a>

## Part 1: The Command Line

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 1/20 | Wed | Three Easy Pieces<br>Command Line<br>Files and Directories | [Introduction to Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf) | [Shell Commands, introduction]({{site.baseurl}}/projects/shell_commands.html) |  |
| 1/22 | Fri | Processes<br>Pipes<br>I/O Redirection | [Processes](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf) | [Shell Commands, complete]({{site.baseurl}}/projects/shell_commands.html) | Shell Commands, introduction |
| 1/25 | Mon | Rust<br>File I/O | [Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)<br>[Programming a Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)<br>[Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)<br>[std::fs](https://doc.rust-lang.org/std/fs/index.html) | [Rust Programming 1]({{site.baseurl}}/projects/rust1.html) | Shell Commands, complete |
| 1/27 | Wed | Ownership and Borrowing<br>Strings<br>Buffers | [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)<br>[Read trait](https://doc.rust-lang.org/std/io/trait.Read.html)<br>[String in Rust](https://gjf2a.blogspot.com/2017/02/strings-in-rust.html)<br>[BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html)<br>[BufRead trait](https://doc.rust-lang.org/std/io/trait.BufRead.html) |  |  |
| 1/29 | Fri | Rust Collection Types | [Common Collections](https://doc.rust-lang.org/book/ch08-00-common-collections.html) |  |  |
| 2/1 | Mon | Unix Process API | [Process API](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf)<br>[nix crate](https://docs.rs/nix/0.19.1/nix/)<br>[C strings](https://doc.rust-lang.org/std/ffi/struct.CString.html) | [Rust Programming 2]({{site.baseurl}}/projects/rust2.html) | Rust Programming 1 |
| 2/3 | Wed | Unix System Calls | [Direct Execution](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf) |  |  |
| 2/5 | Fri | Break: no class |  |  |  |
| 2/8 | Mon | Files and Directories | [Files and Directories](http://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf) |  |  |
| 2/10 | Wed | File Descriptors<br>Pipelines | [Pipelines in Rust](https://gjf2a.blogspot.com/2017/02/pipelines-in-rust.html) | [Unix Shell]({{site.baseurl}}/projects/rush.html) | Rust Programming 2 |
| 2/12 | Fri | Data structures in Rust | [Using Structs to Structure Related Data](https://doc.rust-lang.org/book/ch05-00-structs.html)<br>[Enums and Pattern Matching](https://doc.rust-lang.org/book/ch06-00-enums.html) |  |  |
| 2/15 | Mon | Review of Unix Command Line<br>Review of Rust |  |  |  |


## Part 2: The Internet

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 2/17 | Wed | The Internet<br>Downloading a web page | [Overview of TCP/IP](https://www.oreilly.com/library/view/tcpip-network-administration/0596002971/ch01.html)<br>[TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html)<br>[Write trait](https://doc.rust-lang.org/std/io/trait.Write.html) | Webget | Unix Shell |
| 2/19 | Fri | Using Transport Layer Security | [Cryptography](http://pages.cs.wisc.edu/~remzi/OSTEP/security-crypto.pdf) |  |  |
| 2/22 | Mon | Threads vs Processes | [Concurrency and Threads](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf) |  |  |
| 2/24 | Wed | Threads in Rust | [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) | Web server 1 | Webget |
| 2/26 | Fri | Locks | [Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf)<br>[Locked Data Structures](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf) |  |  |
| 3/1 | Mon | Concurrency Problems | [Common Concurrency Problems](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf) |  |  |
| 3/3 | Wed | Performance analysis |  | Web server 2 | Web server 1 |


## Part 3: The Kernel

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 3/5 | Fri | Bare metal programming | [A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/)<br>[A Minimal Rust Kernel](https://os.phil-opp.com/minimal-rust-kernel/) |  |  |
| 3/8 | Mon | VGA Buffer | [VGA Buffer](https://os.phil-opp.com/vga-text-mode/) |  |  |
| 3/10 | Wed | Pluggable Interrupt OS | [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os)<br>[Tracer](https://github.com/gjf2a/bare_metal_tracer) | Bare metal game | Web server 2 |
| 3/12 | Fri | Ghost Hunter | [Ghost Hunter](https://github.com/gjf2a/ghost_hunter)<br>[Ghost Hunter Core](https://github.com/gjf2a/ghost_hunter_core) |  |  |
| 3/15 | Mon | Interrupts | [CPU Exceptions](https://os.phil-opp.com/cpu-exceptions/)<br>[Double Faults](https://os.phil-opp.com/double-fault-exceptions/)<br>[Hardware interrupts](https://os.phil-opp.com/hardware-interrupts/) |  |  |
| 3/17 | Wed | Game Demo Day |  |  | Bare metal game check-in |
| 3/19 | Fri | Interrupts |  |  |  |
| 3/22 | Mon | Final Game Demos |  |  | Bare metal game |
| 3/24 | Wed | Break: no class |  |  |  |
| 3/26 | Fri | Interrupt-based multitasking |  | Game Kernel |  |
| 3/29 | Mon | Paging | [Introduction to Paging (OS in Rust)](https://os.phil-opp.com/paging-introduction/)<br>[Introduction to Paging (OSTEP)](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-paging.pdf) |  |  |
| 3/31 | Wed | Implementation of Paging | [Paging Implementation](https://os.phil-opp.com/paging-implementation/)<br>[Translation Lookaside Buffers](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf) |  |  |
| 4/2 | Fri | Memory Management: Heap | [Heap Allocation](https://os.phil-opp.com/heap-allocation/) | Heap | Game Kernel |
| 4/5 | Mon | Allocator Designs | [Allocator Designs](https://os.phil-opp.com/allocator-designs/)<br>[Free Space Management](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-freespace.pdf) |  |  |
| 4/7 | Wed | Garbage Collection |  |  |  |
| 4/9 | Fri | Processor Scheduling | [CPU Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) | Scheduling | Heap |
| 4/12 | Mon | Scheduling with Priorities | [Multi-Level Feedback](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf) |  |  |
| 4/14 | Wed | Randomized Scheduling | [Lottery Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf) |  |  |
| 4/16 | Fri | Final projects |  | Project proposal | Scheduling |
| 4/19 | Mon | I/O Devices<br>Hard Disk Drives | [I/O Devices](http://pages.cs.wisc.edu/~remzi/OSTEP/file-devices.pdf)<br>[Hard Disk Drives](http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf) |  |  |
| 4/21 | Wed | File System | [File System Implementation](http://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf) | File System | Project Proposal |
| 4/23 | Fri | Break: no class |  |  |  |
| 4/26 | Mon | Solid-State Drives | [Flash-based SSDs](http://pages.cs.wisc.edu/~remzi/OSTEP/file-ssd.pdf) |  |  |
| 4/28 | Wed | Famous OSs |  |  |  |
| 4/30 | Fri | Wrap-up |  |  | File System |
| 5/10 | Mon | Final Project Presentations | | | |

<hr>
# <a name="assessment">Assessment</a>

## <a name="projects">Projects</a>

A total of 12 projects will be assigned throughout the semester; approximately one project 
per week. Each submission will be assessed as either **Partial** or **Complete**. The criteria
for these assessments will be given for each assignment.

Each student should have a [GitHub](https://github.com/) account. For each programming project,
the student should create a **private** GitHub repository to store the project. The student
should add [Dr. Ferrer](https://github.com/gjf2a) as a contributor to the project. When the 
project is due, he will download the repository onto his own machine for grading.

## <a name="finalproject">Final Project</a>
Towards the end of the semester, each student will undertake a final project. There are
two primary options for the final project:
1. **Expository Project**
  * Select two different operating systems to research. One must be from this list of established operating systems:
	- [Minix](https://www.minix3.org/)
	- [FreeBSD](https://www.freebsd.org/)
	- [Debian](https://www.debian.org/)
	- [Ubuntu](https://ubuntu.com/)
	- [Red Hat](https://www.redhat.com/en)
	- [Microsoft Windows](https://www.microsoft.com/en-us/windows)
	- [Macintosh OS](https://www.apple.com/macos/big-sur/)
	- [Android](https://www.android.com/)
	- [iOS](https://www.apple.com/ios/ios-14/)
  * The other should be from this list of innovating operating systems:
    - [seL4](https://sel4.systems/)
    - [Redox](https://www.redox-os.org/)
	- [Theseus](https://github.com/theseus-os/Theseus)
  * Discuss the motivation for creating each operating system.
  * Discuss how each operating system addresses the topics of Virtualization, Concurrency, and Persistence.
  * Discuss the similarities and differences between them, especially in light of the motivation for their creation.
2. **Programming Project**:
  * Implement a working program that extends our exploration of any topic from the course.
    * This may include nontrivial extensions to one of our programming projects.
  * Write a short paper describing the program's purpose and the degree to which it fulfills that purpose.
  
Each student will orally present their final project during the Final Exam period for the 
course, on Monday, May 10, 2021 from 2-5 pm. 

## <a name="participation">Course Participation</a>

* Each student should schedule and attend at least three online Office Hour meetings with the instructor at some point during the semester.


## <a name="grading">Specifications Grading</a>
Each assignment is assessed as **Missing**, **Partial**, or **Complete**. 
Criteria for the latter two categories will be specified for each assignment. Final course
grades are earned based on cumulative assignment outcomes:

* To earn an A in the course, a student will:
  * One of the following:
    * **Complete** the final project and **Complete** at least 10 other projects.
	* **Partial** completion of the final project, and **Complete** all 12 other projects.
  * No **Missing** projects
  * Schedule and attend at least three Office Hours meetings
  * Submit a course feedback form
* To earn a B in the course, a student will: 
  * One of the following:
    * **Complete** the final project and **Complete** at least four other projects
    * **Partial** completion of the final project, and **Complete** at least eight other projects
  * At most two **Missing** projects
  * Schedule and attend at least two Office Hours meetings
  * Submit a course feedback form
* To earn a C in the course, a student will:
  * One of the following:
    * **Complete** the final project and **Complete** at least two other projects
	* **Partial** completion of the final project, and **Complete** at least four other projects
	* **Missing** final project, and **Complete** at least eight other projects
  * At most four **Missing** projects
  * Schedule and attend at least one Office Hours meeting
  * Submit a course feedback form
* To earn a D in the course, a student will:
  * One of the following:
    * **Complete** the final project, and **Partial** completion of at least four other projects
	* **Partial** completion of the final project, and **Partial** completion of at least six other projects
	* **Missing** final project, and **Partial** completion of at least eight other projects

### Revising submitted work
If a submitted project receives a **Partial** assessment and the student seeks a **Complete** assessment:
* The student will schedule and attend an Office Hours meeting to discuss the necessary revisions and establish a deadline for their submission.
* If the student submits the revisions by the agreed deadline, the revised project will receive a **Complete** assessment.

## <a name="latedays">Late Policy</a>
If a student needs an extension, the instructor must be notified by email or Teams message by 
4 pm on the day prior to the due date. This notification email must state the duration of the 
requested extension. The instructor reserves the right to decline a request for an extension, 
but the intention is that most requests for extensions will be granted.
