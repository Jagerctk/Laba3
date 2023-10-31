# TODO Напишите функцию find_common_participants
def fcp(pfg, psg, separator=','):
        pfg_list = pfg.split(separator)

        psg_list = psg.split(separator)
        result = []
        for ilichoblyat in pfg_list:
            if ilichoblyat in psg_list:
                result.append(ilichoblyat)
                result.sort()
        return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(fcp(participants_second_group,participants_first_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
