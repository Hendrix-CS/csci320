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
| 2/21 | Fri | In-Class Essay 1: The Unix Shell
|      |
| 2/24 | Mon | Threads vs Processes | [Concurrency and Threads](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf) | [Web Server]({{site.baseurl}}/projects/webserver.html) | Unix Shell |
| 2/26 | Wed | Threads in Rust<br>Locks | [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)<br>[Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf)<br>[Locked Data Structures](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf)
| 2/28 | Fri | Concurrency Problems | [Common Concurrency Problems](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf) |  |  |
|      |
| 3/3  | Mon | Performance analysis |



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
| 3/17 | Mon | User-space vs. Kernel-space programming: Retrospective | | Game Reviews |
| 3/19 | Wed | In-Class Essay 2: Processes and Threads |  |  |  |
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
| 4/25 | Fri | History of MS-DOS and Windows, evolution of GNU/Linux |  | [Free Project]() | SWIM Part 4  |
|      |
| 4/28 | Mon | In-Class Essay 3: The Kernel 
| 4/30 | Wed | Free Software vs. Open Source<br>Return of the Mac<br>Microkernels |  |  |  |
| 5/2  | Fri | Wrap-up |  |  |  |
|      |
| 5/9  | Fri 8:30-11:30am | Final Essay: Three Easy Pieces | | | Free Project |

<hr>
# <a name="assessment">Assessment</a>

# TODO: CONTINUE REVISION HERE

## <a name="projects">Projects</a>

A total of 10 projects will be assigned throughout the semester; approximately one 
project per week. Each project will have three levels to which it can be completed, with each level building upon the previous level. In general:
* A **Level 1 project** contains a basic implementation of the core ideas explored in the project.
* A **Level 2 project** is a more complete implementation of those ideas, including results and analysis of experiments.
* A **Level 3 project** goes beyond this to undertake a deeper exploration of the assignment ideas.

Each project will be evaluated via **specifications** (a set of criteria) for each level. Projects meeting all the criteria for a 
given level will receive credit for that level; projects that do not meet all the criteria will not receive credit for that level.

Once a project is graded, if a student wishes to revise it to achieve a higher level, the student should first meet with the
professor to discuss the planned revisions. The student may thereafter resubmit the revised project when ready.

Each student should have a [GitHub](https://github.com/) account. Each student should create one **private** GitHub repository that contains all of their code for Parts 1 and 2 of the course, and an additional **private** GitHub repository for Part 3 of the course.  The student should add [Dr. Ferrer](https://github.com/gjf2a) as 
a contributor to each repository. When each project is due, he will download the 
repository onto his own machine for grading.
  

## <a name="grading">Specifications Grading</a>
Each project earns one credit for each level achieved. Submitting a project by the specified deadline earns one additional credit.
There are **55 total credits** available for the semester: **4 credits** for each of **10 projects** and **15 credits** for the 
**final project**.

| Grade | Credit range |
| ----: | -----------: |
| A     | 48-55        |
| B     | 40-47        |
| C     | 32-39        |
| D     | 24-31        |
| F     | 0-23         |


* **Note**: All late submissions/revisions must be received before 5 pm on Tuesday, 
  May 13, the last day of the semester.
