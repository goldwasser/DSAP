"""Provides several example applications for tree traversals."""

def toc_plain(T):
    for p in T.preorder():
        print(p.element())

def toc_indent_bad(T):
    for p in T.preorder():
        print(2*T.depth(p)*' ' + str(p.element()))  # beware of inefficiency

def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at p at depth d."""
    print(2*d*' ' + str(p.element()))               # use depth for indentation
    for c in T.children(p):
        preorder_indent(T, c, d+1)                  # child depth is d+1

def preorder_label(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j) for j in path)          # display path (e.g., "1.3.2")
    print(2*d*' ' + label, p.element())
    path.append(1)                                  # path entries are one-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path)             # child depth is d+1
        path[-1] += 1
    path.pop()

def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')                      # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '      # determine proper separator
            print(sep, end='')
            first_time = False                      # any future passes will not be the first
            parenthesize(T, c)                      # recur on child
        print(')', end='')                          # include closing parenthesis

def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p."""
    subtotal = p.element().space()                  # space used at position p
    for c in T.children(p):
        subtotal += disk_space(T, c)                # add child's space to subtotal
    return subtotal

def layout(T, p, d, x):
    if T.left(p) is not	None:
        x = layout(T, T.left(p), d+1, x)            # resulting x will be increased
    p.element().setX(x)
    p.element().setY(d)
    x =	x+1   	      	      	       	            # increment x
    if T.right(p) is not None:
        x = layout(T, T.right(p), d+1, x)           # resulting x will be increased
    return x
