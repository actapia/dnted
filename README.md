# dnted
`dnted` is a small Python library for computing a normalized edit distance metric between ordered labeled trees using the method presented in Li and Chenguang.

`dnted` uses the [zss module](https://github.com/timtadh/zhang-shasha) to compute absolute edit distances between ordered trees before normalizing and is desgined to be easy to use for those who have already used `zss`. In fact, the two most useful functions in `dnted``normalized_simple_distance` and `normalized_distance`are modelled after the coresponding `simple_dsitance` and `distance` functions provided by `zss`, respectively, and should be compatible with their arguments.

The most important difference between the `normalized` functions in `dnted` and those in `zss` is the presence of two additional arguments in `dnted``alpha` and `get_tree_size`. The former, `alpha`, is expected to be a number representing the maximum cost of adding or deleting a node. The latter, `get_tree_size`, is expected to be a function that gets the size of a given tree.

## References

* Yujian Li and Zhang Chenguang. 2011. A metric normalization of tree edit distance. Front. Comput. Sci China 5, 1 (March 2011), 119-125. DOI=http://dx.doi.org/10.1007/s11704-011-9336-2.


