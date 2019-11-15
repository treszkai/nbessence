# NBessence

Store in Git only what matters.

Usage:

a) Convert a notebook to its essence:
```bash
$ python nbessence_push.py example.ipynb
$ git add example.ipynbe  # or whatever else you want 
```

b) Convert the essence back to a full-fledged notebook:

_Coming soon!_

### Limitations:

For now we can only store output from the `stdout`. No `stderr`, no images.