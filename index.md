---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-multi
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
| 1/20 | Wed | Three Easy Pieces<br>Command Line<br>Files and Directories | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf">2: Introduction to Operating Systems</a> | Shell Commands, introduction |  |
| 1/22 | Fri | Processes<br>Pipes<br>I/O Redirection | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf">4: Processes</a> | Shell Commands, complete | Shell Commands, introduction |
| 1/25 | Mon | Rust<br>File I/O | <a href="https://doc.rust-lang.org/book/ch01-00-getting-started.html">Getting Started</a><br><a href="https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html">Programming a Guessing Game</a><br><a href="https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html">Common Programming Concepts</a><br><a href="https://doc.rust-lang.org/std/fs/index.html">std::fs</a> | Rust Programming 1 | Shell Commands, complete |
| 1/27 | Wed | Ownership and Borrowing<br>Strings<br>Buffers | <a href="https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html">Understanding Ownership</a><br><a href="https://doc.rust-lang.org/std/io/trait.Read.html">Read trait</a><br><a href="https://gjf2a.blogspot.com/2017/02/strings-in-rust.html">String in Rust</a><br><a href="https://doc.rust-lang.org/std/io/struct.BufReader.html">BufReader</a><br><a href="https://doc.rust-lang.org/std/io/trait.BufRead.html">BufRead trait</a> |  |  |
| 1/29 | Fri | Rust Collection Types | <a href="https://doc.rust-lang.org/book/ch08-00-common-collections.html">Common Collections</a> |  |  |
| 2/1 | Mon | Unix Process API | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf">5: Process API</a><br><a href="https://docs.rs/nix/0.19.1/nix/">nix crate</a><br><a href="https://doc.rust-lang.org/std/ffi/struct.CString.html">C strings</a> | Rust Programming 2 | Rust Programming 1 |
| 2/3 | Wed | Unix System Calls | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf">6: Direct Execution</a> |  |  |
| 2/5 | Fri | Break: no class |  |  |  |
| 2/8 | Mon | Files and Directories | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf">39: Files and Directories</a> |  |  |
| 2/10 | Wed | File Descriptors<br>Pipelines | <a href="https://gjf2a.blogspot.com/2017/02/pipelines-in-rust.html">Pipelines in Rust</a> | Unix Shell | Rust Programming 2 |
| 2/12 | Fri | Data structures in Rust | <a href="https://doc.rust-lang.org/book/ch05-00-structs.html">Using Structs to Structure Related Data</a><br><a href="https://doc.rust-lang.org/book/ch06-00-enums.html">Enums and Pattern Matching</a> |  |  |
| 2/15 | Mon | Review of Unix Command Line<br>Review of Rust |  |  |  |


## Part 2: The Internet
|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 2/17 | Wed | The Internet<br>Downloading a web page | <a href="https://www.oreilly.com/library/view/tcpip-network-administration/0596002971/ch01.html">Overview of TCP/IP</a><br><a href="https://doc.rust-lang.org/std/net/struct.TcpStream.html">TcpStream</a><br><a href="https://doc.rust-lang.org/std/io/trait.Write.html">Write trait</a> | Webget | Unix Shell |
| 2/19 | Fri | Using Transport Layer Security | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/security-crypto.pdf">Cryptography</a> |  |  |
| 2/22 | Mon | Threads vs Processes | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf">26: Concurrency and Threads</a> |  |  |
| 2/24 | Wed | Threads in Rust | <a href="https://doc.rust-lang.org/book/ch16-00-concurrency.html">Fearless Concurrency</a> | Web server 1 | Webget |
| 2/26 | Fri | Locks | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf">28: Locks</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf">29: Locked Data Structures</a> |  |  |
| 3/1 | Mon | Concurrency Problems | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf">32: Common Concurrency Problems</a> |  |  |
| 3/3 | Wed | Performance analysis |  | Web server 2 | Web server 1 |


## Part 3: The Kernel
|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 3/5 | Fri | Bare metal programming | <a href="https://os.phil-opp.com/freestanding-rust-binary/">A Freestanding Rust Binary</a><br><a href="https://os.phil-opp.com/minimal-rust-kernel/">A Minimal Rust Kernel</a> |  |  |
| 3/8 | Mon | VGA Buffer | <a href="https://os.phil-opp.com/vga-text-mode/">VGA Buffer</a><br><a href="https://crates.io/crates/pluggable_interrupt_os">Interrupt OS</a><br><a href="https://github.com/gjf2a/bare_metal_tracer">Tracer</a> |  |  |
| 3/10 | Wed | Pluggable Interrupt OS | <a href="https://crates.io/crates/pluggable_interrupt_os">Pluggable Interrupt OS</a><br><a href="https://github.com/gjf2a/bare_metal_tracer">Tracer</a> | Bare metal game | Web server 2 |
| 3/12 | Fri | Ghost Hunter | <a href="https://github.com/gjf2a/ghost_hunter">Ghost Hunter</a><br><a href="https://github.com/gjf2a/ghost_hunter_core">Ghost Hunter Core</a> |  |  |
| 3/15 | Mon | Interrupts | <a href="https://os.phil-opp.com/cpu-exceptions/">CPU Exceptions</a><br><a href="https://os.phil-opp.com/double-fault-exceptions/">Double Faults</a><br><a href="https://os.phil-opp.com/hardware-interrupts/">Hardware interrupts</a> |  |  |
| 3/17 | Wed | Game Demo Day |  |  | Bare metal game check-in |
| 3/19 | Fri | Interrupts |  |  |  |
| 3/22 | Mon | Final Game Demos |  |  |  |
| 3/24 | Wed | Break: no class |  |  |  |
| 3/26 | Fri | Interrupt-based multitasking |  | Game Kernel | Bare metal game |
| 3/29 | Mon | Paging | <a href="https://os.phil-opp.com/paging-introduction/">Introduction to Paging</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-paging.pdf">18: Introduction to Paging</a> |  |  |
| 3/31 | Wed | Implementation of Paging | <a href="https://os.phil-opp.com/paging-implementation/">Paging Implementation</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf">Translation Lookaside Buffers</a> |  |  |
| 4/2 | Fri | Memory Management: Heap | <a href="https://os.phil-opp.com/heap-allocation/">Heap Allocation</a> | Heap | Game Kernel |
| 4/5 | Mon | Allocator Designs | <a href="https://os.phil-opp.com/allocator-designs/">Allocator Designs</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-freespace.pdf">17: Free Space Management</a> |  |  |
| 4/7 | Wed | Garbage Collection |  |  |  |
| 4/9 | Fri | Processor Scheduling | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf">CPU Scheduling</a> | Scheduling | Heap |
| 4/12 | Mon | Scheduling with Priorities | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf">Multi-Level Feedback</a> |  |  |
| 4/14 | Wed | Randomized Scheduling | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf">Lottery Scheduling</a> |  |  |
| 4/16 | Fri | Final projects |  | Project proposal | Scheduling |
| 4/19 | Mon | I/O Devices<br>Hard Disk Drives | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-devices.pdf">I/O Devices</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf">Hard Disk Drives</a> |  |  |
| 4/21 | Wed | File System | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf">File System Implementation</a> | File System | Project Proposal |
| 4/23 | Fri | Break: no class |  |  |  |
| 4/26 | Mon | Solid-State Drives | <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-ssd.pdf">Flash-based SSDs</a> |  |  |
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
  * Research two different operating systems.
  * Discuss the motivation for creating each operating system.
  * Discuss how each operating system addresses the topics of Virtualization, Concurrency, and Persistence.
  * Discuss the similarities and differences between them, especially in light of the motivation for their creation.
2. **Programming Project**:
  * Implement a working program that extends our exploration of any topic from the course.
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
    * **Complete** the final project and **Complete** at least 2 other projects
	* **Partial** completion of the final project, and **Complete** at least 4 other projects
	* **Missing** final project, and **Complete** at least 8 other projects
  * At most four **Missing** projects
  * Schedule and attend at least one Office Hours meeting
  * Submit a course feedback form
* To earn a D in the course, a student will:
  * One of the following:
    * **Complete** the final project, and **Partial** completion of at least 4 other projects
	* **Partial** completion of the final project, and **Partial** completion of at least 6 other projects
	* **Missing** final project, and **Partial** completion of at least 8 other projects

### Revising submitted work
If a submitted project receives a **Partial** assessment:
* The instructor will give feedback identifying revisions that, if applied, would result in a **Complete** assessment.
* The student will schedule and attend an Office Hours meeting to discuss the necessary revisions and establish a deadline for their submission.
* If the student submits the revisions by the agreed deadline, the revised project will receive a **Complete** assessment.

## <a name="latedays">Late Policy</a>
If a student needs an extension, the instructor must be notified by email or Teams message by 
4 pm on the day prior to the due date. This notification email must state the duration of the 
requested extension. The instructor reserves the right to decline a request for an extension, 
but the intention is that most requests for extensions will be granted.
