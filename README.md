# Digital Filter Comparison

I find myself writing simple "smoothing" digital filters a lot. The go-to choice is a standard moving window average. But then there's all that buffer management, initialisation, and looping. My fingers do get tired from all that typing. On the other hand a single pole IIR filter is about two lines of code, in any language, and you only need to store a single variable with no indexing, bugger all initialisation and no buffer management. So it's been nagging in the back of my mind: just how bad is a single pole IIR compared to a moving window average.

Behold, the answer awaits.
