def loop_size(node):
    turtle = hare = node
    hare = hare.next.next
    turtle = turtle.next
    while hare != turtle:
        hare = hare.next.next
        turtle = turtle.next
    hare = hare.next.next  
    turtle = turtle.next
    cnt = 1
    while hare != turtle:
        turtle = turtle.next
        hare = hare.next.next
        cnt += 1
    return cnt