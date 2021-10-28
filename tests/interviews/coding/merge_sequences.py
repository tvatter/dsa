# 01234567890123456789012
# Mary had a little lamb.
# |--|       |---------| GOLD
#   |--| |-|      |---|  PRED
#   ||            |---|  INTERSECT


def merge_and_add(out, one, two):
  a = max(one[0], two[0])
  b = min(one[1], two[1])
  if a <= b:
    out.append([a, b])


def calculate_intersect(gold, pred):
  out = []

  id_gold = 0
  id_pred = 0
  while id_gold < len(gold) and id_pred < len(pred):

    curr_gold = gold[id_gold]
    curr_pred = pred[id_pred]
    merge_and_add(out, curr_gold, curr_pred)

    if curr_pred[1] >= curr_gold[1]:
      id_gold += 1
    if curr_pred[1] <= curr_gold[1]:
      id_pred += 1

  return out


calculate_intersect([[0, 5], [10, 16]], [[2, 4], [8, 10], [14, 15]])
