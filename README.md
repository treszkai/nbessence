# NBessence

Store in Git only what matters. An ipynb essence is a valid YAML file, with `.ipynbe` extension.

### Usage

a) Convert a notebook to its essence:
```bash
$ python nbessence_push.py example.ipynb
$ git add example.ipynbe  # or whatever else you want 
```

b) Convert the essence back to a full-fledged notebook:

_Coming soon!_

### Example output

```yaml
- code: |-
    line1 = "foo"
    if 1:
        line2 = 'bar'
    print(line1, line2)
  stdout: |-
    "foo"
    'bar'
- markdown: |-
    something
    bar
- raw: |-
    line 1
    line 2
```

### Limitations

For now we can only store output from the `stdout`. No `stderr`, no images.