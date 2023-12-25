import collections
import math

with open('input.txt') as file:
    LINES = file.read().strip().splitlines()

total = 0
broadcaster_dests = []
flipflops = {}
conjunctions = {}
for line in LINES:
    source, dests = line.split(' -> ')
    dests = dests.split(', ')
    if source == 'broadcaster':
        broadcaster_dests.extend(dests)
    else:
        prefix = source[0]
        if prefix == '%':
            flipflops[source[1:]] = [dests, 0]
        elif prefix == '&':
            conjunctions[source[1:]] = [dests, {}]

for line in LINES:
    source, dests = line.split(' -> ')
    dests = dests.split(', ')
    for dest in dests:
        if dest in conjunctions:
            conjunctions[dest][1][source[1:]] = 0

tot = [0, 0]
for i in range(1000):
    queue = collections.deque()
    queue.append(('broadcaster', broadcaster_dests, 0))
    tot[0] += len(broadcaster_dests) + 1

    while queue:
        source, dests, pulse_type = queue.popleft()
        for dest in dests:
            if dest in flipflops:
                if pulse_type == 0:
                    flipflops_state = flipflops[dest][1]
                    if flipflops_state == 0:
                        flipflops[dest][1] = 1
                    else:
                        flipflops[dest][1] = 0
                    send, state = flipflops[dest]
                    tot[state] += len(send)
                    queue.append((dest, send, state))
            elif dest in conjunctions:
                conjunctions[dest][1][source] = pulse_type
                send = conjunctions[dest][0]
                state = 0 if all(conjunctions[dest][1].values()) else 1
                tot[state] += len(send)
                queue.append((dest, send, state))

total = math.prod(tot)
print(total)

total = 0
broadcaster_dests = []
flipflops = {}
conjunctions = {}
rx_source = None
for line in LINES:
    source, dests = line.split(' -> ')
    dests = dests.split(', ')
    if dests[0] == 'rx':
        rx_source = source[1:]
    if source == 'broadcaster':
        broadcaster_dests.extend(dests)
    else:
        prefix = source[0]
        if prefix == '%':
            flipflops[source[1:]] = [dests, 0]
        elif prefix == '&':
            conjunctions[source[1:]] = [dests, {}]

__dests = []
for line in LINES:
    source, dests = line.split(' -> ')
    dests = dests.split(', ')
    if rx_source in dests:
        __dests.append(source[1:])
    for dest in dests:
        if dest in conjunctions:
            conjunctions[dest][1][source[1:]] = 0

tot = [0, 0]
patterns = [0 for _ in range(len(__dests))]
i = 0
while all([x != 0 for x in patterns]) is False:
    queue = collections.deque()
    queue.append(('broadcaster', broadcaster_dests, 0))
    tot[0] += len(broadcaster_dests) + 1

    while queue:
        source, dests, pulse_type = queue.popleft()
        for dest in dests:
            if dest in flipflops:
                if pulse_type == 0:
                    flipflops_state = flipflops[dest][1]
                    if flipflops_state == 0:
                        flipflops[dest][1] = 1
                    else:
                        flipflops[dest][1] = 0
                    send, state = flipflops[dest]
                    if i <= 1000:
                        tot[state] += len(send)
                    queue.append((dest, send, state))
            elif dest in conjunctions:
                conjunctions[dest][1][source] = pulse_type
                send = conjunctions[dest][0]
                state = 0 if all(conjunctions[dest][1].values()) else 1
                if i <= 1000:
                    tot[state] += len(send)
                queue.append((dest, send, state))
                if dest in __dests and state == 1:
                    patterns[__dests.index(dest)] = i + 1
    i += 1

print(math.lcm(*patterns))
