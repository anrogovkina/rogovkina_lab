def find_common_participants(first_group, second_group, split_sign=","):
    list_first_group = first_group.split(split_sign)
    list_second_group = second_group.split(split_sign)
    set_first_group = set(list_first_group)
    set_second_group = set(list_second_group)
    result = list(set_first_group.intersection(set_second_group))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Список общих участников:", find_common_participants(participants_first_group, participants_second_group, "|"))

