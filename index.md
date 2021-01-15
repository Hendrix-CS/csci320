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

<table cellspacing="2" cellpadding="3">
<tbody>
<tr><th>Date</th><th>Day</th><th>Topic/Activity</th><th>Reading</th><th>Assigned</th><th>Due</th></tr>
<tr><td>1/20</td><td>Wed</td><td>Three Easy Pieces<br>Command Line<br>Files and Directories</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf">2: Introduction to Operating Systems</a></td><td>Shell Commands, introduction</td><td>None</td></tr>
<tr><td>1/22</td><td>Fri</td><td>Processes<br>Pipes<br>I/O Redirection</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf">4: Processes</a></td><td>Shell Commands, complete</td><td>Shell Commands, introduction</td></tr>
<tr><td>1/25</td><td>Mon</td><td>Rust<br>File I/O</td><td><a href="https://doc.rust-lang.org/book/ch01-00-getting-started.html">Getting Started</a><br><a href="https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html">Programming a Guessing Game</a><br><a href="https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html">Common Programming Concepts</a><br><a href="https://doc.rust-lang.org/std/fs/index.html">std::fs</a></td><td>Rust Programming 1</td><td>Shell Commands, complete</td></tr>
<tr><td>1/27</td><td>Wed</td><td>Ownership and Borrowing<br>Strings<br>Buffers</td><td><a href="https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html">Understanding Ownership</a><br><a href="https://doc.rust-lang.org/std/io/trait.Read.html">Read trait</a><br><a href="https://gjf2a.blogspot.com/2017/02/strings-in-rust.html">String in Rust</a><br><a href="https://doc.rust-lang.org/std/io/struct.BufReader.html">BufReader</a><br><a href="https://doc.rust-lang.org/std/io/trait.BufRead.html">BufRead trait</a></td><td>None</td><td>None</td></tr>
<tr><td>1/29</td><td>Fri</td><td>Rust Collection Types</td><td><a href="https://doc.rust-lang.org/book/ch08-00-common-collections.html">Common Collections</a></td><td>None</td><td>None</td></tr>
<tr><td>2/1</td><td>Mon</td><td>Unix Process API</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf">5: Process API</a><br><a href="https://docs.rs/nix/0.19.1/nix/">nix crate</a><br><a href="https://doc.rust-lang.org/std/ffi/struct.CString.html">C strings</a></td><td>Rust Programming 2</td><td>Rust Programming 1</td></tr>
<tr><td>2/3</td><td>Wed</td><td>Unix System Calls</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf">6: Direct Execution</a></td><td>None</td><td>None</td></tr>
<tr><td>2/5</td><td>Fri</td><td>Break: no class</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>2/8</td><td>Mon</td><td>Files and Directories</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf">39: Files and Directories</a></td><td>None</td><td>None</td></tr>
<tr><td>2/10</td><td>Wed</td><td>File Descriptors<br>Pipelines</td><td><a href="https://gjf2a.blogspot.com/2017/02/pipelines-in-rust.html">Pipelines in Rust</a></td><td>Unix Shell</td><td>Rust Programming 2</td></tr>
<tr><td>2/12</td><td>Fri</td><td>Data structures in Rust</td><td><a href="https://doc.rust-lang.org/book/ch05-00-structs.html">Using Structs to Structure Related Data</a><br><a href="https://doc.rust-lang.org/book/ch06-00-enums.html">Enums and Pattern Matching</a></td><td>None</td><td>None</td></tr>
<tr><td>2/15</td><td>Mon</td><td>Review of Unix Command Line<br>Review of Rust</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>2/17</td><td>Wed</td><td>The Internet<br>Downloading a web page</td><td><a href="https://www.oreilly.com/library/view/tcpip-network-administration/0596002971/ch01.html">Overview of TCP/IP</a><br><a href="https://doc.rust-lang.org/std/net/struct.TcpStream.html">TcpStream</a><br><a href="https://doc.rust-lang.org/std/io/trait.Write.html">Write trait</a></td><td>Webget</td><td>Unix Shell</td></tr>
<tr><td>2/19</td><td>Fri</td><td>Using Transport Layer Security</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/security-crypto.pdf">Cryptography</a></td><td>None</td><td>None</td></tr>
<tr><td>2/22</td><td>Mon</td><td>Threads vs Processes</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf">26: Concurrency and Threads</a></td><td>None</td><td>None</td></tr>
<tr><td>2/24</td><td>Wed</td><td>Threads in Rust</td><td><a href="https://doc.rust-lang.org/book/ch16-00-concurrency.html">Fearless Concurrency</a></td><td>Web server 1</td><td>Webget</td></tr>
<tr><td>2/26</td><td>Fri</td><td>Locks</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf">28: Locks</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf">29: Locked Data Structures</a></td><td>None</td><td>None</td></tr>
<tr><td>3/1</td><td>Mon</td><td>Concurrency Problems</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf">32: Common Concurrency Problems</a></td><td>None</td><td>None</td></tr>
<tr><td>3/3</td><td>Wed</td><td>Performance analysis</td><td>None</td><td>Web server 2</td><td>Web server 1</td></tr>
<tr><td>3/5</td><td>Fri</td><td>Bare metal programming</td><td><a href="https://os.phil-opp.com/freestanding-rust-binary/">A Freestanding Rust Binary</a><br><a href="https://os.phil-opp.com/minimal-rust-kernel/">A Minimal Rust Kernel</a></td><td>None</td><td>None</td></tr>
<tr><td>3/8</td><td>Mon</td><td>VGA Buffer</td><td><a href="https://os.phil-opp.com/vga-text-mode/">VGA Buffer</a><br><a href="https://crates.io/crates/pluggable_interrupt_os">Interrupt OS</a><br><a href="https://github.com/gjf2a/bare_metal_tracer">Tracer</a></td><td>None</td><td>None</td></tr>
<tr><td>3/10</td><td>Wed</td><td>Pluggable Interrupt OS</td><td><a href="https://crates.io/crates/pluggable_interrupt_os">Pluggable Interrupt OS</a><br><a href="https://github.com/gjf2a/bare_metal_tracer">Tracer</a></td><td>Bare metal game</td><td>Web server 2</td></tr>
<tr><td>3/12</td><td>Fri</td><td>Ghost Hunter</td><td><a href="https://github.com/gjf2a/ghost_hunter">Ghost Hunter</a><br><a href="https://github.com/gjf2a/ghost_hunter_core">Ghost Hunter Core</a></td><td>None</td><td>None</td></tr>
<tr><td>3/15</td><td>Mon</td><td>Interrupts</td><td><a href="https://os.phil-opp.com/cpu-exceptions/">CPU Exceptions</a><br><a href="https://os.phil-opp.com/double-fault-exceptions/">Double Faults</a><br><a href="https://os.phil-opp.com/hardware-interrupts/">Hardware interrupts</a></td><td>None</td><td>None</td></tr>
<tr><td>3/17</td><td>Wed</td><td>Game Demo Day</td><td>None</td><td>None</td><td>Bare metal game check-in</td></tr>
<tr><td>3/19</td><td>Fri</td><td>Interrupts</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>3/22</td><td>Mon</td><td>Final Game Demos</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>3/24</td><td>Wed</td><td>Break: no class</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>3/26</td><td>Fri</td><td>Interrupt-based multitasking</td><td>None</td><td>Game Kernel</td><td>Bare metal game</td></tr>
<tr><td>3/29</td><td>Mon</td><td>Paging</td><td><a href="https://os.phil-opp.com/paging-introduction/">Introduction to Paging</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-paging.pdf">18: Introduction to Paging</a></td><td>None</td><td>None</td></tr>
<tr><td>3/31</td><td>Wed</td><td>Implementation of Paging</td><td><a href="https://os.phil-opp.com/paging-implementation/">Paging Implementation</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf">Translation Lookaside Buffers</a></td><td>None</td><td>None</td></tr>
<tr><td>4/2</td><td>Fri</td><td>Memory Management: Heap</td><td><a href="https://os.phil-opp.com/heap-allocation/">Heap Allocation</a></td><td>Heap</td><td>Game Kernel</td></tr>
<tr><td>4/5</td><td>Mon</td><td>Allocator Designs</td><td><a href="https://os.phil-opp.com/allocator-designs/">Allocator Designs</a></td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/vm-freespace.pdf">17: Free Space Management</a></td><td>None</td></tr>
<tr><td>4/7</td><td>Wed</td><td>None</td><td></td><td>Garbage Collection</td><td>None</td></tr>
<tr><td>4/9</td><td>Fri</td><td>None</td><td>None</td><td></td><td>Processor Scheduling</td></tr>
<tr><td>4/12</td><td>Mon</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf">CPU Scheduling</a></td><td>Scheduling</td><td>Heap</td><td></td></tr>
<tr><td>4/14</td><td>Wed</td><td>Scheduling with Priorities</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf">Multi-Level Feedback</a></td><td>None</td><td>None</td></tr>
<tr><td>4/16</td><td>Fri</td><td>Randomized Scheduling</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf">Lottery Scheduling</a></td><td>None</td><td>None</td></tr>
<tr><td>4/19</td><td>Mon</td><td>I/O Devices<br>Hard Disk Drives</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-devices.pdf">I/O Devices</a><br><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf">Hard Disk Drives</a></td><td>None</td><td>None</td></tr>
<tr><td>4/21</td><td>Wed</td><td>File System</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf">File System Implementation</a></td><td>File System</td><td>Scheduling</td></tr>
<tr><td>4/23</td><td>Fri</td><td>Break: no class</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>4/26</td><td>Mon</td><td>Solid-State Drives</td><td><a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-ssd.pdf">Flash-based SSDs</a></td><td>None</td><td>None</td></tr>
<tr><td>4/28</td><td>Wed</td><td>Final projects</td><td>None</td><td>Project proposal</td><td>File System</td></tr>
<tr><td>4/30</td><td>Fri</td><td>Famous OSs</td><td>None</td><td>None</td><td>Project proposal</td></tr>
<tr><td>5/10</td><td>Mon</td><td>Final Project Presentations</td><td>None</td><td>None</td><td>Final Project</td></tr>
</tbody>
</table>

<hr>
# <a name="assessment">Assessment</a>

## <a name="projects">Projects</a>

A total of 12 projects will be assigned throughout the semester; approximately one project 
per week. Each project 

Approximately one project will be assigned per week. 

Every Tuesday, a project will be assigned. Students may complete projects individually or 
in teams of two. In most projects, students will program their robots to perform a task using
a new concept introduced that week, potentially incorporating other concepts covered in 
previous weeks. Each project will typically be due the following Tuesday, with a brief
video presentation given in class. Some time will typically be available every Thursday
during the class period for work on that week's project.

### Project Reports
For each project, each student (even if part of a team) should submit an individual project
report. Each report includes the following:
* A project log, which includes the following for every work session:
  * Date of the work session, including start and end times.
  * Goals for the session.
  * Brief descriptions of activities undertaken.
  * Observations of activities.
  * Assessment of the degree to which session goals were met.
* Answers to project-specific questions.
* A conclusion detailing the degree of success of the project.

### Project Presentations

On the due date of each project, each team will play a video in class. The video should meet the following constraints:
* It must be between 80 and 90 seconds in duration.
  * For team projects, the video should be 160 to 180 seconds in duration.
* It should include brief narration of the strategy for the project.
* It should demonstrate the student's robots performing the required tasks for the week's project. Narration should contextualize each demonstrated activity.

## <a name="finalproject">Final Project</a>
In the last three weeks of the semester, each student will undertake a final project. 
In this final project, you will build and program a robot that fulfills a contextualized 
purpose. A public demonstration will be made of the robot's capabilities, and a paper 
reflecting upon lessons learned will be submitted as well. In keeping with the Odyssey 
Special Project guidelines, the project will require at least 30 hours of work. As with 
the other course projects, final projects may be undertaken either individually or in 
teams of two.

## <a name="participation">Class Participation</a>

### Presentation Questions
* Students should be prepared to answer questions after their video presentation concludes. 
* Each student is expected to ask one question on each class day that includes presentations.

### Office Hours
* Each student should schedule and attend at least three online Office Hour meetings with the instructor at some point during the semester.


## <a name="grading">Specifications Grading</a>
Each assignment is graded on a pass-fail basis. To earn a passing grade, the assignment
must be substantively complete; minor imperfections are perfectly acceptable. Final course
grades are earned based on completed passing assignments, as follows:

* To earn an A in the course, a student will:
  * Complete all nine projects
  * Complete the final project
  * Submit a course feedback form
  * Ask six presentation questions
  * Schedule and attend at least three Office Hours meetings
* To earn a B in the course, a student will: 
  * Complete any seven projects
  * Complete the final project
  * Submit a course feedback form
  * Ask four presentation questions
  * Schedule and attend at least two Office Hours meetings
* To earn a C in the course, a student will:
  * Complete any five projects
  * Complete the final project
  * Submit a course feedback form
  * Ask two presentation questions
  * Schedule and attend at least one Office Hours meeting
* To earn a D in the course, a student will:
  * Complete any four projects

### Revising submitted work
If a submitted project is not of sufficient quality to receive a passing grade:
* The instructor will give feedback identifying revisions that, if applied, would result in a passing grade.
* The student will schedule and attend an Office Hours meeting to discuss the necessary revisions and establish a deadline for their submission.
* If the student submits the revisions by the agreed deadline, the revised project will receive a passing grade.

## <a name="latedays">Late Policy</a>
If a student needs an extension, the instructor must be notified by email by 4 pm on the 
day prior to the due date. This notification email must state the duration of the requested 
extension. The instructor reserves the right to decline a request for an extension, but 
the intention is that most requests for extensions will be granted.

## <a name="equipment">Equipment</a>
Each student will be issued the following equipment:
* One robot kit, containing:
  * Two motors and wheels
  * A battery case
  * A plexiglas chassis
* One breadboard
* One motor control chip
* One Arduino board

This equipment should be returned to the instructor at the end of the semester. Students will
be billed for any unreturned equipment.

Each student will need to supply a smartphone or tablet running the Android operating system.
Students for whom this presents a difficulty should contact the instructor, who will investigate
possible arrangements.