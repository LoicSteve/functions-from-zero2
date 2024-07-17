[![Codespaces Prebuilds](https://github.com/LoicSteve/functions-from-zero2/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/LoicSteve/functions-from-zero2/actions/workflows/codespaces/create_codespaces_prebuilds)

# functions-from-zero2
A repo to learn functions


## Step 1: Configure Development environment

* configure Github Codespaces or the equivalent (Cloud9, etc)
* Create scaffold for structure of project: `Makefile` `requirements.txt`
* Optional(setup virtualenv) (install ipython out of requirements.txt)

## step 2: get interc ative debugging working

* use IPython and ipdb

```python
x = 1
y = 2
#import ipdb; ipdb.set_trace()
print(x+y)
```