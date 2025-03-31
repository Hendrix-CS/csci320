---
layout: work
type: Project
num: 8
worktitle: Garbage-Collected Heap
---

At the hardware level, the free RAM in a computer is a giant, undifferentiated mass
known as the **heap**. A key operating system task is to assign blocks of heap RAM to 
processes as they request it. Furthermore, the operating system must track and reclaim 
unused RAM. 

One common approach to heap management is to implement a **garbage-collected heap**.
A garbage-collected heap allocates blocks of RAM on request, and automatically frees
blocks of RAM that are no longer in use. One popular type of garbage-collected heap
is a **copying collector**. In this project, you will implement a copying-collected 
heap that runs as part of the kernel. 

* Privately fork [this template](https://github.com/gjf2a/gc_heap_template) for 
  building your solution. 
* Each `RamHeap` object represents a region of RAM. RAM itself is accessed via the 
  array that each `RamHeap` object manages.
* Also examine the [gc_headers](https://github.com/gjf2a/gc_headers)
  to familiarize yourself with the data structures you will be using.
  * `Pointer` objects are the means by which entities using the heap
  refer to memory. 
  * Each `Pointer` object includes:
    * A block number that uniquely identifies the allocated block.
    * An offset into that block, to access a specific memory location.
    * The total size of the block.
  * The malloc() method will perform an allocation, returning a `Pointer`
  to the newly allocated memory. The `Pointer` will include a unique block
  number for the allocation, along with its size. The `offset` will be zero, 
  referencing the first memory location in the block.
  * The `load()` and `store()` methods in conjunction with `Pointer`s are 
  used to retrieve and update values in heap-allocated RAM.
  * Entities using the heap only use `Pointer` objects - they are never
  given access to the specific memory address of the memory they are using.
    * This is because the garbage collector might relocate memory to a
      new address when collecting. 
    * By referencing memory exclusively through block numbers, the 
      relocation process is made invisible to the user.
* When `malloc()` is called but there is no more space in the heap,
  the collector will call the `trace()` method of its `Tracer` parameter
  to find out which blocks are in use.
  * The collector should provide an array of `MAX_BLOCKS` boolean values
    to `trace()`. All of the values in the array should initially be `false`.
  * The `Tracer` will mark `true` for each block it wants to keep.
  * The collector will then copy each `true` block to the new heap, 
    updating their addresses as they are moved.

## Submissions
* Add the instructor as a collaborator on your fork of `gc_heap_template`.
* Submit your GitHub URL via Teams.

## Assessment
* **Level 1**
  * The following unit tests pass:
    * `block_table_test()`
    * `basic_allocation_test()`
    * `out_of_blocks_test()`
    * `test_bad_address_error()`
* **Level 2**
  * The Level 1 unit tests still pass. In addition, the following unit tests pass:
    * `deallocation_test()`
    * `collection_test()`
    * `full_test()`
    * `test_no_blocks_error()`
    * `test_zero_size_error()`
    * `test_illegal_block_error()`
    * `test_unallocated_block_error()`
    * `test_offset_error()`
    * `test_misaligned_pointer_error()`
* **Level 3**
  * Implement a **generational** collector.
    * Any object that survives `MAX_COPIES` collections is copied into a second-generation 
      heap segment.
    * The second-generation heap will be collected much less often, as most objects won't live
      long enough to be copied there.
  * The Level 1 and Level 2 unit tests must still pass. In addition, `generational_test()` passes.