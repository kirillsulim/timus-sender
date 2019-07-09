# timus-sender

Timus sender is simple python script to sent solution of problems to [timus](https://timus.online/).

## How to use

Pass required parameters to script:

```
sender.py --judge-id=<your id> --compiler=<compiler code> --problem=<problem id> <path/to/solution>
```

Script will return link to your submissons to this problem.

## Parameters deduction

All parameters can be deducted from context.

### judge-id

You can set value of your judge id in `.judge_id` file in your home directory.
In this case you can skip `judge-id` parameter and your judge id will be read from file.

### compiler

If `compiler` parameter doesn't passed to script compiler will be defined by file extension. Actual default compilers available in source code.

### problem

If `problem` parameter doesn't passed to script problem number will be defined by directory of file.
Possible directory name formats:

- `<problem id>`
- `<problem id>-<description>`
- `<description>-<problem id>`
