Chosen project: Dumb code analysis
- Write a python script that recurses over a given directory (for test purposes, the OneUp platform repo) and returns the following information:
	- Which file has the most pairs of curly braces?
	- Which file has the deepest nesting of curly braces?
	- Who’s written how many lines of code?
	- Who’s written the most comments? Includes // comments, /* comments */, and multi-line comments, but excluding comment lines that are PHPDoc hints. [1]
	- What is everyone’s comment ratio?

[1] any line that starts with /* or * as the first non-whitespace character, but is not followed by an @ as the next non-whitespace character.

Set up:

run ```pipenv shell``` to start the virtualised env. 

---

To do:
- consider future args

Done:
- learn how to traverse directory structure
- what dir am I in
- what files are in the dir
- what folders are in dir
- file type by extension
- identify node mods vendor and exclude library imports


Options
output
	- running tally
	- record of each file
traversal
	- one traversal for all tasks for each file
	- one traversal for each task or set of tasks


Starting dir arg from outset