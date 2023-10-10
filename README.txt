To implement the keyword search for statistically improbable phrases algorithm as described in Christian Rudder's *Dataclysm*

1. Pass the name of your input file to word counter.py (or word_counter_strip_412-.py) to create a new file sorted by rank order:

e.g. the format "rank + '\t' + word + '\t' + count"

word_counter_strip_412-.py does the same thing, but omits the most common N words from the English language 

2. rank_compiler.py can then be used on the rank output file [rank '\t' count '\t' word] to produce a file of the format:

Word	C rank		C percentile	S rank	S percentile	*Dist*

Where Dist is the Euclidean distance from the 100th %-ile of the speech and 0% of the corpus, with larger distance  = less significant