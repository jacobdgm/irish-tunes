# Validation

## Good
- correct number of beats in every measure
- number of measures per section is a power of 2 and/or multiple of 4
- material from the beginning or end of one section recurs at the beginning/end of a subsequent section

## Bad
- series of up to three repeated notes are fine, but 4 or more repeated notes should almost never happen
- leaps of more than an octave (eight pitches) should almost never happen
- nested tuplets, or any tuplets that are not triplets
- mismatched first and second repeats
- extremely long/short notes

## Short prompts
- when prompted with only "R: \<tune type\>", model should generate the proper value for M:
    - jig: 6/8
    - reel: 4/4
    - polka: 2/4
    - waltz: 3/4
    - hornpipe: 4/4
    - slip jig: 9/8
