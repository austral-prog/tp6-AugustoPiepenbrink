def remove_elements(list_to_remove_elements):
    indices_to_remove = [0, 4, 5]
    return [item for i, item in enumerate(list_to_remove_elements) if i not in indices_to_remove]


def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    modified_list = []
    if len(list_of_lists_to_modify) >= 1:
        modified_list.append(list_of_lists_to_modify[0][:2])
    if len(list_of_lists_to_modify) >= 2:
        modified_list.append(list_of_lists_to_modify[1][1:4])
    if len(list_of_lists_to_modify) >= 3:
        modified_list.append(list_of_lists_to_modify[2][-2:])
    return modified_list
