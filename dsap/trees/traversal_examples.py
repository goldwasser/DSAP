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

def preorder_label(T, p, path):
    """Print labeled representation of subtree of T rooted at p reached by given path."""
    label = '.'.join(str(j) for j in path)          # display path (e.g., "1.3.2")
    print(2*len(path)*' ' + label, p.element())
    path.append(1)                                  # add path entry for first child
    for c in T.children(p):
        preorder_label(T, c, path)
        path[-1] += 1                               # increase last path entry
    path.pop()                                      # restore path to its incoming state

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
