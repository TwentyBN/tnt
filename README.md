# tnt

tnt is not tensorflow


We find it pretty annoying that you can't just

    pip install tensorflow

For that reason, we now suggest to run

    pip install tnt

## Version numbers

Version numbers for `tnt` consist of four numbers. The first three refer to the
corresponding tensorflow version, while the last one increases incrementally
and represents tnt-internal changes. This is useful, if you want to specify
`tnt` in a `requirements.txt` file as `tnt~=0.11`.


## Note on reinstalls

If you install tnt in multiple environments, note that `pip` will usually cache
previous installs. This means that the second time you install `tnt` tensorflow
*won't be installed for tensorflow versions before 0.12.0rc0*. To avoid this, you can install tnt like this

    pip install --no-cache-dir tnt

This will also work with requirements files (e.g. `pip install --no-cache-dir
-r requirements.txt`), but it won't work with requirements that you specify in your `setup.py`.
