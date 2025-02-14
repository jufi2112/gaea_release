from collections import namedtuple

Genotype = namedtuple("Genotype", "normal normal_concat reduce reduce_concat")

PRIMITIVES = [
    "none",
    "max_pool_3x3",
    "avg_pool_3x3",
    "skip_connect",
    "sep_conv_3x3",
    "sep_conv_5x5",
    "dil_conv_3x3",
    "dil_conv_5x5",
]

DARTS_OPS = [
    "none",
    "max_pool_3x3",
    "avg_pool_3x3",
    "skip_connect",
    "sep_conv_3x3",
    "sep_conv_5x5",
    "dil_conv_3x3",
    "dil_conv_5x5",
]

DARTS_NOZERO = [
    "max_pool_3x3",
    "avg_pool_3x3",
    "skip_connect",
    "sep_conv_3x3",
    "sep_conv_5x5",
    "dil_conv_3x3",
    "dil_conv_5x5",
]

SMALL = [
    "none",
    "max_pool_3x3",
    "skip_connect",
    "sep_conv_3x3",
]

SMALL_NOZERO = [
    "max_pool_3x3",
    "skip_connect",
    "sep_conv_3x3",
]

# each genotype consists of normal cell and reduce cell
# normal:   contains (in ascending order) for every intermediate node n entries (n=number of input connections that each node can have)
#           every entry is composed of (edge operation name, source node of the directed edge)
# normal_concat:    contains the nodes who's feature maps are combined to form the output
# reduce:   same as normal, but for reduction cell
# reduce_concat: same as normal_concat, but for reduction cell

NASNet = Genotype(
    normal=[
        ("sep_conv_5x5", 1),
        ("sep_conv_3x3", 0),
        ("sep_conv_5x5", 0),
        ("sep_conv_3x3", 0),
        ("avg_pool_3x3", 1),
        ("skip_connect", 0),
        ("avg_pool_3x3", 0),
        ("avg_pool_3x3", 0),
        ("sep_conv_3x3", 1),
        ("skip_connect", 1),
    ],
    normal_concat=[2, 3, 4, 5, 6],
    reduce=[
        ("sep_conv_5x5", 1),
        ("sep_conv_7x7", 0),
        ("max_pool_3x3", 1),
        ("sep_conv_7x7", 0),
        ("avg_pool_3x3", 1),
        ("sep_conv_5x5", 0),
        ("skip_connect", 3),
        ("avg_pool_3x3", 2),
        ("sep_conv_3x3", 2),
        ("max_pool_3x3", 1),
    ],
    reduce_concat=[4, 5, 6],
)

AmoebaNet = Genotype(
    normal=[
        ("avg_pool_3x3", 0),
        ("max_pool_3x3", 1),
        ("sep_conv_3x3", 0),
        ("sep_conv_5x5", 2),
        ("sep_conv_3x3", 0),
        ("avg_pool_3x3", 3),
        ("sep_conv_3x3", 1),
        ("skip_connect", 1),
        ("skip_connect", 0),
        ("avg_pool_3x3", 1),
    ],
    normal_concat=[4, 5, 6],
    reduce=[
        ("avg_pool_3x3", 0),
        ("sep_conv_3x3", 1),
        ("max_pool_3x3", 0),
        ("sep_conv_7x7", 2),
        ("sep_conv_7x7", 0),
        ("avg_pool_3x3", 1),
        ("max_pool_3x3", 0),
        ("max_pool_3x3", 1),
        ("conv_7x1_1x7", 0),
        ("sep_conv_3x3", 5),
    ],
    reduce_concat=[3, 4, 6],
)

DARTS_V1 = Genotype(
    normal=[
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 0),
        ("skip_connect", 0),
        ("sep_conv_3x3", 1),
        ("skip_connect", 0),
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 0),
        ("skip_connect", 2),
    ],
    normal_concat=[2, 3, 4, 5],
    reduce=[
        ("max_pool_3x3", 0),
        ("max_pool_3x3", 1),
        ("skip_connect", 2),
        ("max_pool_3x3", 0),
        ("max_pool_3x3", 0),
        ("skip_connect", 2),
        ("skip_connect", 2),
        ("avg_pool_3x3", 0),
    ],
    reduce_concat=[2, 3, 4, 5],
)
DARTS_V2 = Genotype(
    normal=[
        ("sep_conv_3x3", 0),
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 0),
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 1),
        ("skip_connect", 0),
        ("skip_connect", 0),
        ("dil_conv_3x3", 2),
    ],
    normal_concat=[2, 3, 4, 5],
    reduce=[
        ("max_pool_3x3", 0),
        ("max_pool_3x3", 1),
        ("skip_connect", 2),
        ("max_pool_3x3", 1),
        ("max_pool_3x3", 0),
        ("skip_connect", 2),
        ("skip_connect", 2),
        ("max_pool_3x3", 1),
    ],
    reduce_concat=[2, 3, 4, 5],
)

DARTS = DARTS_V2

ASHA200 = Genotype(
    normal=[
        ("skip_connect", 1),
        ("dil_conv_3x3", 0),
        ("sep_conv_3x3", 1),
        ("skip_connect", 0),
        ("none", 1),
        ("max_pool_3x3", 0),
        ("skip_connect", 1),
        ("dil_conv_3x3", 0),
    ],
    normal_concat=[2, 3, 4, 5],
    reduce=[
        ("max_pool_3x3", 1),
        ("avg_pool_3x3", 0),
        ("sep_conv_5x5", 1),
        ("skip_connect", 2),
        ("max_pool_3x3", 3),
        ("none", 1),
        ("skip_connect", 0),
        ("sep_conv_5x5", 4),
    ],
    reduce_concat=[2, 3, 4, 5],
)


edarts4 = Genotype(
    normal=[
        ("sep_conv_3x3", 0),
        ("skip_connect", 1),
        ("skip_connect", 0),
        ("skip_connect", 1),
        ("skip_connect", 0),
        ("skip_connect", 2),
        ("skip_connect", 0),
        ("dil_conv_3x3", 3),
    ],
    normal_concat=range(2, 6),
    reduce=[
        ("dil_conv_3x3", 1),
        ("max_pool_3x3", 0),
        ("skip_connect", 2),
        ("avg_pool_3x3", 0),
        ("skip_connect", 3),
        ("skip_connect", 2),
        ("skip_connect", 3),
        ("skip_connect", 4),
    ],
    reduce_concat=range(2, 6),
)

PC_DARTS_cifar = Genotype(
    normal=[
        ("sep_conv_3x3", 1),
        ("skip_connect", 0),
        ("sep_conv_3x3", 0),
        ("dil_conv_3x3", 1),
        ("sep_conv_5x5", 0),
        ("sep_conv_3x3", 1),
        ("avg_pool_3x3", 0),
        ("dil_conv_3x3", 1),
    ],
    normal_concat=range(2, 6),
    reduce=[
        ("sep_conv_5x5", 1),
        ("max_pool_3x3", 0),
        ("sep_conv_5x5", 1),
        ("sep_conv_5x5", 2),
        ("sep_conv_3x3", 0),
        ("sep_conv_3x3", 3),
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 2),
    ],
    reduce_concat=range(2, 6),
)
PC_DARTS_image = Genotype(
    normal=[
        ("skip_connect", 1),
        ("sep_conv_3x3", 0),
        ("sep_conv_3x3", 0),
        ("skip_connect", 1),
        ("sep_conv_3x3", 1),
        ("sep_conv_3x3", 3),
        ("sep_conv_3x3", 1),
        ("dil_conv_5x5", 4),
    ],
    normal_concat=range(2, 6),
    reduce=[
        ("sep_conv_3x3", 0),
        ("skip_connect", 1),
        ("dil_conv_5x5", 2),
        ("max_pool_3x3", 1),
        ("sep_conv_3x3", 2),
        ("sep_conv_3x3", 1),
        ("sep_conv_5x5", 0),
        ("sep_conv_3x3", 3),
    ],
    reduce_concat=range(2, 6),
)
