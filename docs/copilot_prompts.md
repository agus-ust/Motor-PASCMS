# Copilot prompt templates (copy, fill the <>, paste PROJECT_CONTEXT.md first)

## 1. Build a feature
Context: <paste PROJECT_CONTEXT.md>. Today's task: <one feature, one sentence>.
Relevant BRD text: <paste only the needed section>. Golden test: <ID and expected value>.
Write: the test first, then the code. Complete files only. Tell me the file path for each file and how to run the test.

## 2. Fix a failure
This test fails. File: <path>. Code: <paste>. Error: <paste full traceback>. Expected from BRD: <value>.
Explain the cause in two sentences, then give the corrected complete file.

## 3. Explain before I commit
Explain this file line by line as if I must defend it to my mentor. List every assumption it makes and anything not in the BRD.

## 4. Review my diff
Here is my change: <paste>. Check against PROJECT_CONTEXT.md rules, money rounding, and the BRD. List problems by severity. Do not rewrite unless I ask.

## 5. End of day
Here is my status block and the files I changed: <paste>. Update the status block, list risks for tomorrow, and the first three tasks.
