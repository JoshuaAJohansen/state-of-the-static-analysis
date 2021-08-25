# The solution
main.py is a single python3 file with no dependencies. Drop it into a folder with python3 in your path, and you can execute it and see all of the tools that you can use to work more effectively with files.

These can vary from python's Black code formatter, to caniuse for javascript to determine which apis are available on different browsers, to TFSec for analyzing terraform infrastructure plans to detect improvements that could be made.

My plan is to continue to update the list of tools and file extensions here as better tools are found, so that we all can benefit from the collective tools that are built and available for us to use.

You too can use '[caniuse.com](https://caniuse.com) it's great for web development.'

---
# Scanning your code
Create a file at the root of your project, and copy the contents of 'main.py' into it, then run it using

# Running 
```sh
python3 main.py
```

# Using the results
Explore the suggestions you see in the console and which files they are useful for. If you have a codebase largely consisting of one type of file, then incorporating some tooling to scan that for you can have immense quality benefits for a code base, and your overall joy when coding.

# Future plans
- Configure it so that you can pass a path in and have it return the scan based on those files.
- Include links to good videos/blog posts that show how to configure the tools, run them, and best practices to follow.