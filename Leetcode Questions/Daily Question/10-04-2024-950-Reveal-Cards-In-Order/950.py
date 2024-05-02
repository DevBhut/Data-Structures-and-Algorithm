from collections import deque

def deckReveal(deck: list[int]) ->list[int]:
    deck.sort()
    n = len(deck)
    result = [0]*n
    indices = deque(range(n))
    for card in deck:
        idx = indices.popleft()
        result[idx] = card
        if indices:
            indices.append(indices.popleft())
    return result


# without using deque
def deckReveal2(deck: list[int]) -> list[int]:
    deck.sort()
    n = len(deck)
    result = [0]*n
    indices = [i for i in range(n)]
    for card in deck:
        idx = indices.pop(0)
        result[idx] = card
        if indices:
            indices.append(indices.pop(0))
    return result
    
    

print(deckReveal2([17,13,11,2,3,5,7]))