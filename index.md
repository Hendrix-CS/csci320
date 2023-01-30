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
  * Interact directly with the CPU, RAM, keyboard, and monitor on behalf of a user.
  * Operate concurrently without errors.
* Empirically analyze the performance of operating system components.
* Address cybersecurity issues that arise in these contexts.

## <a name="resources">Resources</a>

{% include resources.html content=site.resources %}

<hr>

# NEW: [Interactive Rust Book](https://rust-book.cs.brown.edu/)

# <a name="calendar">Calendar</a>

## Part 1: The Command Line

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 1/18 | Wed | Three Easy Pieces<br>Command Line<br>Files and Directories | [Introduction to Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf) | [Survey](https://forms.gle/xwQESACLYUpc1i9R9)<br>[Shell Commands, introduction]({{site.baseurl}}/projects/shell_commands.html) |  |
| 1/20 | Fri | Processes<br>Pipes<br>I/O Redirection | [Processes](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf) | [Shell Commands, complete]({{site.baseurl}}/projects/shell_commands.html) | Shell Commands, introduction |
|      |
| 1/23 | Mon | Rust<br>File I/O | [Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)<br>[Programming a Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)<br>[Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)<br>[std::fs](https://doc.rust-lang.org/std/fs/index.html) | [Rust Programming 1]({{site.baseurl}}/projects/rust1.html) | Shell Commands, complete |
| 1/25 | Wed | Ownership and Borrowing<br>Strings<br>Buffers | [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)<br>[Read trait](https://doc.rust-lang.org/std/io/trait.Read.html)<br>[String in Rust](https://gjf2a.blogspot.com/2017/02/strings-in-rust.html)<br>[BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html)<br>[BufRead trait](https://doc.rust-lang.org/std/io/trait.BufRead.html) |  |  |
| 1/27 | Fri | Rust Collection Types | [Common Collections](https://doc.rust-lang.org/book/ch08-00-common-collections.html) |  |  |
|      |     
| 1/30 | Mon | Unix Process API | [Process API](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf)<br>[nix crate](https://docs.rs/nix/0.26.2/nix/)<br>[C strings](https://doc.rust-lang.org/std/ffi/struct.CString.html) | [Rust Programming 2]({{site.baseurl}}/projects/rust2.html) | Rust Programming 1 |
| 2/1 | Wed | Unix System Calls | [Direct Execution](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf) |  |  |
| 2/3 | Fri | Files and Directories | [Files and Directories](http://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf) |  |  |
|     |
| 2/6 | Mon | File Descriptors<br>Pipelines | [Pipelines in Rust](https://gjf2a.blogspot.com/2017/02/pipelines-in-rust.html) | [Unix Shell]({{site.baseurl}}/projects/rush.html) | Rust Programming 2 |
| 2/8 | Wed | Data structures in Rust | [Using Structs to Structure Related Data](https://doc.rust-lang.org/book/ch05-00-structs.html)<br>[Enums and Pattern Matching](https://doc.rust-lang.org/book/ch06-00-enums.html) |  |  |
| 2/10 | Fri | Review of Unix Command Line<br>Review of Rust |  |  |  |


## Part 2: The Internet

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 2/13 | Mon | The Internet<br>Downloading a web page | [Overview of TCP/IP](https://www.oreilly.com/library/view/tcpip-network-administration/0596002971/ch01.html)<br>[TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html)<br>[Write trait](https://doc.rust-lang.org/std/io/trait.Write.html) | [Webget](https://hendrix-cs.github.io/csci320/projects/webget) | Unix Shell |
| 2/15 | Wed | Using Transport Layer Security | [Cryptography](http://pages.cs.wisc.edu/~remzi/OSTEP/security-crypto.pdf) |  |  |
| 2/17 | Fri | Threads vs Processes | [Concurrency and Threads](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf) |  |  |
|      |
| 2/20 | Mon | Winter Break: No class |
| 2/22 | Wed | Threads in Rust | [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) | [Web server 1]({{site.baseurl}}/projects/webserver1) | Webget |
| 2/24 | Fri | Locks | [Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf)<br>[Locked Data Structures](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf) |  |  |
|      |
| 2/27 | Mon | Concurrency Problems | [Common Concurrency Problems](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf) |  |  |
| 3/1 | Wed | Performance analysis |  | [Web server 2]({{site.baseurl}}/projects/webserver2) | Web server 1 |


## Part 3: The Kernel

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 3/3 | Fri | Bare metal programming | [A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/)<br>[A Minimal Rust Kernel](https://os.phil-opp.com/minimal-rust-kernel/) |  |  |
|     |
| 3/6 | Mon | VGA Buffer | [VGA Buffer](https://os.phil-opp.com/vga-text-mode/) |  |  |
| 3/8 | Wed | Pluggable Interrupt OS | [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os)<br>[Tracer](https://github.com/gjf2a/bare_metal_tracer) | <!--[Bare metal game]({{site.baseurl}}/projects/baremetalgame)-->Kernel Programming 1 | Web server 2 |
| 3/10 | Fri | Ghost Hunter | [Ghost Hunter](https://github.com/gjf2a/ghost_hunter)<br>[Ghost Hunter Core](https://github.com/gjf2a/ghost_hunter_core) |  |  |
|      |
| 3/13 | Mon | Interrupts | [CPU Exceptions](https://os.phil-opp.com/cpu-exceptions/)<br>[Double Faults](https://os.phil-opp.com/double-fault-exceptions/)<br>[Hardware interrupts](https://os.phil-opp.com/hardware-interrupts/) |  |  |
| 3/15 | Wed | Interrupts |  |  |  |
| 3/17 | Fri | Interrupts |  |  | Kernel Programming 1 |
|      |
| 3/20 | Mon | Spring Break: no class |  |  |  |
| 3/22 | Wed | Spring Break: no class |  |  |  |
| 3/24 | Fri | Spring Break: no class |  |  |  |
|      |
| 3/27 | Mon | TBA |  | Kernel Programming 2  | |
| 3/29 | Wed | Interrupt-based multitasking |  | <!--[Game Kernel]({{site.baseurl}}/projects/game_kernel)--> |  |
| 3/31 | Fri | Paging | [Introduction to Paging (OS in Rust)](https://os.phil-opp.com/paging-introduction/)<br>[Introduction to Paging (OSTEP)](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-paging.pdf) |  |  |
|      |
| 4/3 | Mon | Implementation of Paging | [Paging Implementation](https://os.phil-opp.com/paging-implementation/)<br>[Translation Lookaside Buffers](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf) |  |  |
| 4/5 | Wed | Memory Management: Heap | [Heap Allocation](https://os.phil-opp.com/heap-allocation/) | | |
| 4/7 | Fri | Allocator Designs | [Allocator Designs](https://os.phil-opp.com/allocator-designs/)<br>[Free Space Management](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-freespace.pdf) | Kernel Programming 3  | Kernel Programming 2  |
|     |
| 4/10 | Mon | Garbage Collection |  | |  |
| 4/12 | Wed | Processor Scheduling | [CPU Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) | <!--[Cooperative Multitasking Kernel]({{site.baseurl}}/projects/coop_os)--> |  |
| 4/14 | Fri | Scheduling with Priorities | [Multi-Level Feedback](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf) |  |  |
|      |
| 4/17 | Mon | Randomized Scheduling | [Lottery Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf) |  |  |
| 4/19 | Wed | Final projects |  | Project proposal | Kernel Programming 3 |
| 4/21 | Fri | I/O Devices<br>Hard Disk Drives | [I/O Devices](http://pages.cs.wisc.edu/~remzi/OSTEP/file-devices.pdf)<br>[Hard Disk Drives](http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf) |  |  |
|      |
| 4/24 | Mon | File System | [File System Implementation](http://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf) |  | Project Proposal |
| 4/26 | Wed | Solid-State Drives | [Flash-based SSDs](http://pages.cs.wisc.edu/~remzi/OSTEP/file-ssd.pdf) |  |  |
| 4/28 | Fri | Wrap-up |  |  |  |
|      |
| 5/5  | Fri 2-5 pm | Final Project Presentations | | | |

<hr>
# <a name="assessment">Assessment</a>

## <a name="projects">Projects</a>

A total of 10 projects will be assigned throughout the semester; approximately one 
project per week. Each submission will be assessed as either **Partial** or 
**Complete**. The criteria for these assessments will be given for each assignment.

Each student should have a [GitHub](https://github.com/) account. For each 
programming project, the student should create a **private** GitHub repository to 
store the project. The student should add [Dr. Ferrer](https://github.com/gjf2a) as 
a contributor to the project. When the project is due, he will download the 
repository onto his own machine for grading.

## <a name="finalproject">Final Project</a>
Towards the end of the semester, each student will undertake a final project. There 
are two primary options for the final project:

### Expository Project

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
    - [Fuchsia](https://fuchsia.dev/)
    - [Theseus](https://github.com/theseus-os/Theseus)
	
  * Discuss the motivation for creating each operating system.
  * Discuss how each operating system addresses the topics of Virtualization, Concurrency, and Persistence.
  * Discuss the similarities and differences between them, especially in light of the motivation for their creation.

### Programming Project

  * Implement a working program that extends our exploration of any topic from the course.
    * This may include nontrivial extensions to one of our programming projects.
  * Write a short paper describing the program's purpose and the degree to which it fulfills that purpose.
  
Each student will orally present their final project during the Final Exam period 
for the course, on Friday, May 5, 2023 from 2-5 pm. 

## <a name="grading">Specifications Grading</a>
Each assignment is assessed as **Missing**, **Partial**, or **Complete**. 
Criteria for the latter two categories will be specified for each assignment. Final course grades are earned based on cumulative assignment outcomes:

* To earn an A in the course, a student will:
  * **Complete** the final project
  * **Complete** all 10 regular projects
* To earn a B in the course, a student will: 
  * One of the following:
    * **Complete** the final project, **Complete** at least six other projects,
      including at least two kernel projects, and at least **Partially Complete**
      two more projects.
    * **Partial** completion of the final project, **Complete** all 10 regular projects.
* To earn a C in the course, a student will:
  * One of the following:
    * **Complete** the final project and **Complete** at least four other projects, including at least one kernel project, and at least **Partially Complete** a minimum of two more projects.
    * **Partial** completion of the final project, **Complete** at least six other projects, including at least two kernel projects, and at least **Partially Complete** two more projects.
    * **Missing** final project, **Complete** at least 9 out of 10 regular projects, including all kernel projects; at least **Partially Complete** the remaining project.
* To earn a D in the course, a student will:
  * One of the following:
    * **Complete** the final project, **Complete** at least two regular projects, and at least **Partially Complete** two more projects
    * **Partially Complete** the final project and at least four other projects, including at least one kernel project, and at least **Partially Complete** a minimum of two other projects
    * **Missing** final project, **Complete** at least six other projects, including at least two kernel projects, and at least **Partially Complete** two more projects.
  
## <a name="tokens">Tokens</a>
* Each student starts the semester with three **tokens**. 
* Send Dr. Ferrer a message on Teams to spend a token.
* A student may spend one token in order to:
  * Submit a project after the posted deadline.
    * When you send the message to spend the token, specify a new
      deadline for that project that you plan to meet.
  * Submit a revised version of a project in the event the submission receives
      a **Partial** assessment.
* Scheduling and attending an [office hours meeting](https://drferrer.youcanbook.me) 
  with Dr. Ferrer earns one additional token.
* **Note**: All late submissions/revisions must be received before 5 pm on Tuesday, 
  May 9, the last day of the semester.
