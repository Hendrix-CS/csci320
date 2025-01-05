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
  * CPU and RAM by virtualizing those resources by means of the **process** abstraction.
  * Persistent memory (hard disk, Flash memory) through the **file system** abstraction.
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

## Part 1: User Space

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 1/22 | Wed | Three Easy Pieces<br>Command Line<br>Files and Directories | [Introduction to Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf) | [Survey](https://forms.gle/xwQESACLYUpc1i9R9)<br>[Shell Commands, introduction]({{site.baseurl}}/projects/shell_commands.html) |  |
| 1/24 | Fri | Processes<br>Pipes<br>I/O Redirection | [Processes](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf) | [Shell Commands, complete]({{site.baseurl}}/projects/shell_commands.html) | Shell Commands, introduction |
|      |
| 1/27 | Mon | Rust<br>File I/O | [Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)<br>[Programming a Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)<br>[Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)<br>[std::fs](https://doc.rust-lang.org/std/fs/index.html) | [Rust Programming 1]({{site.baseurl}}/projects/rust1.html) | Shell Commands, complete |
| 1/29 | Wed | Ownership and Borrowing<br>Strings<br>Buffers | [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)<br>[Read trait](https://doc.rust-lang.org/std/io/trait.Read.html)<br>[String in Rust](https://gjf2a.blogspot.com/2017/02/strings-in-rust.html)<br>[BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html)<br>[BufRead trait](https://doc.rust-lang.org/std/io/trait.BufRead.html) |  |  |
| 1/31 | Fri | Rust Collection Types | [Common Collections](https://doc.rust-lang.org/book/ch08-00-common-collections.html) |  |  |
|      |     
| 2/3  | Mon | The Internet<br>Downloading a web page | [Overview of TCP/IP](https://www.oreilly.com/library/view/tcpip-network-administration/0596002971/ch01.html)<br>[TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html)<br>[Write trait](https://doc.rust-lang.org/std/io/trait.Write.html)<br>[`write!` macro](https://doc.rust-lang.org/std/macro.write.html) | [Rust Programming 2]({{site.baseurl}}/projects/rust2.html) | Rust Programming 1 |
| 2/5  | Wed | Using Transport Layer Security | [Cryptography](http://pages.cs.wisc.edu/~remzi/OSTEP/security-crypto.pdf)
| 2/7  | Fri | Unix Process API | [Process API](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf)<br>[nix crate](https://docs.rs/nix/0.26.2/nix/)<br>[C strings](https://doc.rust-lang.org/std/ffi/struct.CString.html) | 
|      |
| 2/10 | Mon | Unix System Calls | [Direct Execution](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf) | |
| 2/12 | Wed | Files and Directories | [Files and Directories](http://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf) | [Unix Shell]({{site.baseurl}}/projects/vssh.html) | Rust Programming 2 |
| 2/14 | Fri | File Descriptors<br>Pipelines | [Pipelines in Rust](https://gjf2a.blogspot.com/2017/02/pipelines-in-rust.html) |
|      |
| 2/17 | Mon | **Winter Break: No class** |
| 2/19 | Wed | Data structures in Rust | [Using Structs to Structure Related Data](https://doc.rust-lang.org/book/ch05-00-structs.html)<br>[Enums and Pattern Matching](https://doc.rust-lang.org/book/ch06-00-enums.html)
| 2/21 | Fri | In-Class Essay 1: [The Unix Shell]({{site.baseurl}}/essays/essay1.html)
|      |
| 2/24 | Mon | Threads vs Processes | [Concurrency and Threads](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf) | [Web Server]({{site.baseurl}}/projects/webserver.html) | Unix Shell |
| 2/26 | Wed | Threads in Rust<br>Locks | [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)<br>[Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf)<br>[Locked Data Structures](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf)
| 2/28 | Fri | Concurrency Problems | [Common Concurrency Problems](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf) |  |  |
|      |
| 3/3  | Mon | Iterators in Rust |



## Part 2: Kernel Space

|Date|Day|Topic/Activity|Reading|Assigned|Due|
| --- | --- | --- | --- | --- | --- |
| 3/5  | Wed | Bare metal programming | [A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/)<br>[A Minimal Rust Kernel](https://os.phil-opp.com/minimal-rust-kernel/)<br>[VGA Buffer](https://os.phil-opp.com/vga-text-mode/)<br>[Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os) |  [Bare metal game]({{site.baseurl}}/projects/baremetalgame) | Web server |
| 3/7  | Fri | Ghost Hunter | [Ghost Hunter](https://github.com/gjf2a/ghost_hunter)<br>[Ghost Hunter Core](https://github.com/gjf2a/ghost_hunter_core) |  |  |
|      |
| 3/10 | Mon | Interrupts | [CPU Exceptions](https://os.phil-opp.com/cpu-exceptions/)<br>[Double Faults](https://os.phil-opp.com/double-fault-exceptions/)<br>[Hardware interrupts](https://os.phil-opp.com/hardware-interrupts/) |
| 3/12 | Wed | Interrupts | |  |  |
| 3/14 | Fri | Bare Metal Demos | | [SWIM Part 1: Interface]({{site.baseurl}}/projects/bare_metal_editor.html) | Bare Metal Game |
|      |
| 3/17 | Mon | User-space vs. Kernel-space programming: Retrospective | | |
| 3/19 | Wed | In-Class Essay 2: [Processes and Threads]({{site.baseurl}}/essays/essay2.html) |  |  |  |
| 3/21 | Fri | The Story So Far |  |  | SWIM Part 1: Interface |
|      |
| 3/24 | Mon | Spring Break: no class |  |  |  |
| 3/26 | Wed | Spring Break: no class |  |  |  |
| 3/28 | Fri | Spring Break: no class |  |  |  |
|      |
| 3/31 | Mon | Garbage Collection | | [SWIM Part 2: Garbage Collection]({{site.baseurl}}/projects/garbage.html) |
| 4/2  | Wed | Memory Management: Heap | [Heap Allocation](https://os.phil-opp.com/heap-allocation/) | | |
| 4/4  | Fri | Allocator Designs | [Allocator Designs](https://os.phil-opp.com/allocator-designs/)<br>[Free Space Management](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-freespace.pdf) | |  |
|      |
| 4/7  | Mon | File Systems | [I/O Devices](http://pages.cs.wisc.edu/~remzi/OSTEP/file-devices.pdf)<br>[Hard Disk Drives](http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf)  | [SWIM Part 3: File System]({{site.baseurl}}/projects/filesystem.html) | SWIM Part 2: Garbage Collection |
| 4/9  | Wed | File Systems | [File System Implementation](http://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf) | |  |
| 4/11 | Fri | Paging | [Introduction to Paging (OS in Rust)](https://os.phil-opp.com/paging-introduction/)<br>[Introduction to Paging (OSTEP)](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-paging.pdf) |  |  |
|      |
| 4/14 | Mon | Implementation of Paging | [Paging Implementation](https://os.phil-opp.com/paging-implementation/)<br>[Translation Lookaside Buffers](http://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf) |  |  |
| 4/16 | Wed | Processor Scheduling | [CPU Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) | [SWIM Part 4: Processes]({{site.baseurl}}/projects/swim.html) | SWIM Part 3: File System |
| 4/18 | Fri | Scheduling with Priorities | [Multi-Level Feedback](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf) |  |  |
|      |
| 4/21 | Mon | Randomized Scheduling | [Lottery Scheduling](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf) |  |  |
| 4/23 | Wed | Unix history, GNU Project, Linux kernel
| 4/25 | Fri | History of MS-DOS and Windows, evolution of GNU/Linux |  | [Free Project](#free) | SWIM Part 4  |
|      |
| 4/28 | Mon | In-Class Essay 3: [The Kernel]({{site.baseurl}}/essays/essay3.html) 
| 4/30 | Wed | Free Software vs. Open Source<br>Return of the Mac<br>Microkernels |  |  |  |
| 5/2  | Fri | Three Easy Pieces |  |  |  |
|      |
| 5/9  | Fri 8:30-11:30am | **No final exam** | | | Free project<br>All revised work |

<hr>
# <a name="assessment">Assessment</a>

## <a name="projects">Projects</a>

A total of 10 formal projects will be assigned throughout the semester; approximately one 
project per week. Each project will have three levels to which it can be completed, with each level building upon the previous level. In general:
* A **Level 1 project** contains a basic implementation of the core ideas explored in the project.
* A **Level 2 project** is a more complete implementation of those ideas.
* A **Level 3 project** goes beyond this to undertake a deeper exploration of the assignment ideas.

Each project will be evaluated via **specifications** (a set of criteria) for each level. Projects meeting all the criteria for a 
given level will receive credit for that level; projects that do not meet all the criteria will not receive credit for that level.

Each project submitted by the **assigned deadline** of at least **Level 1 quality** receives 
**one additional credit** as an on-time bonus.

Once a project is graded, if a student wishes to revise it to achieve a higher level, the student should first meet with the
professor to discuss the planned revisions. The student may thereafter resubmit the revised project when ready.

Each student should have a [GitHub](https://github.com/) account. Each student should create one **private** GitHub repository 
that contains all of their code for Part 1 of the course and additional GitHub repositories as 
specified for the Part 2 projects.  The student should add [Dr. Ferrer](https://github.com/gjf2a) as 
a contributor to each repository. For each project, there will be a Teams assignment in which 
you will copy and paste the URL for the project's GitHub repository. When each project is due, 
the instructor will download the repository onto his own machine for grading.

### <a name="free">Free Project</a>

Students may also complete a **free project**. This is **completely optional**, but it is
an opportunity to earn project credits pursuing a topic of personal interest. 
The free project consists of a program written in the Rust programming language on any topic 
of interest to the student. Any student wishing to pursue a free project should submit a project
proposal by Monday, April 21. The instructor will advise the student as to what would constitute 
Level 1, Level 2, and Level 3 performance on the proposed project. 

All free projects are due by the end of the final exam period for the course. There is no 
on-time bonus for a free project; it must be submitted by the deadline to receive any credit.
  
## <a name="essays">In-Class Essays</a>

A total of three in-class essays will be assigned over the course of the semester. Each essay
topic is posted on the course web page. In preparing for the in-class essay, each student may
make use of whatever resources they would like - readings, assignments, classmates, anything on
the Internet, or any other resource. 

The in-class essay itself is closed-book, closed-note, and closed-device. Paper will be provided
for writing the essay, which must be submitted at the end of the class period. 

The essays will be commented upon by the instructor and returned. Each student should then
revise their essay, taking into account the instructor comments. The revised essay should be 
typed and submitted electronically. The original handwritten essay should also be resubmitted. 
The revised essay will be due one week after the original essays are returned.

Students are welcome to make use of additional resources when revising their essays; proper
citation should be included for each resource. Each revised essay will then be assessed as
**Level 1** or **Level 2**, depending on the quality of the essay. Quality will be assessed
according to the following criteria:
* Writing quality, including proper spelling, usage, and grammar.
* Demonstrated depth of understanding the essay topic.
* Appropriate use of examples from course projects.
 
One additional credit will be awarded for on-time submissions of the revised essays.

## <a name="grading">Specifications Grading</a>
Each project and essay earns one credit for each level achieved. Submitting an assignment by the 
specified deadline earns one additional credit.
There are **52 total credits** available for the semester: **4 credits** for each of 
**10 formal projects**, **3 credits** for the **free project**, and **3 credits** for 
each of the **three essays**.

| Grade | Minimum Project Credits | Minimum Essay Credits | Minimum Total Credits |
| ----: | ----------------------: | --------------------: | --------------------: |
| A     | Level 2 on 10 projects  | Level 2 on 3 essays   | 47                    |
| B     | 30                      | Level 2 on 2 essays<br>Level 1 on 1 essay   | 38                    |
| C     | 20                      | Level 1 on 3 essays   | 29                    |
| D     | 12                      | Level 1 on 2 essays   | 18                    |


* **Note**: All late submissions/revisions must be received before 11:30 am on Friday, 
  May 9, the end of the final exam period for the course.
