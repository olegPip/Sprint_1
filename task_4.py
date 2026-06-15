new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1. Перенос "task_005" в одно действие через pop() и append()
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# 2. Удаление "task_007" из списка new_tasks
new_tasks.remove('task_007')

# 3. Вывести последнюю задачу из обновленного списка new_tasks
print(new_tasks[-1])

