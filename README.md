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
