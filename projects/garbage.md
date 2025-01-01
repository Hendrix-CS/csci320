---
layout: work
type: Project
num: 8
worktitle: Garbage-Collected Heap
---

* Implement a copying garbage collector.
* Use [this template](https://github.com/gjf2a/gc_heap_template) for building 
  your solution. 
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
