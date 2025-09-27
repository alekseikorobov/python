TEMPLATE_NOTE = '''---
type: $type
add_dt: $add_dt
source_dt: $source_date
start_dt:
done_dt:
week: $week
source: $source
status: not_start
is_done: false
important:
complexity:
link: $link
длина: $duration
parent:
tags:
  - "#review" $tags
aliases:
---

---
```meta-bind-button
style: primary
label: "Mark START"
id: "start-button"
hidden: true
actions:
  - type: updateMetadata
    bindTarget: start_dt
    evaluate: true
    value: "moment().format('YYYY-MM-DD HH:mm:ss')"
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "progress"
  - type: updateMetadata
    bindTarget: week
    evaluate: true
    value: "moment().isoWeek()"
```
```meta-bind-button
style: primary
label: "Mark done"
id: "done-button"
hidden: true
actions:
  - type: updateMetadata
    bindTarget: done_dt
    evaluate: true
    value: "moment().format('YYYY-MM-DD HH:mm:ss')"
  - type: updateMetadata
    bindTarget: is_done
    evaluate: true
    value: true
  - type: updateMetadata
    bindTarget: "status"
    evaluate: false
    value: "done"
```
`BUTTON[start-button]`   `BUTTON[done-button]`

---

$description

'''


TEMPLATE_LEETCODE = '''---
difficulty: $difficulty
status: new
topics: $topics
date_add: $add_dt
date_done:
description_short:
description: ""
solution:
link: $link
parent: "[[leetcode]]"
tags: $tags
---


### Задание
$description

### Примеры


### Решение

```python

```

### Похожие задачи
$sim_questions


### Сложность
По времени 
По памяти
'''